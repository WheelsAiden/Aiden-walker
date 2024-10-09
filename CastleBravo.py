import sys  # Imports the sys module for system-specific parameters and functions
import time  # Imports the time module to use the sleep function for delays

# ANSI escape sequences for text colors
colors = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "cyan": "\033[36m"
}

# Prints a welcome message in blue to the console
print(f"{colors['blue']}\nWelcome to InfoTechCenter V1.0\n{colors['reset']}")

# Initialize variables
x = 0  # This variable keeps track of the loop iterations (up to 20)
ellipsis = 0  # This controls the number of dots displayed after the message

# A while loop that will run 20 times
while x != 20:
    x += 1  # Increment x by 1 with each iteration

    # Cycle through colors for each iteration
    color = colors[list(colors.keys())[x % 4 + 1]]  # Changes between red, green, yellow, and blue

    # Create the message that gets updated each loop iteration
    message = (f"{color}Infotech Center System Booting" + "." * ellipsis + colors["reset"])
    ellipsis += 1  # Add one dot (.) to the message each time
    sys.stdout.write("\r" + message)  # Overwrite the current line in the console with the new message
    time.sleep(.5)  # Wait for half a second before the next iteration

    # Reset the ellipsis back to 0 after it reaches 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # When x reaches 20, print the system boot complete message in green
    if x == 20:
        print(f"\n\n{colors['green']}Operating System Booted Up - Retina Scanned - Access Granted{colors['reset']}")

