import random

class Card:
  def __init__(self, value, suit):
    self.value = value;
    self.suit = suit;

  def __repr__(self):
    tmp = self.value + " of " + self.suit
    return tmp


class Deck:
  def __init__(self):
    self.cards = []
    self.fill()

  def fill(self):
    tmp = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    suits = ["Diamonds", "Clubs", "Spades", "Hearts"]
    for i in suits:
      for x in tmp:
        self.cards.append(Card(x, i))
  
  def __repr__(self):
    return ("Deck of %i cards" % int(self.count()))

  '''
  Returns the number of cards in the deck
  '''
  def count(self):
    return len(self.cards)

  ''' 
  Deals a card from the top of the deck.  If the Deck is empty, 
  it raises a ValueError
  '''
  def _deal(self, num):
    if len(self.cards)> num:
      for i in range(0, num):
        del self.cards[len(self.cards)-1]
    else:
      for i in range(0, len(self.cards)):
        del self.cards[len(self.cards)-1]
      raise ValueError("All cards have been dealt")
    return self.cards
  
  '''
  Shuffles the deck if the deck is full.  If the deck is not full, raises
  a ValueError
  '''
  def shuffle(self):
    if len(self.cards) == 52:
      for i in range(random.randint(0, 20), 50):
        tmp = self.cards[i]
        self.cards[i] = self.cards[(i+i)%52]
        self.cards[(i+i)%52] = tmp
    else:
      raise ValueError("Only full decks can be shuffled")
    return self.cards


  def deal_card(self):
    tmp_card = self.cards[len(self.cards)-1]
    self._deal(1)
    return tmp_card
  
  def deal_hand(self, num):
    tmp_cards = []
    for i in range(0, num):
      tmp_cards.append(self.cards[len(self.cards)-1])
      self._deal(1)
    return tmp_cards
  
