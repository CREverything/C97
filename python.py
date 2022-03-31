import random
print("You shall play a number guessing game. 5 wrong chances and we obliterate your planet. The fate of your species depends on your choice.")
array = [1, 2, 3, 4, 5, 6]
answer = random.choice(array)
chances = "5"
calcChances = 5
number = int(input("\nGuess a number between 1 and 9"))

while(calcChances>0):
    number = int(input("\nGuess a number between 1 and 9"))
    if(number == answer):
        print("\nCongratulations! You have saved the planet!")

    elif(number > answer):
       print("\nYour guess was too high. You only have "+str(calcChances)+" remaining.")
       calcChances = int(chances) - 1

    else:
       print("\nYour guess was too low. You only have "+str(calcChances)+" remaining.")
       calcChances = int(chances) - 1

    if(0 >= int(calcChances)):
       print("\nYou have caused the destruction of your planet.")
