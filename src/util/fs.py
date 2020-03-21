# SECTION IMPORTS - External and internal imports.
# =====================================================

# External
import json
import os


# SECTION FS - Utility functions for writing/reading files.
# =====================================================
def absolute_path(file = '', path = '', isState = False):
  subdirectory = '' if isState else '/database' 
  absolute = '%s%s/%s.json' % (path, subdirectory, file)
  return absolute


def writeFile(data, file_path):
  # Ensure the directory path exists
  if not os.path.exists(os.path.dirname(file_path)):
    try:
      os.makedirs(os.path.dirname(file_path))
    except OSError as exc: # Guard against race condition
      if exc.errno != errno.EEXIST:
          raise
  
  # Write the file
  with open(file_path, 'w') as fid:
    json.dump(data, fid, indent=2)


def readFile(file_path):
  with open(file_path) as fid:
    return json.load(fid)