from random import choice


random_number = choice(range(1, 101))

guess = raw_input("Please guess a number between 1-100.")

guesses = []

while guess != random_number:
    if guess > 100:
        # tell the user that this number is out of range
        # ask for another guess
    elif guess < 0:
        # tell the user that this number is out of range
        # ask for another guess
    else:
        if guess in guesses:
            # tell the user that they've already guessed this
            # ask for another guess
        elif guess > random_number:
            # tell the user that the number is too high
            # add the number to guesses
            # ask for another guess
        elif guess < random_number:
            # tell the user that the number is too low
            # add the number to guesses
            # ask for another guess

print "You win! It took {} guesses".format(len(guesses))
