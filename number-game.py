"""Simple number guessing game with recursion."""

from random import randint


def number_game(raw_guess, random_number, guesses):

    while True:
        try:
            guess = int(raw_guess)
            break

        except ValueError:
            raw_guess = raw_input("This is not a number. Please guess a number between 1-100: ")
            number_game(raw_guess, random_number, guesses)

    # base case
    if guess == random_number:
        print "You win! It took {} guesses".format((len(guesses)+1))

        play_again = raw_input("Would you like to play again? Y/N: ")

        if play_again.upper() == "Y" or "YES":
            raw_guess = raw_input("Please guess a number between 1-100: ")

            new_random_number = int(randint(1, 100))

            new_guesses = []

            number_game(raw_guess, new_random_number, new_guesses)

        elif play_again.upper() == "N" or "NO":
            print "Thank you for playing!"
            # currently not hitting this line
        else:
            print "I'm not sure what you're trying to tell me."
            # somehow ask Y/N again

    else:

        if guess > 100:
            raw_guess = raw_input("This guess is out of range. Please guess a number between 1-100: * ")
            print random_number
            number_game(raw_guess, random_number, guesses)
        elif guess < 1:
            raw_guess = raw_input("This guess is out of range. Please guess a number between 1-100: ** ")
            print random_number
            number_game(raw_guess, random_number, guesses)
        else:
            if guess in guesses:
                raw_guess = raw_input("You have already guessed this number. Please guess another number between 1-100: ")
                print random_number
                print guesses
                number_game(raw_guess, random_number, guesses)
            elif guess > random_number:
                guesses.append(guess)
                print guesses
                raw_guess = raw_input("Your guess is too high. Please guess another number between 1-100: ")
                print random_number
                number_game(raw_guess, random_number, guesses)
            elif guess < random_number:
                guesses.append(guess)
                print guesses
                raw_guess = raw_input("Your guess is too low. Please guess another number between 1-100: ")
                print random_number
                number_game(raw_guess, random_number, guesses)

raw_guess = raw_input("Please guess a number between 1-100: ")

random_number = int(randint(1, 100))

guesses = []

number_game(raw_guess, random_number, guesses)
