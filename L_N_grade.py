def usersChoice(choice):
    if choice == 'Number':
        enter_num = float(input("Enter the Grade Point: "))
        if 3.9 <= enter_num <= 4.9:
            print("The Score is A")
        elif 2.9 <= enter_num <= 3.8:
            print("The Score is B")
        elif 1.9 <= enter_num <= 2.8:
            print("The Score is C")
        elif 0.9 <= enter_num <= 1.8:
            print("The Score is D")
        else:
            print("The Score is F")
    elif choice == 'Letter':
        enter_letter = str(input("Enter the Letter Grade: "))
        enter_letter = enter_letter.upper()
        if enter_letter == 'A':
            print("The Score is greater than 3.9")
        elif enter_letter == 'B':
            print("The Score is greater than 2.9")
        elif enter_letter == 'C':
            print("The Score is greater than 1.9")
        elif enter_letter == 'D':
            print("The Score is greater than 0.9")
        elif enter_letter == 'F':
            print("The Score is less than 0.9")
        else:
            print("Invalid Entry")


enter_choice = str(input("Enter your Choice: "))
enter_choice = enter_choice.title()
usersChoice(enter_choice)

