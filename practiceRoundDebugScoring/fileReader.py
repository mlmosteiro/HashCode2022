import os
import glob


def loadInputFiles():
    path = 'practiceRoundDebugScoring/input_data/'
    return glob.glob(os.path.join(os.getcwd(), path + "*.txt"))


def parseInput(file):
    with open(os.path.join(os.getcwd(), file), "r") as f:

        content = f.read()
        lines = content.split("\n")

        likedIngredientsCount = {}
        dislikedIngredientsCount = {}

        clientsLikedIngredients = []
        clientsDislikedIngredients = []

        totalClients = lines[0]

        for i in range(1, len(lines)):
            if (i % 2 == 1):
                line = lines[i]
                ingredients = line.split(" ")
                clientsLikedIngredients.append(ingredients[1:])
                for ingredient in ingredients[1:]:
                    likedIngredientsCount[ingredient] = likedIngredientsCount.get(
                        ingredient, 0) + 1
            elif (i % 2 == 0):
                line = lines[i]
                ingredients = line.split(" ")
                clientsDislikedIngredients.append(ingredients[1:])
                for ingredient in ingredients[1:]:
                    dislikedIngredientsCount[ingredient] = dislikedIngredientsCount.get(
                        ingredient, 0) + 1

        return totalClients, likedIngredientsCount, dislikedIngredientsCount, clientsLikedIngredients, clientsDislikedIngredients
