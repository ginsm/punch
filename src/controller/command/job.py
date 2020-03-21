# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import re


# SECTION HANDLER - Job selection handlers.
# =====================================================
def handler(command, argument):
  if argument is None:
    print('Current Job: %s' % str(db.get_state()['job']))
    # return view.currentJob()
    return

  if re.search('\/', argument) is not None:
    # return view.invalidJobName(argument)
    return False

  db.set_state({'job': argument})

  if not db.exists(argument):
    schema = db.get_state('schema')
    schema['name'] = argument
    db.write(schema, argument)
  
  # return view.newSelectedJob(argument)
