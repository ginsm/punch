# SECTION  VIEW - The command.info.py view.
# =====================================================

def displayInformation(database, hours):
  print('\n'.join([
    'Name: %s' % database['name'],
    'Punched: %s' % database['lastAction'],
    'Total hours: %s' % hours,
  ]))
  return True


def invalidJob(job):
  print('Unable to show information for "%s"; it does not exist.' % job)
  return False