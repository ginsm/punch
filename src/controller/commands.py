# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import controller.command as command
import command.punch as punch
import command.job as job
import command.rm as rm
import command.list as listall
import command.hours as hours
import view.commands as view


# SECTION  HANDLER - The command handler.
# =====================================================
def handle(command, argument):
  if db.get_state() is False:
    return view.createFirstJob()

  if command is None:
    command = 'punch'
    
  handlers = {
    'punch': punch.handler,
    'p': punch.handler,
    'job': job.handler,
    'j': job.handler,
    'rm': rm.handler,
    'r': rm.handler,
    'list': listall.handler,
    'l': listall.handler,
    'hours': hours.handler,
    'h': hours.handler,
  }

  if (command not in handlers):
    return view.invalidCommand(command)

  return handlers[command](command, argument)
