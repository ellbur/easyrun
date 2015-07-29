# easyrun

Makes it easy to run shell commands from Python:

    easyrun('gcc', '-o', bin, options, sources)
    user = easyrun('whoami')

Does the following things:

 * Converts numbers and other non-strings to strings
 * Flattens nested lists and tuples
 * Echoes the command and output in color
 * Captures output and returns a string
 * Checks return code for 0
 
Depends on [quickfiles](https://github.com/ellbur/quickfiles), [quickstructures](https://github.com/ellbur/quickstructures).
