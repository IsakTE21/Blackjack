import random

# Create a deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# Shuffle the deck
random.shuffle(deck)

# Deal the cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Calculate the score for each hand
def calculate_score(hand):
  score = 0
  for card in hand:
    if card == 11 or card == 12 or card == 13:
      score += 10
    elif card == 14:
      if score >= 11:
        score += 1
      else:
        score += 11
    else:
      score += card
  return score

player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

# Print the hands and scores
print("Player hand:", *player_hand, "(" + str(player_score) + ")")
print("Dealer hand:", *dealer_hand, "(" + str(dealer_score) + ")")

# Player's turn
while player_score < 21:
  action = input("Do you want to hit or stand (h/s)? ")
  if action.lower() == "h":
    player_hand.append(deck.pop())
    player_score = calculate_score(player_hand)
    print("Player hand:", *player_hand, "(" + str(player_score) + ")")
    if player_score > 21:
      print("You bust!")
      break
  elif action.lower() == "s":
    break

# Dealer's turn
if player_score <= 21:
  while dealer_score < 17:
    dealer_hand.append(deck.pop())
    dealer_score = calculate_score(dealer_hand)
    print("Dealer hand:", *dealer_hand, "(" + str(dealer_score) + ")")
    if dealer_score > 21:
      print("Dealer busts!")
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
