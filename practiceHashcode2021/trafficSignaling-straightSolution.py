import fileReader
import fileWriter
from outputDomain.OutputData import OutputData
from outputDomain.TrafficLightSchedule import TrafficLightSchedule

# problem in :
# https://storage.googleapis.com/coding-competitions.appspot.com/HC/2021/hashcode_2021_online_qualification_round.pdf
# 1. Read inputData
# 2. Write solution files
# 3. Build simple solution


def getStraightSolution(streets):
    trafficLightsAtTheEndOf = {}

    for street in streets:
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


def main():
    files = fileReader.loadInputFiles()

    for file in files:

        duration, numIntersections, numStreets, numCars, points, streets, carPaths = fileReader.parseInput(file)

        outputData = getStraightSolution(streets)

        fileWriter.writeResultFile("straightSolution", file, outputData.__str__())


main()
