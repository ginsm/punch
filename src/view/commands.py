# SECTION  HANDLER - The command handler.
# =====================================================
def createFirstJob():
  print(
    'You must add your first job to use the program: ' +
    'punch job <name>.'  
  )
  return False

def invalidCommand(command):
  print('"%s" is not a valid command.' % command)
  return False