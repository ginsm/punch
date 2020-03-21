# SECTION IMPORTS - External and internal imports.
# =====================================================
# External
import os

# Internal
import view.commands.list as view
import model.db as db


# SECTION HANDLER - List the jobs you are tracking.
# =====================================================
def handler(command, argument):
  current_job = db.get_state()['job']
  path = os.path.abspath(db.__dirname + '/database/')
  databases = [
    is_current(
      os.path.splitext(os.path.basename(f))[0],
      current_job
    )
    for f in os.listdir(path)
    if os.path.isfile(os.path.join(path, f))
  ]
  return view.listJobs(databases)

def is_current(file, current_job):
  if current_job == file:
    return '* %s ' % file
  return file