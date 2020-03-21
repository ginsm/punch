# SECTION IMPORTS - External and internal imports.
# =====================================================
import time


# SECTION TIMER - Helps keep track of time/hours.
# =====================================================
def current_time():
  return round(time.time())


def get_new_hours(current_time, previous_time):
  return (current_time - previous_time) / 3600000
