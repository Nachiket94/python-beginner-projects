import random

# define upper and lower bound for game
smaller_number = 1
larger_number = 10
upper_limit = 10
lower_limit = 1
num_of_guesses=0


# function to prompt user for input. will continue to ask user for proper int if invalid num passed
def enter_and_verification(lower_limit, upper_limit):
    user_guess = int(input(f"\nEnter number between {lower_limit} to {upper_limit}: "))
    while user_guess > upper_limit or user_guess < lower_limit:
        if user_guess > upper_limit:
            user_guess = int(
                input(
                    f"\nYour guess exceeds the upper range. Lower your guess and try again.\nEnter number between {lower_limit} to {upper_limit}: "
                )
            )
        if user_guess < lower_limit:
            user_guess = int(
                input(
                    f"\nYour guess exceeds the lower range. Increase your guess and try again.\nEnter number between {lower_limit} to {upper_limit}: "
                )
            )
    return user_guess


# function to handle checking user input against random number and upper/lower bounds
def guess(num, user_guess):
    upper_limit = 10
    lower_limit = 1
    while num != user_guess:
        if num > user_guess:
            print(f"\nNumber is higher than {user_guess}")
            lower_limit = user_guess
            user_guess = enter_and_verification(lower_limit + 1, upper_limit)
            num_of_guesses++
        elif num < user_guess:
            print(f"\nNumber is lower than {user_guess}")
            upper_limit = user_guess
            user_guess = enter_and_verification(lower_limit, upper_limit - 1)
            num_of_guesses++
        else:
            print()
    print(f"\nCongrats! You've guessed the correct number! It was {num}.\n")
    print("\nYou have tried {num_of_guesses} times to find the number.\n")


# while loop to prompt user to play intially, then continue to play or not
while True:
    play_y_n = input("Welcome to Number Guesser. If you'd like to play, press 'Y': ")
    if play_y_n.lower() == "y":
        num = random.randint(smaller_number, larger_number)
        user_guess = enter_and_verification(lower_limit, upper_limit)
        guess(num, user_guess)
    else:
        print("Thanks for playing!")
        break
