



```py import random

turns = ["rock","paper","scissors"]

human_turn = input("Enter rock, scissors or paper")
computer_turn = random.choice(turns)

if human_turn == computer_turn:
    print("It's a draw")
elif human_turn == "rock" and computer_turn == "scissors":
    print("Human wins!")
elif human_turn == "paper" and computer_turn == "rock":
    print("Human wins!")
elif human_turn == "scissors" and computer_turn == "paper":
    print("Human wins!")
else:
    print("Computer wins!")
```
