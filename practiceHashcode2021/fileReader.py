import os
import glob
from inputDomain.CarPath import CarPath
from inputDomain.Street import Street


def loadInputFiles():
    path = 'practiceHashcode2021/input_data/'
    list_of_files = glob.glob(os.path.join(os.getcwd(), path + "*.txt"))
    return sorted( list_of_files, key =  lambda x: os.stat(os.path.join(path, x)).st_size)


def getLines(file):
    with open(os.path.join(os.getcwd(), file), "r") as f:
        content = f.read()
        lines = content.split("\n")
        return list(filter(None, lines))


def parseStreets(lines):
    streetList = []

    for index in range(len(lines)):
        streetList.append(Street(lines[index].split(" ")))

    return streetList


def parseCarPaths(lines):
    carPaths = []

    for index in range(len(lines)):
        carPaths.append(CarPath(lines[index].split(" ")[1:]))

    return carPaths


def parseInput(file):
    lines = getLines(file)

    duration, numIntersections, numStreets, numCars, points = lines[0].split(
        " ")
    streets = parseStreets(lines[1:int(numStreets)+1])
    carPaths = parseCarPaths(lines[int(numStreets)+1:])

    return duration, numIntersections, numStreets, numCars, points, streets, carPaths


""" 
    print('streets')
    print(streets)

    print('cars')
    print(carPaths)

    print ('duration: ' + duration 
    + '\n numIntersections: ' + numIntersections 
    + '\n numStreets: ' + numStreets
    + '\n numCars: ' + numCars 
    + '\n points: ' + points )
"""

# paintMap(streets)
