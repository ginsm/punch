# SECTION  VIEW - The command.hours.py view.
# =====================================================

def displayHours(hours, job):
  print('You are currently %s hours into "%s"' % (hours, job))
  return True


def invalidJob(job):
  print('Unable to show hours for "%s"; it does not exist.' % job)
  return False