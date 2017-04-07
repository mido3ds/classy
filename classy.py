#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse, sys, os

SUCCESS = 0
FAIL = 1
STYLES = ["LLVM", "Google", "Chromium", "Mozilla", "WebKit"]

def build_parser():
    ''' define args, return parser'''
    parser = argparse.ArgumentParser()

    files = parser.add_argument_group('Files')
    files.add_argument('-o', '--out', nargs='?', default=os.getcwd())
    files.add_argument('-I', '--include', nargs='+')
    files.add_argument('-C', '--conf', nargs='?')

    classes = parser.add_argument_group('Classes')
    classes.add_argument('--parent', nargs='+')
    classes.add_argument('--child', nargs='+')

    other = parser.add_argument_group('Other')
    other.add_argument('--style', nargs='?', choices=STYLES, default='WebKit')
    other.add_argument('-u', '--using', nargs='+')

    return parser

def main(args):
    return SUCCESS

if __name__=='__main__':
    args = build_parser().parse_args()
    sys.exit(main(args))