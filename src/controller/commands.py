# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import controller.command as command
import command.punch as punch
import command.job as job
import command.rm as rm
import command.list as lst
import command.hours as hours


# SECTION  HANDLER - The command handler.
# =====================================================
def handle(command, argument):
  if db.get_state() is False:
    # return view.createFirstJob()
    return False

  if command is None:
    command = 'punch'
    
  handlers = {
    'punch': punch.handler,
    'job': job.handler,
    'rm': rm.handler,
    'list': listall.handler,
    'hours': hours.handler,
  }

  if (command not in handlers):
    # return view.invalidCommand(command)
    return

  return handlers[command](command, argument)
