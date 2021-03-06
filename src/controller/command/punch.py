# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import util.timer as timer
import view.commands.punch as view


# SECTION HANDLER - Punch in and out handlers.
# =====================================================
def handler(command, argument):
  file = db.get_state()['job']
  database = db.read(file)
  last_action = str(database['lastAction'])
  
  if last_action == 'in':
    return punch_out(database)

  if last_action == 'out':
    return punch_in(database)
  

def punch_out(database):
  new_total_hours = timer.total_hours(database)
  
  db.write({
    'totalHours': new_total_hours,
    'time': 0,
    'lastAction': 'out',
    'name': database['name'],
  }, database['name'])

  return view.punched_out(database, new_total_hours)


def punch_in(database):
  db.write({
    'totalHours': database['totalHours'],
    'time': timer.current_time(),
    'lastAction': 'in',
    'name': database['name'],
  }, database['name'])

  return view.punched_in(database)
  