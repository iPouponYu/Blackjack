import random

cards = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'Ace1':1, 'Ace10':11}

running = True    
def PlayerHand():
    global player_card_1 
    global player_card_2 

    player_card_1 = random.choices(list(cards.values()))
    player_card_2 = random.choices(list(cards.values()))
    print('Your hand: ' + str(player_card_1)+ str(player_card_2))
    return player_card_1, player_card_2

    
def CroupierHand():
    global croupier_card

    croupier_card = random.choices(list(cards.values()))
    print('Croupier hand is: ' + str(croupier_card))
    return croupier_card


def CroupierFlip():
    global croupier_card_2
    croupier_card_2 = random.choices(list(cards.values()))
    print ('Croupier hand: ' + str (croupier_card)  + str(croupier_card_2))
    


def Score():
    global playerscore
    playerscore = player_card_1[0] + player_card_2[0]
    return playerscore

def CroupierScore():
    global croupier_score
    croupier_score = croupier_card[0] + croupier_card_2[0]
    return croupier_score
    

def PlayerDecision():
    player_decision = True
    global player_score_new
    decision = input('Do you want to take the another card?')
    if decision == 'Yes':
        player_card_3 = random.choices(list(cards.values()))
        player_score_new = playerscore + player_card_3[0] 
        print('Your hand is: ' + str(player_card_1)+ str(player_card_2) + str(player_card_3))
        return player_score_new

def GameWinner():
    if croupier_score == 21:
        print('Croupier wins!')
        
    elif player_score_new > 21:
        print('Croupier wins!')
        
    elif croupier_score > player_score_new:
        print('Croupier wins!')
        
    elif player_score_new == 21:
        print ('Player wins!')
        
    elif croupier_score > 21:
        print('Player wins!')
        
    elif player_score_new < 21 and player_score_new > croupier_score:
        print('Player wins!')

def Running():
    global running

    running = input('Do you want to play again?')
    
    if running ==  'Yes':
        running = True
    else: 
        running = False
    return running
        

while running:       
    PlayerHand()
    Score()
    CroupierHand()
    PlayerDecision()
    CroupierFlip()
    CroupierScore()
    GameWinner()
    Running()



