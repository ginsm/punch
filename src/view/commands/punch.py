# SECTION  VIEW - The command.punch.py view.
# =====================================================
def punched_out(database, hours):
  name = database['name']
  hours = round(hours, 2)
  print('Punching out with a total of %s hours for "%s".' % (hours, name))
  return True


def punched_in(database):
  name = database['name']
  hours = round(database['totalHours'], 2)
  print('Punching in with a total of %s hours for "%s".' % (hours, name))
  return True