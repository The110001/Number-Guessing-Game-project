# import modules
import random

## random number script ##

# welcome message
print("Hello dear user. We are so glad that you are here :)\n"
      "This is a Number Guessing game and you are prompted to choose\n"
      "a range from the options below. Then our program will choose\n"
      "a random number that you must guess correctly. You have a specific\n"
      "number of guesses, so be wise and do not waste them ;)\n"
      "That is all :)\n")

# different ranges, chances and number of guesses
range1, chances1, number_to_guess1 = range(1,100 + 1), 8, random.randrange(1,100 + 1)
range2, chances2, number_to_guess2 = range(1,500 + 1), 9, random.randrange(1,500 + 1)
range3, chances3, number_to_guess3 = range(1,1000 + 1), 10, random.randrange(1,1000 + 1)

# random number function
def random_num (range, chances, number_to_guess):
    # local variables
    guess_counter = 0

    # the event loop

    print("Please provide your guess below.\n"
          "WARNING: Do not type any unexpected characters such as alphabets, decimal numbers,\n"
          "and special characters such as !,#,$, etc.\nThese exceptions will raise an error\n"
          "and reduce your number of chances! So be careful.")

    while guess_counter <= chances:
        user_number = input("\n--> ")
        guess_counter += 1

        # conditions
        # user number = number to guess
        if user_number.isdigit() and int(user_number) == number_to_guess:
            if guess_counter == 1:
                return (f"\nWell done! You managed to guess the number on your first try !!!!!\n"
                      "congratulations and hope to see you again in our program ;)\n"
                        f"the correct number: {number_to_guess}")
            else:
                return ("\nWell done! You managed to guess the number correctly\n"
                      "congratulations and hope to see you next time in our program ;)\n"
                        f"the correct number: {number_to_guess}")
        # user number < number to guess
        elif user_number.isdigit() and int(user_number) < number_to_guess:
            if guess_counter == chances:
                return (f"\nOH NOOO!!! you could not guess the number correctly.\n"
                        "better luck next time.\n"
                        f"the correct number: {number_to_guess}")
            elif guess_counter == chances - 1:
                print(f"\nyour number is less than the target.\n"
                      "be careful, you have one more attempt left !!!\n")
            else:
                print(f"\nyour number is less than the target.\n"
                      "try again.\n"
                      f"you have {chances - guess_counter} chance/chances left")
        # user number > number to guess
        elif user_number.isdigit() and int(user_number) > number_to_guess:
            if guess_counter == chances:
                return (f"\nOH NOOO!!! you could not guess the number correctly.\n"
                        "better luck next time.\n"
                        f"the correct number: {number_to_guess}")
            elif guess_counter == chances - 1:
                print("\nyour number is greater than the target.\n"
                      "be careful, you have one more attempt left !!!\n")
            else:
                print("\nyour number is greater than the target.\n"
                      "try again.\n"
                      f"you have {chances - guess_counter} chance/chances left")
        else:
            if guess_counter == chances:
                return (f"OH NOOO! YOU DUMMYYY !!!!!\n"
                        f"you wasted your last attempt by typing something stupid !!\n"
                        f"the correct number: {number_to_guess}")
            elif guess_counter == chances - 1:
                print("\nyour input is not acceptable.\n"
                      "be careful, you have one more attempt left !!!\n"
                      "do not wasted this chance!")
            else:
                print("\nyour input is not acceptable.\n"
                      "be careful to not waste your chances\n"
                      f"you have {chances - guess_counter} chance/chances left")

# user choices
def user_choice():

    # display the choices for the user
    print(f"\nthese are the available options:\n"
          f"choice 1: range -> (1,100), chances -> {str(chances1)}\n"
          f"choice 2: range -> (1,500), chances -> {str(chances2)}\n"
          f"choice 3: range -> (1,1000), chances -> {str(chances3)}")

    # options = "choice 1": choice1, "choice 2": choice2, "choice 3": choice3
    # create a loop and conditions for the user to choose an option

    print("\nNow please type your choice down below.\n"
          "Try to type choice 1, choice 2, or choice 3.\n"
          "do not add any extra character or spaces!")

    while True:
        user_input = input("\n--> ")

        if user_input == "choice 1":
            result1 = random_num(range1, chances1, number_to_guess1)
            return result1
        elif user_input == "choice 2":
            result2 = random_num(range2, chances2, number_to_guess2)
            return result2
        elif user_input == "choice 3":
            result3 = random_num(range3, chances3, number_to_guess3)
            return result3
        else:
            print("\nYour input is not acceptable.\n"
                  "please try to avoid any misspelling and unwanted characters.\n"
                  "thank you.\n")

end_program = user_choice()
print(end_program)
