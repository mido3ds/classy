#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse
import sys
import os

SUCCESS = 0
FAIL = 1
STYLES = ["llvm", "google", "chromium", "mozilla", "webkit"]


def build_parser():
    ''' define args, return parser'''
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
    other.add_argument('--style', nargs='?', choices=STYLES,
                       default='webkit', const='webkit')
    other.add_argument('-u', '--using', nargs='+')

    return parser


def make_header_guards(class_name):
    ''' return top and down header guards of class name '''
    class_name = '__{}_H__'.format(class_name.upper())

    top = '#ifndef {0}\n#define {0}\n'.format(class_name)
    down = '\n#endif  /* {} */'.format(class_name)

    return top, down


def main(args):
    return SUCCESS

if __name__ == '__main__':
    args = build_parser().parse_args()
    sys.exit(main(args))
