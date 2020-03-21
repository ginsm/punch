# SECTION  VIEW - The command.track.py view.
# =====================================================
def jobNameRequired():
  print('You must provide a job name.')
  return True


def invalidCharacter(job):
  print('You cannot use \'/\' in your job name: "%s".' % job)
  return False


def newSelectedJob(job):
  print('You have selected "%s" as your current job.' % job)
  return True