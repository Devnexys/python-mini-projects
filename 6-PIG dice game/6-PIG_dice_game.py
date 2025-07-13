import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players dawg!\n")
    else:
        print("Invalid integer. Try again\n")

max_score = 20
player_scores = [0 for _ in range(players)]         # this way, all the initial values of list are set to 0

while max(player_scores) < max_score:

    for player_idx in range(players):
        
        if max(player_scores) >= max_score:
            break

        else:
            print('\nPlayer', player_idx + 1, "turn has just started!")
            print("Your total score is:", player_scores[player_idx], "\n\n")
            current_score = 0

            while True:

                should_roll = input("Would you like to roll (y)? ")
                if should_roll.lower() != 'y':
                    break

                value = roll()
                if value == 1:
                    print("\nYou rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a:", value)

                print("Your score is:", current_score)

            player_scores[player_idx] += current_score
            print("Your total score is:", player_scores[player_idx])
            print('-----------------------------------------------')

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nPlayer number", winning_idx + 1, 'is the winner with the score of:', max_score)