import sys  # Imports the sys module for system-specific parameters and functions
import time  # Imports the time module to use the sleep function for delays

# Prints a welcome message to the console
print("\nWelcome to InfoTechCenter V1.0""\n")

# Initialize variables
x = 0  # This variable keeps track of the loop iterations (up to 20)
ellipsis = 0  # This controls the number of dots displayed after the message

# A while loop that will run 20 times
while x != 20:
    x += 1  # Increment x by 1 with each iteration
    # Create the message that gets updated each loop iteration
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Add one dot (.) to the message each time
    sys.stdout.write("\r" + message)  # Overwrite the current line in the console with the new message
    time.sleep(.5)  # Wait for half a second before the next iteration

    # Reset the ellipsis back to 0 after it reaches 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # When x reaches 20, print the system boot complete message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
