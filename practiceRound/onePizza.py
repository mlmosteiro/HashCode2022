import fileReader
import fileWriter


def calculateFavoriteIngredients(likedIngredients, dislikedIngredients):
    selectedIngredients = [ingredient for ingredient in likedIngredients if ingredient not in dislikedIngredients]

    return selectedIngredients


def main():
    files = fileReader.loadInputFiles()

    for file in files:

        likedIngredients, dislikedIngredients = fileReader.parseInput(file)

        favoriteIngredients = calculateFavoriteIngredients(likedIngredients, dislikedIngredients)

        resultTxt = len(favoriteIngredients).__str__() + " " + " ".join(favoriteIngredients)

        fileWriter.writeResultFile(file, resultTxt)

main()