print("\n*************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForcast = ["snowing", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherComdition = random.choice(weatherForcast)
    return weatherComdition

print(weather())