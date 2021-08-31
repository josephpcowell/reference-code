"""
This document will hold helpful functions to reference
when needed in the future
"""


def month_diff(a, b):
  """
  Returns month delta between two datetime objects
  Args:
    a: a datetime
    b: the other datetime
    
  Returns:
    Integer representing the difference in months between the two dates.
  """
  return 12 * (a.dt.year - b.dt.year) + (a.dt.month - b.dt.month)
