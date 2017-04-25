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


class Variable:
    ''' variable info '''
    type = None
    default_value = None
    name = None

    def __init__(self, string):
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
        self._create_members()
        pass

    def create_header_file(self):
        ''' stores string of header file '''
        pass

    def create_source_file(self):
        ''' stores string of source file '''
        pass

    def write_files(self):
        ''' writes src & hdr to out directory '''
        pass

    def stylize_files(self):
        ''' runs clang-format to sylize the file if found (or if style is on) '''
        pass

    def _get_header_guards(self):
        ''' return top and down header guards of class name '''
        part = '__{}_H__'.format(self.name.upper())

        top = '#ifndef {0}\n#define {0}\n'.format(part)
        down = '\n#endif  /* {} */'.format(part)

        return top, down

    def _create_members(self):
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
                        var = Variable(member)
                        self.variables.append(var)


######################################################################


def main(args):
    creator = ClassCreator(args)

    # create
    creator.create_header_file()
    creator.create_source_file()

    # write
    creator.write_files()

    # style
    creator.stylize_files()

    return SUCCESS

if __name__ == '__main__':
    args = build_parser().parse_args()
    sys.exit(main(args))
