def locate_cards(cards, query):
  lo, hi = 0, len(cards)
  while lo<=hi:
    mid = (lo + hi)//2
    if cards[mid]==query:
      return mid
    elif cards[mid] < query:
      lo = mid + 1
    elif cards[mid] > query:
      hi = mid - 1