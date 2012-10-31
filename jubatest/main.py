import sys
import argparse

from jubatest.version import get_version
from jubatest.operator import Operator
from jubatest.util import is_readable

def parse_options():
  parser = argparse.ArgumentParser()
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
    is_readable(configfile)
    operator = Operator(configfile)
    operator.run()
    operator.print_details()
