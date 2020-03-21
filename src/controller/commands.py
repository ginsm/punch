# SECTION IMPORTS - External and internal imports.
# =====================================================
# Internal
import controller.command as command
import command.punch as punch
import command.job as job
import command.rm as rm


# SECTION  HANDLER - The command handler.
# =====================================================
def handle(command, argument):
  if command is None:
    command = 'punch'
    
  handlers = {
    'punch': punch.handler,
    'job': job.handler,
    'rm': rm.handler,
  }

  if (command not in handlers):
    # return view.invalidCommand(command)
    return

  return handlers[command](command, argument)
