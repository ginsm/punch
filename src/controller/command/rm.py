# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import view.commands.rm as view


# SECTION HANDLER - Delete a job from the app.
# =====================================================
def handler(command, argument):
  current_job = db.get_state()['job']
  if argument == current_job:
    return view.cannotDeleteCurrentJob(current_job)
  if db.exists(argument):
    db.delete(argument)
    return view.deleted(argument)
  view.notFound(argument)
