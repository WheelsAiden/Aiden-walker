print("\n******************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)

print(gasLevelGauge())
print(gasStations())

#def gasLevelAlert