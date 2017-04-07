#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""create c++ classes automatically"""
import argparse, sys

SUCCESS = 0

def get_args():
    ''' define args and parse them, returns args '''
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def main(args):
    return SUCCESS

if __name__=='__main__':
    args = get_args()
    sys.exit(main(args))