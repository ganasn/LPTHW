from nose.tools import *
import NAME  #Project name

def setup():
    print 'within setup()'

def teardown():
    print 'teardown()'
    
def test_basic():
    print 'execute'