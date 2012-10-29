import os

def isReadable(filepath):
  if not os.path.exists(filepath):
    raise IOError("\"" + filepath + "\" is not exist.")
  if not os.path.isfile(filepath):
    raise IOError("\"" + filepath + "\" is not File.")
