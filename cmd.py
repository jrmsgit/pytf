from unittest.runner import TextTestRunner
from os.path import abspath
import suite

def main (srcdir, stream = None):
    s = suite.load (srcdir)
    if len (s._tests) > 0:
        r = TextTestRunner (stream = stream, verbosity = 2).run (s)
        return len (r.errors) or len (r.failures)
    else:
        print ("%s: no tests found" % abspath (srcdir))
        return 0
