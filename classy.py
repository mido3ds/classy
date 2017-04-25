#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse
import sys
import os
######################################################################
SUCCESS = 0
FAIL = 1
AVAILABLE_STYLES = ["llvm", "google", "chromium", "mozilla", "webkit"]
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
    args = []
    is_virtual = False
    access = None


class Class:
    ''' Class info '''
    name = None
    parents = None
    methods = None
    members = None


class Member:
    ''' member info '''
    type = None
    default_value = None
    name = None

######################################################################


class ClassCreator:
    ''' takes args from parser and constructs files '''
    src = None
    hdr = None

    def __init__(self, args):
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
        self.class_name = '__{}_H__'.format(self.class_name.upper())

        top = '#ifndef {0}\n#define {0}\n'.format(self.class_name)
        down = '\n#endif  /* {} */'.format(self.class_name)

        return top, down

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
