#!/usr/bin/env python

from easyrun import easyrun
from quickfiles import *

here = p(__file__).dir

easyrun('ls')
print('')

args = ('-n', 5)
easyrun('head', args, here/'basic.py')
print('')

