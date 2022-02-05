import fileReader
import fileWriter


def calculateFavoriteIngredients(likedIngredients, dislikedIngredients):
    selectedIngredients = [
        ingredient for ingredient in likedIngredients if ingredient not in dislikedIngredients]

    return selectedIngredients


def pizzaHasLikedIngredients(ingredientsInPizza, likedIngredients):
    result = all(ingredients in ingredientsInPizza for ingredients in likedIngredients)
    # print ("pizzaHasLikedIngredients: " + result.__str__())
    return result


def pizzaHasAnyDislikedIngredients(ingredientsInPizza, dislikedIngredients):
    result = len(list(set(dislikedIngredients).intersection(ingredientsInPizza))) == 0
    # print("pizzaHasAnyDislikedIngredients: " + result.__str__())
    return result


def clientLikesPizza(ingredientsInPizza, likedIngredients, dislikedIngredients):
    # print("==========================")
    # print("ingredientsInPizza")
    # print(ingredientsInPizza)
    # print("likedIngredients")
    # print(likedIngredients)
    # print("dislikedIngredients")
    # print(dislikedIngredients)

    return pizzaHasLikedIngredients(ingredientsInPizza, likedIngredients) and pizzaHasAnyDislikedIngredients(ingredientsInPizza, dislikedIngredients)


def main():
    files = fileReader.loadInputFiles()

    for file in files:
        totalClients, likedIngredients, dislikedIngredients, clientsLikedIngredients, clientsDislikedIngredients = fileReader.parseInput(file)

        favoriteIngredients = calculateFavoriteIngredients(likedIngredients, dislikedIngredients)

        points = 0
        for i in range(0, int(totalClients)):
            if clientLikesPizza(favoriteIngredients, clientsLikedIngredients[i], clientsDislikedIngredients[i]):
                points += 1

        print(file + ": " + points.__str__())
        resultTxt = len(favoriteIngredients).__str__() + " " + " ".join(favoriteIngredients)
        fileWriter.writeResultFile(file, resultTxt)


main()
