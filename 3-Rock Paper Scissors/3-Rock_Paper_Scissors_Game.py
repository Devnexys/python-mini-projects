import random

print("Lets play Rock-Paper-Scissors Game")

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]
no_of_games = 0

while True:

    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Please enter valid input")
        continue

    no_of_games += 1

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("You picked:", user_input)
    print("Computer picked:", computer_pick)


    if user_input == 'rock' and computer_pick == 'scissors':
        print("You Won!")
        user_wins += 1

    elif user_input == 'rock' and computer_pick == 'paper':
        print("You Lost!")
        computer_wins += 1

    elif user_input == 'rock' and computer_pick == 'rock':
        print("Draw!")
        draws += 1


    if user_input == 'paper' and computer_pick == 'scissors':
        print("You Lost!")
        computer_wins += 1

    elif user_input == 'paper' and computer_pick == 'paper':
        print("Draw!")
        draws += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print("You Won!")
        user_wins += 1


    if user_input == 'scissors' and computer_pick == 'scissors':
        print("Draw!")
        draws += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You Won!")
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'rock':
        print("You Lost!")
        computer_wins += 1

print("\nResults:\nTotal number of games played:", no_of_games)
print("Total games you won:", user_wins)
print("Total games computer won:", computer_wins)
print("Draws:", draws)
print("GoodBye")