"""Simple number guessing game with recursion."""

from random import randint


def number_game(raw_guess, random_number):

    guesses = []

    while True:
        try:
            guess = int(raw_guess)
            break

        except ValueError:
            print "This is not a number."

    # base case
    if raw_guess == random_number:
        print "You win! It took {} guesses".format(len(guesses))

    else:

        if guess > 100:
            raw_guess = raw_input("This guess is out of range. Please guess a number between 1-100: * ")
            print random_number
            number_game(raw_guess, random_number)
        elif guess < 0:
            raw_guess = raw_input("This guess is out of range. Please guess a number between 1-100: ** ")
            print random_number
            number_game(raw_guess, random_number)
        else:
            if guess in guesses:
                # print guesses
                raw_guess = raw_input("You have already guessed this number. Please guess another number between 1-100: ")
                print random_number
                number_game(raw_guess, random_number)
            elif guess > random_number:
                guesses.append(guess)
                raw_guess = raw_input("Your guess is too high. Please guess another number between 1-100: ")
                print random_number
                number_game(raw_guess, random_number)
            elif guess < random_number:
                guesses.append(guess)
                raw_guess = raw_input("Your guess is too low. Please guess another number between 1-100: ")
                print random_number
                number_game(raw_guess, random_number)

    # print "You win! It took {} guesses".format(len(guesses))

raw_guess = raw_input("Please guess a number between 1-100: ")

random_number = int(randint(1, 100))

number_game(raw_guess, random_number)
