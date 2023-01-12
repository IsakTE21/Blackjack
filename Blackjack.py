import random

# Create a deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4

# Shuffle the deck
random.shuffle(deck)

# Deal the cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Calculate the score for each hand
def calculate_score(hand):
  score = 0
  aces = 0
  for card in hand:
    if card == 11:
      aces += 1
    score += card
  while score <= 11 and aces > 0:
    score += 10
    aces -= 1
  return score

player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

# Check for natural blackjack
if player_score == 21:
    print("Player has a natural blackjack and wins!")
elif dealer_score == 21:
    print("Dealer has a natural blackjack and wins!")
else:
    # Print the hands and scores
    print("Player hand:", *player_hand, "(" + str(player_score) + ")")
    print("Dealer hand:", dealer_hand[0], "and another card")
  
    # Player's turn
    while player_score < 21:
      action = input("Do you want to hit or stand (h/s)? ")
      if action.lower() == "h":
        if deck:
          player_hand.append(deck.pop())
          player_score = calculate_score(player_hand)
          print("Player hand:", *player_hand, "(" + str(player_score) + ")")
        else:
          print("No more cards in the deck")
          break
        if player_score > 21:
          print("You bust!")
          break
      elif action.lower() == "s":
        break
      else:
        print("Invalid input, please enter h or s")
      
    # Dealer's turn
    if player_score <= 21:
      while dealer_score < 17:
        if deck:
          dealer_hand.append(deck.pop())
          dealer_score = calculate_score(dealer_hand)
          print("Dealer hand:", *dealer_hand, "(" + str(dealer_score) + ")")
          if dealer_score > 21:
            print("Dealer busts!")
            break
        else:
          print("No more cards in the deck")
          break
      # Decide winner
      if player_score > 21:
        print("Dealer wins!")
      elif dealer_score > 21:
        print("Player wins!")
      elif player_score > dealer_score:
        print("Player wins!")
      elif dealer_score > player_score:
        print("Dealer wins!")
      else:
        print("It's a tie!")

