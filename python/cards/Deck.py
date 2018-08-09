import Card
from random import shuffle

class Deck:
	cards = []
	
	def __init__(self):
		pass

	def create_deck(self):
		for suit in Card.suits:
			for rank in Card.ranks:
				self.cards.append(Card.Card(suit, rank))

	def shuffle(self):
		shuffle(self.cards)

	def sort(self):
		self.cards.sort(key=lambda card: card.rank.value)
		self.cards.sort(key=lambda card: card.suit.idx)

	def pop(self):
		if len(self.cards) > 0:
			return self.cards.pop()
		else:
			return None

	#def top(self):
	#	return self.cards.top()

	def push_top(self, card):
		self.cards.append(card)

	#def push_bottom(self, card):
	#	self.cards.insert(0, card)

def main():
	pass

if __name__ == "__main__":
	main()
