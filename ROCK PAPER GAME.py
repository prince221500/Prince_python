import random

user = input("Enter a choice (rock, paper, scissors): ")
possible = ["rock", "paper", "scissors"]
comp = random.choice(possible)
print()
print(f"You chose {user}, computer chose {comp}.")

if user == comp:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if comp == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if comp == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if comp == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")