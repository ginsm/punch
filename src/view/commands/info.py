# SECTION  VIEW - The command.info.py view.
# =====================================================

def displayHours(hours, job):
  print('You are at %s hours for "%s".' % (hours, job))
  return True


def invalidJob(job):
  print('Unable to show hours for "%s"; it does not exist.' % job)
  return False