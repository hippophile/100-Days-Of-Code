""" 
The classic Number Guessing game in CLI
"""

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

dif = input("Choose a difficulty. Type 'easy' or 'hard': ")


if dif == "easy" :
    attemps = 10
elif dif == 'hard' :
    attemps = 5

print(f"You have {attemps} attemps remaining to guess the number")

guess = "Make a guess: "
my_num = 67

playing = True
while playing == True :
    ans = input(guess)
    if int(ans) == my_num :
        print("Yes, You found it, You won!!!")
        playing = False
    elif int(ans) > my_num :
        attemps -= 1
        print("Too high")
        print("Guess again")
        print(f"You have {attemps} attemps remaining to guess the number")
    elif int(ans) < my_num :
        attemps -= 1
        print("Too low")
        print("Guess again")
        print(f"You have {attemps} attemps remaining to guess the number")
