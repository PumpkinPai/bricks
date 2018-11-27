
* Collection of example python code for simple things done every damn time

* Don't run it.

* It's python3



## START OF IT ALL
#/usr/bin/python3

if __name__ == "__main__":
    exit()


## SUBPROCESS
import subprocess
cmd = "vim"
arg = "example.txt"

subprocess.call([cmd, arg])


## COMMAND LINE ARGUMENTS
import sys
try:
    arg = sys.argv[1]
    arg = arg.lower()
except:
    arg = ''


## STRINGS
    - substrings
        exStr = 'abcdef'
        exStr[0:3]      >> 'abc'
        exStr[:2]       >> 'ab'
        exStr[:-3]      >> 'abc'
        exStr[3:-1]     >> 'de'
        exStr[-3:]      >> 'def'

    - lower/capital
        exStr.lower()
        exStr.upper()

