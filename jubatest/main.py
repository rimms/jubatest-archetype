import sys
import os
import argparse

from jubatest.version import get_version
from jubatest.operator import Operator
from jubatest.util import is_readable, makedirs

def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-c',
    '--config',
    required = True,
    nargs    = '+',
    help     = 'configration files',
    metavar  = 'FILES',
    dest     = 'configfiles'
  )
  parser.add_argument(
    '-o',
    '--out',
    required = False,
    help     = 'output directory',
    metavar  = 'FILE',
    dest     = 'outdir'
  )
  parser.add_argument(
    '-v',
    '--version',
    action   = 'version',
    version  = '%(prog)s ' + get_version()
  )
  return parser.parse_args()

def main():
  outfile_prefix = 'result-'

  arguments = parse_options()

  outdir = arguments.outdir.rstrip('/') if arguments.outdir else None
  if outdir:
    makedirs(outdir)

  for configfile in arguments.configfiles:
    try:
      is_readable(configfile)
    except IOError as ioe:
      print ioe
      continue

    outfilename = outfile_prefix + os.path.basename(configfile)
    outfile = outdir + '/' + outfilename if outdir else outfilename

    try:
      operator = Operator(configfile)
      operator.run()
      operator.dump(outfile)
    except IOError as ioe:
      raise
