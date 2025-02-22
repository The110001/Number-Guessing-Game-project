# writing a program to create a pyramid with numbers
# get the input from the user

while True:
    number = input('please provide a number here. Make sure to not include any alphabet, spaces or new lines.\nAnd the number must be greater or equal to 5. thank you\n--> ')
    if number.isdigit() and int(number) >= 5 :
        print("thank you for the input.")
        break
    else:
        print("your input does not match our rules. Please try again.\n")

def program():
    integer = int(number)

    for i in range(1, integer + 1):
        for j in range(1,i + 1):
            print(j, end = " ")
        print("")

program()