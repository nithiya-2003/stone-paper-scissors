import random


op = ("rock", "paper", "scissors")

play = True 

while play:
    player = None
    computer = random.choice(op)

    while player not in op:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")

    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("You win!")

    else:
        print("You lose!")

    
    pa = input("Play again? (y/n): ").lower()
    
    
    if pa != "y":
        play = False

print("THANKS FOR PLAYING...")
