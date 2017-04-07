#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse, sys, os

SUCCESS = 0

def make_parser():
    ''' define args, return parser'''
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--out', nargs='?', default=os.getcwd())
    parser.add_argument('-I', '--include', nargs='+')
    # parser.add_argument()

    return parser

def main(args):
    return SUCCESS

if __name__=='__main__':
    parser = make_parser()
    args = parser.parse_args()

    print(args) # test
    sys.exit(main(args))