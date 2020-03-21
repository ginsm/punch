# SECTION IMPORTS - External and internal imports.
# =====================================================
# External
import os

# Internal
import view.commands.list as view
from model.db import __dirname


# SECTION HANDLER - List the jobs you are tracking.
# =====================================================
def handler(command, argument):
  path = os.path.abspath(__dirname + '/database/')
  databases = [
    os.path.splitext(os.path.basename(f))[0]
    for f in os.listdir(path)
    if os.path.isfile(os.path.join(path, f))
  ]
  return view.listJobs(databases)