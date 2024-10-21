print("\n*************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherComdition = random.choice(weatherForcast)
    return weatherComdition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nThe National Weather Service has updated our alarm by 45 minutes becuase"
              "of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45mph.")

vehicleResponseSystem()