#!/usr/bin/env python3.5
import unittest, classy

class TestArgs(unittest.TestCase):
    def setUp(self):
        self.parser = classy.make_parser()

    def test_include(self):
        pass

    def test_out(self):
        pass

if __name__=='__main__':
    unittest.main(verbosity=2)