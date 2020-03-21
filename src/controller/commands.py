# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import model.db as db
import controller.command as command
import command.punch as punch
import command.track as track
import command.rm as rm
import command.list as listall
import command.info as info
import view.commands as view


# SECTION  HANDLER - Delegates to command handler.
# =====================================================
def handle(command, argument):
  if db.get_state() is False:
    return view.createFirstJob()

  if command is None:
    command = 'punch'
    
  handlers = {
    'punch': punch.handler,
    'p': punch.handler,
    'track': track.handler,
    't': track.handler,
    'rm': rm.handler,
    'r': rm.handler,
    'list': listall.handler,
    'l': listall.handler,
    'info': info.handler,
    'i': info.handler,
  }

  if (command not in handlers):
    return view.invalidCommand(command)

  return handlers[command](command, argument)
