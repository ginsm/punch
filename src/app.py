# SECTION IMPORTS - External and internal imports.
# =====================================================
# External
import sys

# Internal
import controller.process as process
import controller.commands as commands



# SECTION Resolve command and argument.
# =====================================================
# Get the command line arguments
argv = sys.argv[1:]

# Resolve the command and argument
cmd = process.resolve(argv, 'command')
arg = process.resolve(argv, 'argument')

# Handle the command and argument
commands.handle(cmd, arg)
