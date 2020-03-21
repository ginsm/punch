# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db


# SECTION HANDLER - Job selection handlers.
# =====================================================
def handler(command, argument):
  if argument is None:
    print('Current Job: %s' % str(db.get_state()['job']))
    # return view.currentJob()
    return

  job = argument
  db.set_state({'job': job})

  if not db.exists(job):
    schema = db.get_state('schema')
    schema['name'] = job
    db.write(schema, job)
  
  # return view.newSelectedJob()
