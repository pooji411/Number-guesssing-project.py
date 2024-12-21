
import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Initialize the number of tries
    tries = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Ask the user for their guess
        user_guess = input("Take a guess: ")

        # Check if the user wants to quit
        if user_guess.lower() == "quit":
            print("Okay, the number was {}.".format(number_to_guess))
            break

        # Try to convert the user's guess to an integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("That's not a valid number!")
            continue

        # Increment the number of tries
        tries += 1

        # Check if the user's guess is correct
        if user_guess == number_to_guess:
            print("Congratulations! You found the number in {} tries.".format(tries))
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


if __name__ == "__main__":
    number_guessing_game()

