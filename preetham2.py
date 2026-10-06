import random

secret_number = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"You got it in {attempts} guesses!")
        break
