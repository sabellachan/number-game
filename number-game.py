"""Simple number guessing game."""

from random import choice


random_number = int(choice(range(1, 101)))

raw_guess = raw_input("Please guess a number between 1-100: ")

guesses = []

try:
    guess = int(raw_guess)

    while guess != random_number:

        if guess > 100:
            print "This guess is out of range."
            guess = raw_input("Please guess a number between 1-100: ")
        elif guess < 0:
            print "This guess is out of range."
            guess = raw_input("Please guess a number between 1-100: ")
        else:
            if guess in guesses:
                print "You have already guessed this number."
                guess = raw_input("Please guess another number between 1-100: ")
            elif guess > random_number:
                print "Your guess is too high."
                guesses.append(guess)
                guess = raw_input("Please guess another number between 1-100: ")
            elif guess < random_number:
                print "Your guess is too low."
                guesses.append(guess)
                guess = raw_input("Please guess another number between 1-100: ")

    print "You win! It took {} guesses".format(len(guesses))

except ValueError:
    print "This is not a number."
    raw_guess = raw_input("Please guess a number between 1-100.")
