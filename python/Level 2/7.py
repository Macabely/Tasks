import random
num1 = 1
num2 = 100
guesses = 0
test = True 
best = random.randint(num1, num2)
print("Number guessing game")
print("Choose a number between 1 and 100")

while test:
    guess = input("Please enter your guessing number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < num1 or guess > num2:
            print("The number is out of range")
            print("Please choose a number between 1 and 100")
        elif guess < best:
            print("Too low, try agnin")
        elif guess > best:
            print("Too high, try again")
        else:
            print(f"correct the {best} is the right answer")
            print(f"You did {guesses} guesses")
            test = False
    else:
        print("Invalid! Please choose a number between 1 and 100")