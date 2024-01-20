def play_game():
    """Plays a single round of Rock, Paper, Scissors, Lizard, Spock against the computer."""
    
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ")

    while user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
        print("That choice doesn't work try again. Please choose from rock, paper, scissors, lizard, or spock.")
        user_choice = input("Enter your choice: ")

    computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif beats(user_choice, computer_choice):
        print("You win!")
    else:
        print("Computer wins!")

def beats(a, b):
    return ((a == "rock" and b in ["scissors", "lizard"]) or
            (a == "paper" and b in ["rock", "spock"]) or
            (a == "scissors" and b in ["paper", "lizard"]) or
            (a == "lizard" and b in ["paper", "spock"]) or
            (a == "spock" and b in ["rock", "scissors"]))


while True:
    play_game()
    play_again = input("Play again? (yes or no): ")
    if play_again != "yes":
        break
