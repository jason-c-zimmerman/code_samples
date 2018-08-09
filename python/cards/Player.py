import Card
import Deck

class Player:

	def __init__(self, name, max_hand_count):
		self.name = name
		self.max_hand = max_hand_count
		self.hand = []
		self.points = 0

	def add_card_to_hand(self, card):
		if not self.full_hand():
			self.hand.append(card)

	def full_hand(self):
		return len(self.hand) >= self.max_hand

	def check_card_rank_match(self, pick):
		for card in self.hand:
			if pick.rank.name == card.rank.name and pick is not card:
				return card
		return None

def main():
	pass

if __name__ == "__main__":
	main()