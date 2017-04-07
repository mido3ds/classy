#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse, sys, os

SUCCESS = 0
STYLES = ["LLVM", "Google", "Chromium", "Mozilla", "WebKit"]

def build_parser():
    ''' define args, return parser'''
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--out', nargs='?', default=os.getcwd())
    parser.add_argument('-I', '--include', nargs='+')
    parser.add_argument('-C', '--conf', nargs='?')

    parser.add_argument('--parent', nargs='+')
    parser.add_argument('--child', nargs='+')

    parser.add_argument('--style', nargs='?', choices=STYLES, default='WebKit')

    return parser

def main(args):
    return SUCCESS

if __name__=='__main__':
    parser = build_parser()
    args = parser.parse_args()
    sys.exit(main(args))