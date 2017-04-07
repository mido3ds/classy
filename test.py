#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import unittest, classy, os

class TestArgs(unittest.TestCase):
    def setUp(self):
        self.parser = classy.build_parser()

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

    def test_conf(self):
        args = self.parse('-C .')
        self.assertEqual(args.conf, '.')

        args = self.parse('')
        self.assertEqual(args.conf, None)

        args = self.parse('--conf .')
        self.assertEqual(args.conf, '.')

        args = self.parse('--conf habal.cf')
        self.assertEqual(args.conf, 'habal.cf')

    def test_parent(self):
        args = self.parse('')
        self.assertEqual(args.parent, None)

        args = self.parse('--parent .')
        self.assertEqual(args.parent, ['.'])

        args = self.parse('--parent habal habal2 habal3')
        self.assertEqual(args.parent, 'habal habal2 habal3'.split())

    def test_child(self):
        args = self.parse('')
        self.assertEqual(args.child, None)

        args = self.parse('--child .')
        self.assertEqual(args.child, ['.'])

        args = self.parse('--child habal habal2 habal3')
        self.assertEqual(args.child, 'habal habal2 habal3'.split())

    def test_style(self):
        args = self.parse('')
        self.assertEqual(args.style, 'webkit')

        args = self.parse('--style mozilla')
        self.assertEqual(args.style, 'mozilla')

        with self.assertRaises(SystemExit):
            self.parse('--style habal')

        with self.assertRaises(SystemExit):
            self.parse('--style mozilla webkit')

        args = self.parse('--style')
        self.assertEqual(args.style, 'webkit')

    def test_using(self):
        args = self.parse('')
        self.assertIsNone(args.using)

        args = self.parse('--using .')
        self.assertEqual(args.using, ['.'])

        args = self.parse('--using habal habal2 habal3')
        self.assertEqual(args.using, 'habal habal2 habal3'.split())

        args = self.parse('-u habal habal std')
        self.assertEqual(args.using, 'habal habal std'.split())

if __name__=='__main__':
    unittest.main(verbosity=2)