import random
from time import sleep

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

# Print header for better output readability
print("\n******************************\n")
print("Gasoline Branch")

# Call the gas level alert function
gas_level_alert()


