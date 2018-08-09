import Player
import Card
import Deck
import time
import random

SIZE_OF_BEGINNING_HAND = 7

def main():
	deck = Deck.Deck()
	deck.create_deck()
	deck.shuffle()

	player1 = Player.Player("Cassandra", max_hand_count = 52)
	player2 = Player.Player("Alexandra", max_hand_count = 52)

	for i in range(SIZE_OF_BEGINNING_HAND):
		player1.add_card_to_hand(deck.pop())
		player2.add_card_to_hand(deck.pop())

	# print player1.name
	# for card in player1.hand:
	# 	print card.rank.name, "of", card.suit.name

	# print player2.name
	# for card in player2.hand:
	# 	print card.rank.name, "of", card.suit.name

#	print "Deck"
#	for card in deck.cards:
#		print card.rank.name, "of", card.suit.name

	for card1 in player1.hand:
		card2 = player1.check_card_rank_match(card1)
		if card2 is not None:
			print player1.name, "Match!", card1.rank.name, "of", card1.suit.name, "and", card2.rank.name, "of", card2.suit.name
			player1.hand.remove(card1)
			player1.hand.remove(card2)
			player1.points += 1

	for card1 in player2.hand:
		card2 = player2.check_card_rank_match(card1)
		if card2 is not None:
			print player2.name, "Match!", card1.rank.name, "of", card1.suit.name, "and", card2.rank.name, "of", card2.suit.name
			player2.hand.remove(card1)
			player2.hand.remove(card2)
			player2.points += 1

	curr_player = player1
	curr_opponent = player2


	while len(curr_player.hand) > 0:
		pick = random.choice(curr_player.hand)
		print curr_player.name, "says, I choose", pick.rank.name
		match = False
		card = curr_opponent.check_card_rank_match(pick)
		if card is not None:
			print "Match!", pick.rank.name, "of", pick.suit.name, "and", card.rank.name, "of", card.suit.name
			curr_player.hand.remove(pick)
			curr_opponent.hand.remove(card)
 			curr_player.points += 1
 			match = True
 		if not match:		
			print "Go Fish..."
			pick = deck.pop()
			if pick is None: break
			card = curr_player.check_card_rank_match(pick)
			if card is not None:
				print "Match!", pick.rank.name, "of", pick.suit.name, "and", card.rank.name, "of", card.suit.name
				curr_player.hand.remove(card)
				curr_player.points += 1
			else:
				curr_player.add_card_to_hand(pick)
			curr_player, curr_opponent = curr_opponent, curr_player
		
#		time.sleep(0.7)

	for card1 in player1.hand:
		card2 = player1.check_card_rank_match(card1)
		if card2 is not None:
			print player1.name, "Match!", card1.rank.name, "of", card1.suit.name, "and", card2.rank.name, "of", card2.suit.name
			player1.hand.remove(card1)
			player1.hand.remove(card2)
			player1.points += 1

	for card1 in player2.hand:
		card2 = player2.check_card_rank_match(card1)
		if card2 is not None:
			print player2.name, "Match!", card1.rank.name, "of", card1.suit.name, "and", card2.rank.name, "of", card2.suit.name
			player2.hand.remove(card1)
			player2.hand.remove(card2)
			player2.points += 1
			
	print player1.points, player2.points

if __name__ == "__main__":
	main()