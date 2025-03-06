# import modules
import random
import tkinter as tk

# random number function
def random_num (range, chances, number_to_guess):
    # local variables
    guess_counter = 0

    # the event loop
    while guess_counter <= chances:
        guess_counter += 1
        user_number = int(input("\nPlease provide your guess here: "))

        # conditions
        # user number = number to guess
        if str(user_number).isdigit() and user_number == number_to_guess:
            if guess_counter == 1:
                return (f"\nWell done! You managed to guess the number on your first try !!!!!\n"
                      "congratulations and hope to see you again in our program ;)\n"
                        f"the correct number: {number_to_guess}")
            else:
                return ("\nWell done! You managed to guess the number correctly\n"
                      "congratulations and hope to see you next time in our program ;)\n"
                        f"the correct number: {number_to_guess}")
        # user number < number to guess
        elif str(user_number).isdigit() and user_number < number_to_guess:
            if guess_counter == chances:
                return (f"\nOH NOOO!!! you could not guess the number correctly.\n"
                        "better luck next time.\n"
                        f"the correct number: {number_to_guess}")
            elif guess_counter == chances - 1:
                print("\nyour number is less than the target.\n"
                      "be careful, you have one more attempt left !!!")
            else:
                print("\nyour number is less than the target.\n"
                      "try again.")
        # user number > number to guess
        elif str(user_number).isdigit() and user_number > number_to_guess:
            if guess_counter == chances:
                return (f"\nOH NOOO!!! you could not guess the number correctly.\n"
                        "better luck next time.\n"
                        f"the correct number: {number_to_guess}")
            elif guess_counter == chances - 1:
                print("\nyour number is greater than the target.\n"
                      "be careful, you have one more attempt !!!")
            else:
                print("\nyour number is greater than the target.\n"
                      "try again.")
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
                  "be careful to not waste your chances")

# different ranges and number of guesses
range1, chances1, number_to_guess1 = range(1,100 + 1), 7, random.randrange(1,100 + 1)
range2, chances2, number_to_guess2 = range(1,500 + 1), 8, random.randrange(1,500 + 1)
range3, chances3, number_to_guess3 = range(1,1000 + 1), 9, random.randrange(1,1000 + 1)

# tkinter GUI
main_window = tk.Tk()

main_window.title("Number Guessing Game")
main_window.mainloop()

# welcome message
print("Hello dear user. We are so glad that you are here :)\n"
      "This is a Number Guessing game and you are prompted to choose\n"
      "from the below options one range. Then our program will choose\n"
      "a random number that you must guess correctly. You have a specific\n"
      "number of guesses, so be wise and do not waste them ;)"
      "That is all :)\n"
      "\n"
      "WARNING: Do not type any unexpected characters such as alphabets, decimal numbers, and special characters such as !,#,$, etc.\n"
      "These exceptions will raise an error and reduce your number of chances! So be careful.")