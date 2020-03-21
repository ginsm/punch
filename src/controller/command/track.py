# SECTION IMPORTS - External and internal imports.
# =====================================================
# External
import re

# Internal
import view.commands.track as view
import model.db as db


# SECTION HANDLER - Job selection handlers.
# =====================================================
def handler(command, argument):
  if argument is None:
    return view.jobNameRequired()

  if re.search('\/', argument) is not None:
    return view.invalidCharacter(argument)

  db.set_state({'job': argument})

  if not db.exists(argument):
    schema = db.get_state('schema')
    schema['name'] = argument
    db.write(schema, argument)
  
  return view.newSelectedJob(argument)
