import os

RESULTS_PATH = "practiceRound/results"


def writeResultFile(filePath, message):
    createResultsDirectory()

    fileName = filePath.split("/")[-1].split(".")[0]

    resultFile = open(os.path.join(os.getcwd(), RESULTS_PATH + "/result_" + fileName + ".txt"), "w")
    resultFile.write(message)
    resultFile.close()


def createResultsDirectory():
    path = os.path.join(os.getcwd(), RESULTS_PATH)
    if not os.path.exists(path):
        os.makedirs(path)
