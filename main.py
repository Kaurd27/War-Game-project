import random
import player
import sys

##### Main program #####

# Get deck from the txt file
deck_of_cards = []
f = open('deck_b.txt', 'r')
for line in f:
    deck_of_cards.append(line.strip())

deck_of_cards = [int(i) for i in deck_of_cards]


# Get input from the users
player1_name = input('Name of player 1: ')
player2_name = input('Name of Player 2: ')

# Create player instances
player1 = player.Player(player1_name)
player2 = player.Player(player2_name)
deck1 = player1.deck
deck2 = player2.deck
pot = []


# Distribute the decks to the players
for i in range(0, len(deck_of_cards)-1, 2):
    deck1.append(deck_of_cards[i])
    deck2.append(deck_of_cards[i+1])

# Function for the battle
def battle(pot):

    #put the cards in the pot
    pot.append(deck1.pop(0))
    pot.append(deck1.pop(0))
    pot.append(deck1.pop(0))

    pot.append(deck2.pop(0))
    pot.append(deck2.pop(0))
    pot.append(deck2.pop(0))

    pot.append(deck1.pop(0))
    pot.append(deck2.pop(0))

    # player 1 wins if the card is higher.
    if pot[-2] > pot[-1]:
        deck1.extend(pot)
        pot.clear()
        return

    # player 2 wins if their card is higher.
    elif pot[-2] < pot[-1]:
        deck2.extend(pot)
        pot.clear()
        return

    # Another war begins if both cards are the same again
    elif pot[-2] == pot[-1]:
        if len(deck1) < 4:
            deck2.extend(pot)
            deck2.extend(deck1)
            pot.clear()
            deck1.clear()
            return

        elif len(deck2) < 4:
            deck1.extend(pot)
            deck1.extend(deck2)
            pot.clear()
            deck2.clear()
            return
            
        elif len(deck1) >= 4 and len(deck2) >= 4:
            battle(pot)
            return
  
    else:
        return

# Function to play 
def play(pot):
    pot.append(deck1.pop(0))
    pot.append(deck2.pop(0))


# Game beigns
count = 0
while deck1 and deck2:

    while len(deck1) != 0 and len(deck2) != 0:
        
        # pop one card from the front of the user's deck
        play(pot)
        count += 1

        # Apply the inequality appropriate for players cards
        if pot[-2] > pot[-1]:
            deck1.extend(pot)
            pot.clear()
            
        elif pot[-2] < pot[-1]:
            deck2.extend(pot)
            pot.clear()
        
        # War begins when players have the same cards
        elif pot[-2] == pot[-1]:
            
            #check the length of card deck 1
            if len(deck1) < 4:
                deck2.extend(pot)
                deck2.extend(deck1)
                pot.clear()
                deck1.clear()
                break
                
            #check the length of player 2
            elif len(deck2) < 4:
                deck1.extend(pot)
                deck1.extend(deck2)
                pot.clear()
                deck2.clear()
                break
            
            #if both have enough cards, then play a battle
            else:  
                battle(pot)
                break

    #Print results 
    if len(deck1) == 0:
        print("Player {} won in {} rounds.".format(player2_name, count))
    elif len(deck2) == 0:
        print("Player {} won in {} rounds.".format(player1_name, count))
    else:
        pass
