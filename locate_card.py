# To find the location of a given card number from a list of cards placed(flipped) in sorted manner.
from binary_search import binary_search as bs
def locate_cards_descending_leftmost(cards, query):
  """This is a function to search a specific card in a list of cards."""
  
  def condition(mid):
    """This condition function is defined for a list sorted in descending order and to find left most index."""

    if cards[mid]==query:
      if mid>0 and cards[mid-1]==query:
        return "left"
      else:
        return "found"
    elif cards[mid]>query:
      return "right"
    elif cards[mid]<query:
      return "left"
  return bs(0, len(cards)-1, condition)

def locate_cards_ascending_leftmost(cards, query):
  """This is a function to search a specific card in a list of cards."""
  
  def condition(mid):
    """This condition function is defined for a list sorted in descending order and to find left most index."""

    if cards[mid]==query:
      if mid>0 and cards[mid-1]==query:
        return "left"
      else:
        return "found"
    elif cards[mid]<query:
      return "right"
    elif cards[mid]>query:
      return "left"
  return bs(0, len(cards)-1, condition)

def locate_cards_descending_rightmost(cards, query):
  """This is a function to search a specific card in a list of cards."""
  
  def condition(mid):
    """This condition function is defined for a list sorted in descending order and to find right most index."""

    if cards[mid]==query:
      if mid<len(cards)-1 and cards[mid+1]==query:
        return "right"
      else:
        return "found"
    elif cards[mid]>query:
      return "right"
    elif cards[mid]<query:
      return "left"
  return bs(0, len(cards)-1, condition)

def locate_cards_ascending_rightmost(cards, query):
  """This is a function to search a specific card in a list of cards."""
  
  def condition(mid):
    """This condition function is defined for a list sorted in descending order and to find right most index."""

    if cards[mid]==query:
      if mid<len(cards)-1 and cards[mid+1]==query:
        return "right"
      else:
        return "found"
    elif cards[mid]<query:
      return "right"
    elif cards[mid]>query:
      return "left"
  return bs(0, len(cards)-1, condition)