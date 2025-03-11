user_input = input("Enter a number: ")
try:
    number = float(user_inpyt)
    if '.' in user_input:
        print(f"{user_input} is a decimal.")
    else:
        print(f"{user_input} is an integer.")
except ValueError:
    print("That's not yalid number.")