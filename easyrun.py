
from __future__ import print_function
from quickfiles import *
from quickstructures import *
from subprocess import *

def easyrun(*cmd, **kwargs):
    return easyrunto(cmd, **kwargs)(lambda x: None)

def easyrunto(*cmd, **kwargs):
    wd = kwargs.get('wd', None)
    return runto(clean(cmd, wd), **kwargs)

def clean(cmd, wd=None, first=True):
    cleaned = []
    for c in cmd:
        if isinstance(c, Path):
            c.make_parents()
        
        if isinstance(c, Path):
            if wd != None:
                cleaned.append(c.against(wd))
            else:
                cleaned.append(str(c))
        elif isinstance(c, list) or isinstance(c, tuple):
            cleaned.extend(clean(c, wd=wd, first=first))
        else:
            cleaned.append(str(c))
        
        first = False
        
    return t(cleaned)

def runto(cmd, wd=None, stderr=None, verbose=False, echo=True):
    if echo and not verbose:
        print('\033[34m' + abbrev(cmd) + '\033[0m', file=sys.stderr) # ]]
    elif echo:
        print('\033[34m' + str(cmd) + ' (in ' + str(wd) + ')' + '\033[0m', file=sys.stderr) # ]]
    proc = Popen(cmd, stdout=PIPE, stderr=stderr, cwd=wd)
    def next(f):
        result = f(proc)
        status = proc.wait()
        if status != 0:
            raise RunFailed(' '.join(cmd) + ' returned ' + str(status) + ' exit status.')
        return result
    return next

def abbrev(cmd):
    return p(cmd[0]).name + ' ... ' + ' '.join(p(_).name
        for _ in cmd[1:] if not _.startswith('-'))

class RunFailed(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg
    def __repr__(self): return self.msg
    def __str__(self): return self.msg
    
def spy(hl, into=sys.stdout):
    from fcntl import fcntl, F_GETFL, F_SETFL
    from select import select
    import os, sys

    flags = fcntl(hl, F_GETFL)
    fcntl(hl, F_SETFL, flags | os.O_NONBLOCK)

    all = ''

    while True:
        select([hl], [], [])
        data = hl.read()
        if len(data) == 0: break
        into.write(data)
        into.flush()
        all = all + data
    
    return all

