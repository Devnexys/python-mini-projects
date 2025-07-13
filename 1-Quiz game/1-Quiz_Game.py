print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

# if playing not in ["Yes", "YES", "yes", "Y", "y"]:
if playing.lower() not in ["yes", "y"]:
    quit()

print("Okay! Let's play :)\n")


score = 0

answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("4. What does MSEB stand for? ")
if answer.lower() == "maharashtra state electrical board":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("5. What does BJT stand for? ")
if answer.lower() == "bipolar junction transistor":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

print("Results: \nYou got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")