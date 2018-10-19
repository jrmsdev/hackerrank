#!/usr/bin/env python3

import re

from sys import argv, exit
from os import path, scandir
from glob import glob
from unittest import TestSuite, FunctionTestCase, TextTestRunner

test_fn = re.compile (r'.*\.t[0-9]+$')
test_suite = TestSuite ()

class Test (FunctionTestCase):

    def __init__ (self, name):
        super ().__init__ (self.do_test)
        self.name = name

    def do_test (self):
        pass

    def __str__ (self):
        return self.name

def add_test (name):
    test_suite.addTest (Test (name))

def all_tests (script_filename):
    r = list ()
    patt = script_filename[:-3] + '.t*.in'
    for fn in sorted (glob (patt)):
        r.append (fn[:-3])
    return r

def xscandir (d):
    r = list ()
    with scandir (d) as it:
        for e in sorted (it, key = lambda x: x.name):
            if e.is_dir ():
                r.extend (xscandir (path.join (d, e.name)))
            elif e.name.endswith ('.py'):
                r.extend (all_tests (path.join (d, e.name)))
    return r

def find_tests (base):
    if test_fn.match (base):
        add_test (base)

    elif path.isdir (base):
        for x in xscandir (base):
            find_tests (x)

    elif path.isfile (base + '.py'):
        for t in all_tests (base + '.py'):
            find_tests (t)

    else:
        print ('INVALID:', base)

if __name__ == '__main__':
    # find tests
    if len (argv) > 1:
        for patt in sorted (argv[1:]):
            find_tests (patt)
    else:
        with scandir ('.') as it:
            for e in sorted (it, key = lambda x: x.name):
                if e.is_dir ():
                    if not e.name.startswith ('.') and not e.name.startswith ('_'):
                        find_tests (e.name)

    # run tests
    rnr = TextTestRunner (verbosity = 2)
    rst = rnr.run (test_suite)

    exit (1 if len (rst.errors) + len (rst.failures) > 0 else 0)
