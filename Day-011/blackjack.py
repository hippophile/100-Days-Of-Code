"""
A simple CLI blackjack game with infinite number of cards
It feautures: add_cards() mechanism that determines if an ace has to be counted as an 11 or an Ace
deal_card() which selects a random card from the infinite deck
and the winner() that based to the sums of the payer's and the computer's cards will determine the winner.

In this blackjack:
The dealer/computer draws as many cards as the player
If the dealer/computer has 21 he wins no matter what
In the case of draw nobody wins

TODO : Add mini ai for the dealer (ex. to stop drawing when he has sum of 18)
       Add gambling mechanism and points system

"""

import random

def add_cards(nums):
    total = 0 
    aces = 0 
    for num in nums:
        if num == 11 :
            aces += 1
        else :
            total += num   
    total = total + 11*aces
    
    while total > 21 and aces > 0  :
        total -= 10
        aces -= 1
    
    return total
    

def deal_card():
    # infinite cards
    deck     = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(deck)
    return card

def winner(p, c):
    if c == 21:
        return "Computer"
    elif p > 21:
        return "Computer"
    elif p == 21 and c < 21:
        return "Player"
    elif p < 21 and c > p and c < 21:
        return "Computer"
    elif p < 21 and c < p:
        return "Player"
    elif c > 21 and p <= 21 :
        return "Player"
    elif c < 22 and p < 22 and c == p :
        return "None"

exitMes = "You successfully exited the game"
mes = "Do you want to Stand or Hit? s/h: "

ans = input("Do you want to play BlackJack? y/n: ")
if ans == "n":
    print(exitMes)
    exit()

user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(f"Your cards: {user_cards}")
print(f"Computer's card: [{computer_cards[0]}]")

keep_playing = True

while keep_playing :
    answer = input(mes)
    if answer == "h":
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        print(f"Your cards: {user_cards}")
        print(f"Computer's card: [{computer_cards[0]}]")
        if add_cards(user_cards) >= 21 :
            keep_playing = False
    elif answer == "s" :
        keep_playing = False

player_sum = add_cards(user_cards)
computer_sum = add_cards(computer_cards)

print(f"\nThe winner is The {winner(player_sum, computer_sum)}!!!")
print(f"\nYour cards: {user_cards} with the sum of: {player_sum} ")
print(f"\nComputer's card: {computer_cards} with the sum of: {computer_sum} \n")