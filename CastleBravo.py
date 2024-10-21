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