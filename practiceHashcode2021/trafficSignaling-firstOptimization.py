import fileReader
import fileWriter
from outputDomain.OutputData import OutputData
from outputDomain.TrafficLightSchedule import TrafficLightSchedule

# problem in :
# https://storage.googleapis.com/coding-competitions.appspot.com/HC/2021/hashcode_2021_online_qualification_round.pdf


def calculateFavoriteIngredients(likedIngredients, dislikedIngredients):
    selectedIngredients = [
        ingredient for ingredient in likedIngredients if ingredient not in dislikedIngredients]

    return selectedIngredients


def getStraightSolution(carPaths, streets):
    trafficLightsAtTheEndOf = {}

    for street in streets:
        for carPath in carPaths:
            if street.name in carPath.streets:
                if street not in trafficLightsAtTheEndOf:
                    trafficLightsAtTheEndOf[street] = 1
                else:
                    trafficLightsAtTheEndOf[street] += 1

    return buildOutputData(trafficLightsAtTheEndOf)


def buildOutputData(trafficLights):
    outputData = OutputData()

    for street in trafficLights:
        intersection = street.end
        schedule = TrafficLightSchedule(street.name, trafficLights[street])
        outputData.addTrafficLightSchedule(intersection, schedule)

    return outputData


def getUsedStreets(carPaths, streets):
    allStreets = []

    for street in streets:
        for carPath in carPaths:
            if street.name in carPath.streets:
                allStreets.append(street)

    return list(set(allStreets))


def main():
    files = fileReader.loadInputFiles()

    for file in files:

        duration, numIntersections, numStreets, numCars, points, streets, carPaths = fileReader.parseInput(file)

        usedStreets = getUsedStreets(carPaths, streets)
        outputData = getStraightSolution(carPaths, usedStreets)

        fileWriter.writeResultFile("firstOptimization", file, outputData.__str__())


main()
