# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import controller.command as command
import view.commands as view


# SECTION  HANDLER - Delegate arguments to the respective command handler.
# =====================================================
def handle(command, argument):
  if db.get_state() is False:
    return view.createFirstJob()

  if command is None:
    command = 'punch'
    
  handlers = {
    'punch': command.punch.handler,
    'p': command.punch.handler,
    'track': command.track.handler,
    't': command.track.handler,
    'rm': command.rm.handler,
    'r': command.rm.handler,
    'list': command.listall.handler,
    'l': command.listall.handler,
    'info': command.info.handler,
    'i': command.info.handler,
  }

  if (command not in handlers):
    return view.invalidCommand(command)

  return handlers[command](command, argument)
