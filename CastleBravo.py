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
    weatherComdition = random.choice(weatherForcast)
    return weatherComdition


# Store the random weather condition
weatherAlert = weather()


# Define the vehicle response system based on weather conditions
def vehicleResponseSystem():
    # Check for snowy weather
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Pause for 1 second to simulate processing
        print("\nVRS system has been engaged only allowing you to drive 55mph.")

    # Check for blizzard weather
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45mph.")

    # Check for rainy weather
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")

    # Check for windy weather
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 70mph.")

    # Check for icy weather
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 30mph.")

    # Default case for sunny or other weather conditions
    else:
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")


vehicleResponseSystem()