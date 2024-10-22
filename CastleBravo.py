# Print header for better output readability
print("\n******************************\n")
print("Gasoline Branch")

# Importing necessary modules
import random  # Used to randomly select items from lists
from time import sleep  # Used to add delay between outputs


# Function to randomly return a gas level from a list
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)  # Randomly select a gas level


# Function to randomly return a gas station from a list
def gasStations():
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)  # Randomly select a gas station


# Function to alert user based on gas level and simulate checking for the nearest gas station
def gasLevelAlert():
    # Generate random distances to gas stations depending on gas level
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Random distance when gas is low
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)  # Random distance when at quarter tank

    gasLevelIndicator = gasLevelGauge()  # Get the current gas level

    # Check the gas level and provide appropriate messages
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Pause for 2 seconds before the next message
        print("Calling Triple AAA")  # Indicate assistance is being called
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)
        # Display closest gas station and distance for low fuel
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(2)
        # Display closest gas station and distance for quarter tank
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        # Message for half tank level, reassuring user
        print("Your gas tank is half full, which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        # Message for three-quarter tank level
        print("Your gas tank is three-quarters full.")
    else:
        # Message for a full tank
        print("Your gas tank is full!!! Vroom Vroom")


# Call the gas level alert function to simulate the process
gasLevelAlert()
