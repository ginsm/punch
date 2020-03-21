# SECTION  VIEW - The command.listall.py view.
# =====================================================
def listJobs(jobs):
  output = 'Here are your jobs:\n'
  jobs = '\n'.join(jobs)
  print(output + jobs)
  return True