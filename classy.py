#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse
import os
import re
import sys
######################################################################
SUCCESS = 0
FAIL = 1
AVAILABLE_STYLES = ["llvm", "google", "chromium", "mozilla", "webkit"]

# #0: type, #1: name, #2: args, #?3: const|override|=0
REGEX_FUNC = re.compile(r'(.+) (\w+) ?\((.*)?\) ? ?(const|override|= ?0)?;?')
# #?0: unsigned or const, #1: type, #2: name, #?3: value
REGEX_MEMBER = re.compile(r'(const|unsigned)? ?(\w+) (\w+) ?=? ?(\w+)?')

HEADER_TEMPLATE = """\
{top}
{includes}
class {class_name} 
{{
{members}
}};

{bottom}
"""
######################################################################


def build_parser():
    ''' define args, return parser 
        for info refer to ArgumentParser doc.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('class_name')

    access = parser.add_argument_group('Access Modifiers')
    access.add_argument('-b', '--public', nargs='+', action='append')
    access.add_argument('-p', '--private', nargs='+', action='append')
    access.add_argument('-r', '--protected', nargs='+', action='append')

    files = parser.add_argument_group('Files')
    files.add_argument('-o', '--out', nargs='?', default=os.getcwd())
    files.add_argument('-I', '--include', nargs='+')
    files.add_argument('-C', '--conf', nargs='?')

    classes = parser.add_argument_group('Classes')
    classes.add_argument('--parent', nargs='+')
    classes.add_argument('--child', nargs='+')

    other = parser.add_argument_group('Other')
    other.add_argument('--style', nargs='?', choices=AVAILABLE_STYLES,
                       default='webkit', const='webkit')
    other.add_argument('-u', '--using', nargs='+')

    return parser

######################################################################


class Method:
    ''' method info '''
    name = None
    return_type = None
    args = None
    is_virtual = False
    access = None

    def __init__(self, string, access):
        ''' parse given string into a method '''
        self.access = access
        self.is_virtual = False  # TODO: add ability to make virtual

        try:
            tokens = re.findall(REGEX_FUNC, string)[0]
        except IndexError:
            raise Exception('exception in parsing the string {}'
                            ' to a method'.format(string))

        self.return_type = tokens[0]
        self.name = tokens[1]
        self.args = tokens[2]  # TODO: parse args
        # TODO: parse others

    def get_prototype(self):
        if self.is_virtual:
            return 'virtual' + self.return_type + ' ' + self.name + '(' + self.args + ');'
        else:
            return self.return_type + ' ' + self.name + '(' + self.args + ');'

    def get_decleration(self):
        pass


class Variable:
    ''' variable info '''
    type = None
    default_value = None
    name = None
    access = None

    def __init__(self, string, access): 
        ''' parse given string into a variable '''
        try:
            tokens = re.findall(REGEX_MEMBER, string)[0]
        except IndexError:
            raise Exception('exception in parsing the string {}'
                            ' to a variable'.format(string))

        if tokens[0]:
            self.type = tokens[0] + ' ' + tokens[1]
        else:
            self.type = tokens[1]
        self.name = tokens[2]
        self.default_value = tokens[3] or None
        self.access = access

    def __str__(self):
        if self.default_value:
            return str(self.type + ' ' + self.name + ' = ' + self.default_value + ';')
        else:
            return str(self.type + ' ' + self.name + ';')

######################################################################


class ClassCreator:
    ''' takes args from parser and constructs files '''
    src = None
    hdr = None

    name = None
    parents = []
    methods = []
    variables = []

    def __init__(self, args):
        self.args = args

        self.name = args.class_name

        self._create_members()
        self._create_parents()

    def create_header_file(self):
        ''' stores string of header file in hdr '''
        top, bottom = self._get_header_guards()

        self.hdr = HEADER_TEMPLATE.format(
            top=top, 
            includes=self._get_all_includes(),

            class_name=self.name,
            members='\n\n'.join(
                filter(
                    lambda x: x != '' ,
                    [self._get_members_definitions(access) for access in ['public', 'protected', 'private']]
                )
            ),

            bottom=bottom,
        )

    def create_source_file(self):
        ''' stores string of source file in src '''
        pass

    def _get_members_definitions(self, access_specifier):
        ''' return str of members definitions of access modifier '''

        head = access_specifier + ':' '\n    '
        methods = '\n    '.join([method.get_prototype() for method in self.methods if method.access == access_specifier])
        vars = '\n    '.join([str(variable) for variable in self.variables if variable.access == access_specifier])
        
        if not (methods or vars): return ''
        return  head + methods + ('\n    ' if methods and vars else '') + vars


    def write_files(self):
        ''' writes src & hdr to out directory '''
        pass

    def stylize_files(self):
        ''' runs clang-format to sylize the file if found (or if style is on) '''
        pass

    def _get_header_guards(self):
        ''' return top and down header guards of class name '''
        part = '__{}_H__'.format(self.name.upper())

        top = '#ifndef {0}\n#define {0}'.format(part)
        down = '#endif  /* {} */'.format(part)

        return top, down

    def _create_members(self):
        ''' iterate through members strings for all access_identifiers
         and parse them into Method/Variable object'''

        for access in ['public', 'protected', 'private']:
            members = getattr(self.args, access) or []

            # as public, private and protected are lists of lists,
            # plz blame ArgumentParser
            for sub_members in members:
                for member in sub_members:
                    if '(' in member:  # method
                        method = Method(member, access)
                        self.methods.append(method)
                    else:  # variable
                        var = Variable(member, access)
                        self.variables.append(var)

    def _create_parents(self):
        ''' add parents if found '''

        if self.args.parent:
            self.parents.extend(self.args.parent)

    def _get_hash_include(self, include_file):
        if False:
            return '#include <{}>'.format(include_file)
        else:
            return '#include "{}"'.format(include_file)

    def _get_all_includes(self):
        ''' return string of all includes that should be in header file '''
        if self.args.include:
            includes = self.args.include
            results = []

            for include in includes:
                # TODO: detect whther it is std or not
                results.append(self._get_hash_include(include))

            return '\n' + '\n'.join(result for result in results) + '\n'
        else:
            return ''

    def _get_include_this_header(self):
        return self._get_hash_include(self.name)

######################################################################


def main(args):
    creator = ClassCreator(args)

    # create
    creator.create_header_file(); print(creator.hdr)
    creator.create_source_file()

    # write
    creator.write_files()

    # style
    creator.stylize_files()

    return SUCCESS

if __name__ == '__main__':
    args = build_parser().parse_args()
    sys.exit(main(args))
