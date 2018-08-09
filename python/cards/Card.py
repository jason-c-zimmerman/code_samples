from collections import namedtuple

Suit = namedtuple("Suit", "idx name color")
Rank = namedtuple("Rank", "value name")

suits = (Suit(1, "diamonds", "red"), Suit(2, "hearts", "red"), Suit(3, "spades", "black"), Suit(4, "clubs", "black"))
ranks = (Rank(1, "ace"), Rank(2, "two"), Rank(3, "three"), Rank(4, "four"), Rank(5, "five"), Rank(6, "six"), 
		Rank(7, "seven"), Rank(8, "eight"), Rank(9, "nine"), Rank(10, "ten"), Rank(11, "jack"), Rank(12, "queen"), Rank(13, "king"))
#UP, DOWN = 1, 2 #card orientation

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		#self.facing = DOWN

	#def getColor(suit):
	#	return self.rank.color

	#def flip(self):
	#	self.facing = UP if (self.facing == DOWN) else DOWN
