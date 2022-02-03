from binary_search import binary_search as bs
def locate_cards(cards, query):
  """This is a function to search a specific card in a list of cards."""
  
  def descending_condition(mid):
    """This condition function is defined for a list sorted in descending order."""

    if cards[mid]==query:
      if mid>0 and cards[mid-1]==query:
        return "left"
      else:
        return "found"
    elif cards[mid]>query:
      return "right"
    elif cards[mid]<query:
      return "left"
  return bs(0, len(cards)-1, descending_condition)

if __name__ == "__main__":
  print(locate_cards([13, 12, 11, 10, 7, 7, 4, 3], 7))