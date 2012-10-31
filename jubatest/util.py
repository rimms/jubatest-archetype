import os

def is_readable(path):
  if not os.path.exists(path):
    raise IOError("\"" + path + "\" is not exist.")
  if not os.path.isfile(path):
    raise IOError("\"" + path + "\" is not File.")
  if not os.access(path, os.R_OK):
    raise IOError("\"" + path + "\" is not readable.")
