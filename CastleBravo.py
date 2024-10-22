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

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"Which is",milesToGasStationLow,",miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is", gasStations(), "Which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("your gas tank is a half a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarter tanks full.")
    else:
        print("Your gas tank is full!!! Vroom Vroom")

gasLevelAlert()