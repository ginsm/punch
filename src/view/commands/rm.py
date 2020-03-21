# SECTION  VIEW - The command.rm.py view.
# =====================================================
def cannotDeleteCurrentJob(job):
  print('Unable to delete "%s". It is your currently selected job.' % job)
  return False


def deleted(job):
  print('Successfully deleted job "%s".' % job)
  return True


def notFound(job):
  print('Job "%s" does not exist.' % job)