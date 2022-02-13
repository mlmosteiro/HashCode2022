import os

RESULTS_PATH = "practiceHashcode2021/results"


def writeResultFile(invokator, filePath, message):
    createResultsDirectory(invokator)

    fileName = filePath.split("/")[-1].split(".")[0]

    resultFile = open(os.path.join(os.getcwd(), RESULTS_PATH + "/" + invokator + "/result_" + fileName + ".txt"), "w")
    resultFile.write(message)
    resultFile.close()


def createResultsDirectory(invokator):
    path = os.path.join(os.getcwd(), RESULTS_PATH + "/" + invokator)
    if not os.path.exists(path):
        os.makedirs(path)
