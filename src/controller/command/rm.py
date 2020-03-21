# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db


# SECTION HANDLER - Delete a job from the app.
# =====================================================
def handler(command, argument):
  return db.delete(argument)