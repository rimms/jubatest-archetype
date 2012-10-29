import sys
from argparse import ArgumentParser

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
    return parser.parse_args()

def main():
    try:
      arguments = parse_options()
      for configfile in arguments.configfiles:
        print configfile
    except:
      sys.exit(1)
    sys.exit(0)
