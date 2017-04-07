#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import unittest, classy, os

class TestArgs(unittest.TestCase):
    def setUp(self):
        self.parser = classy.make_parser()

    def parse(self, string):
        return self.parser.parse_args(string.split())

    def test_include(self):
        args = self.parse('')
        self.assertEqual(args.include, None)

        args = self.parse('-I Me.h You.h')
        self.assertEqual(args.include, ['Me.h', 'You.h'])

        args = self.parse('--include Me.h You.h')
        self.assertEqual(args.include, ['Me.h', 'You.h'])

    def test_out(self):
        args = self.parse('-o .')
        self.assertEqual(args.out, '.')

        args = self.parse('')
        self.assertEqual(args.out, os.getcwd())

        args = self.parse('--out .')
        self.assertEqual(args.out, '.')

        args = self.parse('--out habal')
        self.assertEqual(args.out, 'habal')

if __name__=='__main__':
    unittest.main(verbosity=2)