import fileReader
import fileWriter


def calculateFavoriteIngredients(likedIngredients, dislikedIngredients):
    selectedIngredients = [
        ingredient for ingredient in likedIngredients if ingredient not in dislikedIngredients]

    return selectedIngredients


def pizzaHasAtLeastOneLikedIngredient(likedIngredientInPizza):
    return len(likedIngredientInPizza) > 0


def pizzaHasEnoughLikedIngredients(likedIngredientInPizza, generalLikedIngredients):
    return len(generalLikedIngredients) - 1 <= len(likedIngredientInPizza) <= len(generalLikedIngredients) + 1


def pizzaHasAcceptableDislikedIngredients(dislikedIngredientsInPizza, generalDislikedIngredientsInPizza):
    return len(generalDislikedIngredientsInPizza) - 1 <= len(dislikedIngredientsInPizza) <= len(generalDislikedIngredientsInPizza) + 1


def clientLikesPizza(selectedIngredients, likedIngredients, dislikedIngredients):
    likedIngredientsInPizza = list(set(likedIngredients).intersection(selectedIngredients))
    dislikedIngredientsInPizza = list(set(dislikedIngredients).intersection(selectedIngredients))

    # print("==========================")
    # print("selectedIngredients")
    # print(selectedIngredients)
    # print("likedIngredients")
    # print(likedIngredients)
    # print("dislikedIngredients")
    # print(dislikedIngredients)
    # print("likedIngredientInPizza")
    # print(likedIngredientsInPizza)
    # print("dislikedIngredientsInPizza")
    # print(dislikedIngredientsInPizza)

    return pizzaHasAtLeastOneLikedIngredient(likedIngredientsInPizza) \
        and pizzaHasEnoughLikedIngredients(likedIngredientsInPizza, likedIngredients)\
        and pizzaHasAcceptableDislikedIngredients(dislikedIngredientsInPizza, dislikedIngredients)



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
