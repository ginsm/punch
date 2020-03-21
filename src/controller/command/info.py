# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import util.timer as timer
import view.commands.info as view


# SECTION HANDLER - Get the information about a project.
# =====================================================
def handler(command, argument):
  if argument is None:
    file = db.get_state()['job']
    database = db.read(file)
  else:
    file = argument
    if db.exists(file):
      database = db.read(file)
    else:
      return view.invalidJob(file)

  hours = round(total_hours(database), 2)
  return view.displayInformation(database, hours)
    

def total_hours(database):
  if database['time'] == 0:
    return database['totalHours']
  return timer.get_new_hours(
    timer.current_time(),
    database['time'],
  ) + database['totalHours']