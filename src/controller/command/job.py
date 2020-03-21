# SECTION IMPORTS - External and internal imports.
# =====================================================
# External
import re

# Internal
import view.commands.job as view
import model.db as db


# SECTION HANDLER - Job selection handlers.
# =====================================================
def handler(command, argument):
  if argument is None:
    return view.currentJob(str(db.get_state()['job']))

  if re.search('\/', argument) is not None:
    return view.invalidJobName(argument)

  db.set_state({'job': argument})

  if not db.exists(argument):
    schema = db.get_state('schema')
    schema['name'] = argument
    db.write(schema, argument)
  
  return view.newSelectedJob(argument)
