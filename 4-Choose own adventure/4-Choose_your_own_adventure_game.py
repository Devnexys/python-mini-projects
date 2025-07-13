name = input("Type your name: ")
print("\nWelcome", name, "to this adventure!\n")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left':
    answer = input("You came to a river, you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()
    
    if answer == 'walk':
        print("\nYou walked for many miles, ran out of water and you lost the game.")
    elif answer == 'swim':
        print("\nYou swam across and were eaten by an alligator.")
    else:
        print("\nNot a valid option. You lose!")    

elif answer == 'right':
    answer = input("You came to a bridge. It looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()

    if answer == 'cross':
        answer = input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == 'yes':
            print("\nYou talked to the stanger and they give you gold. You WIN!")
        elif answer == 'no':
            print("\nYou ignored the stranger and they are offended and you lose!")
        else:
            print("\nNot a valid option. You lose!")

    elif answer == 'back':
        print("\nYou go back & lose")
    else:
        print("\nNot a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print("\nThank you for playing", name)