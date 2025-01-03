import random

RPC = ["Rock", "Paper", "Scissors"]

computer = random.choice(RPC)

user = input(
    """
"Choose your type!"
Rock, Paper, Scissors
Your choose: """
)

if user not in RPC:
    print("you didn't choose right thing!")
else:
    print("Computer choose: " + computer)

    if user == computer:
        print("draw")
    elif (
        (user == "Rock" and computer == "Paper")
        or (user == "Paper" and computer == "Scissors")
        or (user == "Scissors" and computer == "Rock")
    ):
        print("you lose...")
    else:
        print("you win!")
