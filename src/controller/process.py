# SECTION PROCESS - Processes command line arguments.
# =====================================================
def resolve(args = [], type = ''):
  # Get the index of the type to resolve
  index = {'command': 0, 'argument': 1}[type]

  # Ensure the args list has enough items
  if len(args) > index:
    # Return the item
    return args[index]
  return None
