# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db


# SECTION HANDLER - Delete a job from the app.
# =====================================================
def handler(command, argument):
  current_job = db.get_state()['job']
  if argument == current_job:
    # return view.cannotDeleteCurrentJob(current_job)
    return False
  return db.delete(argument)
