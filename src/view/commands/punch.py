# SECTION  VIEW - The command.punch.py view.
# =====================================================
def punched_out(database, hours):
  name = database['name']
  hours = round(hours, 2)
  print('Punching out at %s hours for job: %s.' % (hours, name))
  return True

def punched_in(database):
  name = database['name']
  hours = round(database['totalHours'], 2)
  print('Punching in with %s hours for job: %s.' % (hours, name))
  return True