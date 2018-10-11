#!/usr/bin/env python3

from sys import exit, argv, executable
from os import sep
from os.path import abspath, dirname, isdir, isfile, join
from glob import glob
import subprocess

DEBUG = False
verbose = False
mydir = abspath (dirname (argv[0]))
total_checks = 0
passed_checks = 0


def dbg (*s):
    if DEBUG: print (*s)


def getPath (p):
    a = abspath (p)
    if a == mydir:
        return '.'
    else:
        return a.replace (mydir + sep, '')


def getScripts (base):
    patts = [
        join (base, '*.py'),
        join (base, '*/*.py'),
    ]
    fl = set ()
    for p in patts:
        for f in glob (p):
            fl.add (getPath (f))
    dbg ('getFiles:', patts, fl)
    return fl


def getTests (n):
    dbg ('getTestFiles:', n)
    tpatt = n + '.t*.in'
    return sorted ([t.replace ('.in', '') for t in glob (tpatt)])


def doTest (t):
    cmd = '{exe} {script} <{infile} >{outfile}'.format (
            exe = executable, script = f,
            infile = t+'.in', outfile = t+'.result')
    dbg ('t:', cmd)
    subprocess.run (cmd, shell = True)


def checkTest (t):
    global total_checks, passed_checks
    efn = t+'.out'
    rfn = t+'.result'
    expect = None
    result = None
    with open (efn, 'r') as efh:
        expect = efh.read ()
        efh.close ()
    with open (rfn, 'r') as rfh:
        result = rfh.read ()
        rfh.close ()
    print (t, end = '')
    total_checks += 1
    if expect is None:
        print (' FAIL')
        print ('ERROR: could not get test expect info (.in file)')
        return False
    if result is None:
        print (' FAIL')
        print ('ERROR: could not get test result info (.result file)')
        return False
    if result != expect:
        print (' FAIL')
        print ('expect: {} - got: {}'.format (expect, result))
        return False
    print (' PASS')
    passed_checks += 1
    if verbose:
        print ('got:', result.strip ())


def runTests (f):
    dbg ('runTests:', f)
    for t in getTests (f.replace ('.py', '')):
        doTest (t)
        checkTest (t)


if __name__ == '__main__':
    dbg (mydir)
    try:
        verbose_opt = argv.index ('-v')
        verbose = True
        argv.pop (verbose_opt)
    except ValueError:
        pass
    for p in map (getPath, argv[1:]):
        dbg (p)
        if isdir (p):
            dbg ('DIR')
            for f in sorted (getScripts (p)):
                runTests (f)
        elif isfile (p):
            dbg ('FILE')
            runTests (p)
        else:
            dbg ('INVALID')
    print ('Total:', total_checks, 'checks -', total_checks - passed_checks, 'failed')
    exit (0)
