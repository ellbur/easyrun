#!/usr/bin/env python

from easyrun import easyrunto
from quickfiles import *
from sys import stdout

here = p(__file__).dir

@easyrunto('cat', here/'basic.py')
def _(proc):
    for line in proc.stdout:
        if line.find('a') != -1:
            print(line.strip())
            sys.stdout.flush()

