
from __future__ import print_function
from quickfiles import *
from quickstructures import *

def easyrun(*cmd, **kwargs):
    wd = kwargs.get('wd', None)
    return run(clean(cmd, wd), **kwargs)

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

def run(cmd, echo=True, verbose=False, env={}, into=None, wd=None, wait=True, capture=False, stderr=None):
    full_env = dict(os.environ)
    for k in env: full_env[k] = env[k]
    if echo and not verbose:
        print('\033[34m' + abbrev(cmd) + '\033[0m', file=sys.stderr) # ]]
    elif echo:
        print('\033[34m' + str(cmd) + ' (in ' + str(wd) + ')' + '\033[0m', file=sys.stderr) # ]]
    sys.stdout.flush()
    if capture:
        sink = PIPE
    else:
        sink = open(str(into), 'w') if into!=None else None
    cwd = str(wd) if wd != None else None
    if isinstance(stderr, basestring):
        stderr = open(stderr, 'w')
    proc = Popen(map(str, cmd), env=full_env, stdout=sink, stderr=stderr, cwd=cwd)
    if wait:
        code = proc.wait()
        if into != None: sink.close()
        if code != 0:
            raise BuildFailed(' '.join(cmd) + ' returned ' + str(code) + ' exit status')
        if capture:
            return proc.communicate()[0]
        else:
            return None
    else:
        return None
    
def abbrev(cmd):
    return p(cmd[0]).name + ' ... ' + ' '.join(p(_).name
        for _ in cmd[1:] if not _.startswith('-'))

