# SECTION  VIEW - The command.job.py view.
# =====================================================
def currentJob(job):
  print('Your currently selected job is "%s".' % job)
  return True

def invalidJobName(job):
  print('You cannot use "%s" as a job name.' % job)
  return False

def newSelectedJob(job):
  print('You have selected "%s" as your current job.' % job)
  return True