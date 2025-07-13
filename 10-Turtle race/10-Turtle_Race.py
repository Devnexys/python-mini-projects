import turtle  # Module for drawing graphics and controlling turtles
import time  # Module for adding delays in the program
import random  # Module for generating random numbers

# Set the width and height of the racing screen
WIDTH, HEIGHT = 500, 500

# List of colors for the turtles
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

# Initialize the turtle screen
def init_turtle():
    screen = turtle.Screen()  # Create a turtle screen object
    screen.title('Turtle Racing!')  # Set the window title
    screen.setup(WIDTH, HEIGHT)  # Set up the window dimensions

# Function to get the number of racers from the user
def get_number_of_racers():
    racers = 0  # Initialize racers to 0
    while True:  # Keep asking until a valid input is provided
        racers = input('Enter the number of racers (2 - 10): ')  # Take input from the user
        if racers.isdigit():  # Check if the input is a number
            racers = int(racers)  # Convert the input to an integer
        else:
            print('Input is not numeric...  Try Again!')  # Error message for non-numeric input
            continue  # Skip the rest of the loop and restart

        if 2 <= racers <= 10:  # Check if the number is within the valid range
            return racers  # Return the valid number of racers
        else:
            print('Number not in range 2-10. Try Again!')  # Error message for invalid range

# Function to create turtles for the race
def create_turtles(colors):
    turtles = []  # List to hold all the turtle objects

    # Calculate the horizontal spacing between turtles
    spacingx = WIDTH // (len(colors) + 1)

    # Create turtles and set their starting positions
    for i, color in enumerate(colors):  # Loop through each color and its index
        racer = turtle.Turtle()  # Create a new turtle
        racer.color(color)  # Set the turtle's color
        racer.shape('turtle')  # Set the shape to a turtle
        racer.left(90)  # Rotate the turtle to face upward
        racer.penup()  # Lift the pen to avoid drawing while moving
        # Set the turtle's starting position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()  # Put the pen down to prepare for movement

        turtles.append(racer)  # Add the turtle to the list
    return turtles  # Return the list of turtles

# Function to run the race
def race(colors):
    turtles = create_turtles(colors)  # Create the turtles using the provided colors

    while True:  # Keep running until a turtle wins
        for racer in turtles:  # Loop through each turtle
            # Generate a random distance for the turtle to move
            distance = random.randrange(1, 20)
            racer.forward(distance)  # Move the turtle forward by the random distance

            # Get the turtle's current position
            x, y = racer.pos()
            # Check if the turtle has crossed the finish line
            if y >= HEIGHT // 2 - 10:
                # Return the color of the winning turtle
                return colors[turtles.index(racer)]

# Get the number of racers from the user
racers = get_number_of_racers()
print(racers)  # Print the number of racers

init_turtle()  # Initialize the turtle screen

# Shuffle the colors randomly and select colors for the racers
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)  # Print the selected colors

# Start the race and get the winner's color
winner = race(colors)
print('The winner is the turtle with color:', winner)  # Print the winner's color

time.sleep(5)  # Pause the program for 5 seconds to allow the user to see the result




# MY CODE
'''
import turtle

import time

import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def init_turtle():
    screen = turtle.Screen()
    screen.title('Turtle Racing!')
    screen.setup(WIDTH, HEIGHT)


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric...  Try Again!')
            continue    # it skips the next part of the code, and goes to beginning of loop (meaning next iteration)

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')


def create_turtles(colors):
    turtles = []

    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # Set position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)

        racer.pendown()

        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

        
racers = get_number_of_racers()
print(racers)

init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)

winner = race(colors)
print('The winner is the turtle with color:', winner)

time.sleep(5)
'''

'''
Examples of attributes of Python Turtle
racer = turtle.Turtle()

racer.shape('turtle')

racer.penup()

racer.speed(1)

racer.color('blue')

racer.forward(100)
racer.left(90)
racer.right(45)
racer.pendown()

racer.forward(100)
racer.left(45)
racer.backward(100)

time.sleep(5)
'''