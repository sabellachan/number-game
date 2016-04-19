from random import choice


random_number = choice(range(1, 101))

guess = raw_input("Please guess a number between 1-100.")

while guess != random_number:
    if guess > 100:
        