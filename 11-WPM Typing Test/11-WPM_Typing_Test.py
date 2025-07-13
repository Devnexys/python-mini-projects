
import curses  # Module for creating text-based User Interfaces
from curses import wrapper  # A helper function to simplify the curses setup
import time  # Module for tracking time (used to calculate WPM)
import random  # Module for generating random numbers (used to select text)

# Function to display the starting screen
def start_screen(stdscr):
    stdscr.clear()  # Clear the screen
    stdscr.addstr('Welcome to the Speed Typing Test!')  # Display a welcome message
    stdscr.addstr('\nPress any key to begin!')  # Prompt user to press any key
    stdscr.refresh()  # Refresh the screen to show changes
    stdscr.getkey()  # Wait for the user to press a key

# Function to display the target text, current typed text, and WPM
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)  # Display the target text (the one to type)
    stdscr.addstr(1, 0, f'WPM: {wpm}')  # Display the current Words Per Minute (WPM)

    # Loop through the current text typed by the user
    for i, char in enumerate(current):
        correct_char = target[i]  # Get the correct character from the target text
        color = curses.color_pair(1)  # Default color for correct characters (green)

        if char != correct_char:  # If the character is incorrect
            color = curses.color_pair(2)  # Use the red color for errors

        # Display the character with the appropriate color
        stdscr.addstr(0, i, char, color)    

# Function to load random text from a file
def load_text():
    with open('test.txt', 'r') as f:  # Open the file containing text
        lines = f.readlines()  # Read all lines in the file
        return random.choice(lines).strip()  # Pick a random line and remove extra spaces

# Main typing test function
def wpm_test(stdscr):
    target_text = load_text()  # Load a random text for the test
    current_text = []  # Initialize the list for the user’s typed characters
    wpm = 0  # Initialize Words Per Minute
    start_time = time.time()  # Record the start time
    stdscr.nodelay(True)  # Allow non-blocking input (doesn't wait for keypress)

    while True:
        # Calculate the time elapsed and update WPM
        time_elapsed = max(time.time() - start_time, 1)  # Avoid division by zero
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)  # WPM formula

        stdscr.clear()  # Clear the screen
        display_text(stdscr, target_text, current_text, wpm)  # Update the displayed text and WPM
        stdscr.refresh()  # Refresh the screen to show updates

        # Check if the user has completed typing the target text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)  # Re-enable blocking input
            break  # End the loop if the text is complete

        try:
            key = stdscr.getkey()  # Get the user input
        except:
            continue  # If no input, continue the loop

        if ord(key) == 27:  # 27 is the ASCII value for the ESCAPE key
            break  # Exit the test if ESCAPE is pressed

        # Handle backspace input
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):  # Different backspace key codes
            if len(current_text) > 0:
                current_text.pop()  # Remove the last character typed

        # Add the typed key to the current text (if within target text length)
        elif len(current_text) < len(target_text):
            current_text.append(key)

# Main function for the application
def main(stdscr):  # `stdscr` is the Standard Screen provided by curses
    # Initialize color pairs for text display
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green for correct input
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red for incorrect input
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # White for default text

    start_screen(stdscr)  # Show the start screen

    while True:
        wpm_test(stdscr)  # Run the typing test

        # Display completion message and wait for user action
        stdscr.addstr(2, 0, 'You completed the text! Press any key to continue...  (Esc to Exit)')
        key = stdscr.getkey()  # Wait for a keypress

        if ord(key) == 27:  # If ESCAPE key is pressed, exit the program
            break

# Wrapper function to handle curses setup and teardown
wrapper(main)




# MY CODE
'''
import curses

from curses import wrapper

import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')
    stdscr.addstr('\nPress any key to begin!')
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f'WPM: {wpm}')

        for i, char in enumerate(current):
            correct_char = target[i]
            color = curses.color_pair(1)

            if char != correct_char:
                color = curses.color_pair(2)

            stdscr.addstr(0, i, char, color)    

def load_text():
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)

        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:          # ASCII value for 'ESCAPE' Button is 27
            break
        if key in ('KEY_BACKSPACE', '\b', 'x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):       # stdscr - Standard Screen

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2, 0, 'You completed the text! Press any key to continue...  (Esc to Exit)')
        key = stdscr.getkey()
        if ord(key) == 27:
            break

    
    # # stdscr.clear()

    # # stdscr.addstr("Hello World!")
    # stdscr.addstr("Hello World!", curses.color_pair(2))
    
    # # stdscr.addstr(1, 4, "Hello World!")
    # # stdscr.addstr(1, 0, "Hello World!")

    # stdscr.refresh()
    # key = stdscr.getkey()
    # print(key)


wrapper(main)
'''