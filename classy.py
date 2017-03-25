#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""Classy, create c++ classes automatically"""
import argparse, sys

class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(ArgumentParser, self).__init(args, kwargs)

        # add arguments

def main(args):
    return 0

if __name__=='__main__':
    args = ArgumentParser().parse_args()
    sys.exit(main(args))