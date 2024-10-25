import sys  # Imports the sys module for system-specific parameters and functions
import time  # Imports the time module to use the sleep function for delays
import random
from time import sleep

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

timeToSleep = 2 #variable to set the time libary to 2 seconds when called
time.sleep(timeToSleep) # Calling the time to sleep libary with the varible TimeToSleep value

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
    time.sleep(1)  # Wait for half a second before the next iteration

    # Reset the ellipsis back to 0 after it reaches 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # When x reaches 20, print the system boot complete message in green
    if x == 20:
        print(f"\n\n{colors['green']}Operating System Booted Up - Retina Scanned - Access Granted{colors['reset']}")


print("\n*************************************\n")

print("Weather Branch\n")

# Import necessary libraries
import random
from time import sleep

# Define the weather function to randomly choose a weather condition
def weather():
    # List of possible weather conditions
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    # Randomly select a condition from the list
    return random.choice(weatherForcast)

# Store the random weather condition
weatherAlert = weather()

# Define a dictionary mapping weather conditions to alarm delays and speed limits
weather_conditions = {
    "snowy": {"delay": 30, "speed_limit": 55},
    "blizzard": {"delay": 45, "speed_limit": 45},
    "rainy": {"delay": 15, "speed_limit": 65},
    "windy": {"delay": 5, "speed_limit": 70},
    "icy": {"delay": 50, "speed_limit": 30}
}

# Define the vehicle response system based on weather conditions
def vehicleResponseSystem():
    # Check if the weather condition exists in the weather_conditions dictionary
    if weatherAlert in weather_conditions:
        condition = weather_conditions[weatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {condition['delay']} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)  # Pause for 1 second to simulate processing
        print(f"\nVRS system has been engaged only allowing you to drive {condition['speed_limit']}mph.")
    else:
        # Default case for sunny or other weather conditions
        print(f"The NWS is calling for {weatherAlert} skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")

vehicleResponseSystem()

print("\n*************************************\n")
print("Gasoline Branch\n")

# Constants for gas levels and gas stations
GAS_LEVELS = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
GAS_STATIONS = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]

# Function to randomly return a gas level
def get_gas_level():
    return random.choice(GAS_LEVELS)

# Function to randomly return a gas station
def get_gas_station():
    return random.choice(GAS_STATIONS)

# Function to alert user based on gas level and simulate nearest gas station
def gas_level_alert():
    gas_level = get_gas_level()  # Get the current gas level
    station = get_gas_station()  # Get the closest gas station

    # Use dictionary to map gas levels to their corresponding actions
    level_actions = {
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
        "Low": f"Your gas tank is extremely low, checking GPS for the closest gas station.\n"
               f"The closest gas station is {station}, which is {round(random.uniform(1, 25), 1)} miles away.",
        "Quarter Tank": f"Your gas tank is on a quarter of a tank, checking GPS for the closest gas station.\n"
                        f"The closest gas station is {station}, which is {round(random.uniform(25.1, 50), 1)} miles away.",
        "Half Tank": "Your gas tank is half full, which is plenty to get to your destination.",
        "Three Quarter Tank": "Your gas tank is three-quarters full.",
        "Full Tank": "Your gas tank is full!!! Vroom Vroom"
    }

    # Print the message based on the current gas level
    print(level_actions[gas_level])
    sleep(2)  # Add a delay between actions

# Call the gas level alert function
gas_level_alert()
