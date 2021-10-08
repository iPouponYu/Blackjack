import random


cards = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'Ace1':1, 'Ace10':11}

class PlayerHand:

    player_card = random.choices(list(cards.values()))
    player_card_2 = random.choices(list(cards.values()))
    print('Your hand is: ' + str(player_card)+ str(player_card_2))
    

    def __repr__(self):
        return str(self.player_card + self.player_card_2)  
class CroupierHand:
        croupier_card = random.choices(list(cards.values()))
        print('Croupier hand is: ' + str(croupier_card))
class CroupierFlip:
    croupier_card_2 = random.choices(list(cards.values()))
    print('Croupier hand is: ' + str(croupier_card_2))


def score():
    playerscore = PlayerHand.player_card_2[0] + PlayerHand.player_card[0]
    return playerscore




PlayerHand()
CroupierHand()
print(score())




