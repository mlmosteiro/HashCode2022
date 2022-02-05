import os
import glob


def loadInputFiles():
    path = 'practiceRound/input_data/'
    return glob.glob(os.path.join(os.getcwd(), path + "*.txt"))


def parseInput(file):
    with open(os.path.join(os.getcwd(), file), "r") as f:

        content = f.read()
        lines = content.split("\n")

        likedIngredientsCount = {}
        dislikedIngredientsCount = {}

        for i in range(1, len(lines)):
            line = lines[i]
            ingredients = line.split(" ")

            if (i % 2 == 1):  # odd lines are liked ingredients
                for ingredient in ingredients[1:]:
                    likedIngredientsCount[ingredient] = likedIngredientsCount.get(ingredient, 0) + 1
            elif (i % 2 == 0):  # even lines are disliked ingredients
                for ingredient in ingredients[1:]:
                    dislikedIngredientsCount[ingredient] = dislikedIngredientsCount.get(ingredient, 0) + 1

        return likedIngredientsCount, dislikedIngredientsCount
