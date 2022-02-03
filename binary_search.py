def binary_search(lo, hi, condition):

  """Generic binary search function which takes three inputs the first index, last index and the condition."""
  while lo<=hi:
    mid = (lo + hi)//2
    cond_test = condition(mid)
    if cond_test == "found":
      return mid
    elif cond_test == "left":
      hi = mid - 1
    elif cond_test == "right":
      lo = mid + 1
  return -1