import random
randomNumber = random.randrange(0,10)
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Enter the number "))
    if userInput==randomNumber:
        guessed = True
        print("perfect")
    elif userInput>10:
        print("Our guess range is between 0 and 10, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 10, please try a bit higher")
    elif userInput>randomNumber:
        print("ur answer is higher")
    elif userInput < randomNumber:
        print("ur answer is lower")

print("End of program")