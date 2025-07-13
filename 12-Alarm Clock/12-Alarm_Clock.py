from playsound import playsound  # Import the playsound library to play audio files
import time  # Import the time module for time-related functions

# Escape sequences for clearing and resetting the terminal
CLEAR = "\033[2J"  # Clears the terminal screen
CLEAR_AND_RETURN = "\033[H"  # Moves the cursor back to the top-left corner of the screen

# Function to set an alarm after a specified number of seconds
def alarm(seconds):
    time_elapsed = 0  # Keep track of how many seconds have passed

    print(CLEAR)  # Clear the terminal screen before starting the countdown

    while time_elapsed < seconds:  # Loop until the specified time has passed
        time.sleep(1)  # Pause for 1 second
        time_elapsed += 1  # Increment the elapsed time by 1 second
        
        time_left = seconds - time_elapsed  # Calculate the remaining time
        minute_left = time_left // 60  # Convert remaining time to minutes
        seconds_left = time_left % 60  # Get the remaining seconds (after minutes)

        # Display the countdown in "MM:SS" format, updated on the same line
        print(f'{CLEAR_AND_RETURN}Alarm will sound in: {minute_left:02d}:{seconds_left:02d}')
        # ":02d" ensures the numbers are always shown with 2 digits, adding a leading 0 if needed

    playsound('alarm.mp3')  # Play the alarm sound when the countdown is over

# Get user input for minutes and seconds for the alarm
minutes = int(input("Minutes to wait: "))  # Get the number of minutes from the user
seconds = int(input("Seconds to wait: "))  # Get the number of seconds from the user
total_seconds = minutes * 60 + seconds  # Convert the total time to seconds

# Start the alarm with the total time
alarm(total_seconds)
