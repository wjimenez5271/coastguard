#!/usr/bin/python
import sys
sys.path.append('../')

import unittest
from coastguard.lib.hostfilter import HostFilter
from collections import namedtuple

TestHost = namedtuple("TestHost", "name, blah")

class HostFilterTestCase(unittest.TestCase):
    def setUp(self):
        whitelist = ["abc", "de.*", "ooo"]
        blacklist = ["ab.*", "pooo", "^ghi"]
        self.hostFilter = HostFilter(whitelist, blacklist)

        self.testCases = {
            "abc": True,
            "def": True,
            "ghi": False,
            "abb": False,
            "ooop": True,
            "pooo": False,
            "lala": True
        }

    def test_allowed(self):
        for case, expected in self.testCases.iteritems():
            if self.hostFilter.allowed(case) != expected:
                self.fail("Failed pattern {0}, expected {1}".format(case, expected))

    def test_allowed_with_attribute(self):
        for case, expected in self.testCases.iteritems():
            host = TestHost(case, False)
            if self.hostFilter.allowed(host, 'name') != expected:
                self.fail("Failed pattern {0}, expected {1}".format(case, expected))

    def test_filter(self):
        cases = self.testCases.keys()
        filtered = self.hostFilter.filter(cases)
        expected = [x for x, expected in self.testCases.iteritems() if expected]
        self.assertItemsEqual(filtered, expected)

    def test_filter_with_attribute(self):
        cases = [TestHost(case, True) for case in self.testCases.keys()]
        filtered = self.hostFilter.filter(cases, 'name')
        expected = [TestHost(case, True) for case, expected in self.testCases.iteritems() if expected]
        self.assertItemsEqual(filtered, expected)

if __name__ == '__main__':
    unittest.main()
