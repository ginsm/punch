# SECTION IMPORTS - External and internal imports.
# =====================================================
# External
import os

# Internal
import util.fs as fs


# SECTION VARIABLES - Global variables for db.py.
# =====================================================
__dirname = os.path.dirname(__file__)


# SECTION DATABASE - Controls the database files.
# =====================================================
def write(data, file):
  file_existed = False if exists(file) else True
  fs.writeFile(
    data,
    fs.absolute_path(file, __dirname),
  )
  return file_existed


def read(file):
  if exists(file):
    return fs.readFile(
      fs.absolute_path(file, __dirname),
    )


def delete(file):
  if exists(file):
    os.remove(
      fs.absolute_path(file, __dirname)
    )
    return True
  return False


# SECTION STATE - Controls the state of the application.
# =====================================================
def set_state(data):
  return fs.writeFile(
    data,
    fs.absolute_path('state', __dirname, True),
  )


def get_state(file = 'state'):
  file_path = fs.absolute_path(file, __dirname, True)
  if os.path.exists(file_path):
    return fs.readFile(file_path)
  return False


# SECTION HELPER - Functions that are used by both.
# =====================================================
def exists(file = ''):
  file = fs.absolute_path(file, __dirname)
  return os.path.exists(file)
