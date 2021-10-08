import random

cards = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'Ace':[1, 10]}

class PlayerHand:
    player_card = random.choices(list(cards.values()))
    player_card_2 = random.choices(list(cards.values()))

    def __repr__(self):
        return str(self.player_card + self.player_card_2)  


player_cards = PlayerHand()
print(player_cards)




