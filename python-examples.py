
* Collection of example python code for simple things done every damn time

* Don't run it.

* It's python3



## START OF IT ALL
#/usr/bin/python3

if __name__ == "__main__":
    exit()

## DIRECTORY STUFF
import os
curdir = os.getcwd()
newdir = '/newdir'
try:
    os.mkdir(newdir)
except OSError:
    print("Creation failed for %s" % newdir)
else:
    print("Success at life and making %s" % newdir


## SUBPROCESS
import subprocess
cmd = "vim"
arg = "example.txt"

subprocess.call([cmd, arg])


## COMMAND LINE ARGUMENTS
import sys
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except:
    arg1 = ''

## NAMED COMMAND LINE ARGUMENTS
import argparse, sys
parser = argparse.ArgumentParser(description='do some things and other')
parser.add_argument('--thing', help = 'This is what thing does')
parser.add_argument('-o', '--other', help = 'This is what other is')
args = parser.parse_args()
thingWeWant = args.thing
print(args)
print(sys)

call: script.py --thing=value1 --other value2
prints-->   thing='value1', other="value2"
            ['script.py', '--thing=value1', '--other', 'value2']

call: script.py -h
prints-->
usage: script.py [-h] [--thing value1] [--other value2]
optional arguments:
    -h, --help show this message and exit
    -- thing value1  This is what thing does
    -- other value2  This is what other is


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

