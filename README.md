
Makes it more convenient to run shell commands.

    from easyrun import easyrun
    from quickfiles import *

    here = p(__file__).dir

    easyrun('ls')

    args = ('-n', 5)
    easyrun('head', args, here/'basic.py')


