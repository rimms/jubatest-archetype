import sys
import traceback
from argparse import ArgumentParser
from jubatest.version import get_version
from jubatest.runner import execute

def parse_options():
    parser = ArgumentParser()
    parser.add_argument(
      '-f',
      '--file',
      required = True,
      nargs    = '+',
      help     = 'configration files',
      metavar  = 'FILES',
      dest     = 'configfiles'
    )
    parser.add_argument(
      '-v',
      '--version',
      action   = 'version',
      version  = '%(prog)s ' + get_version()
    )
    return parser.parse_args()

def main():
    arguments = parse_options()
    for configfile in arguments.configfiles:
        execute(configfile)
