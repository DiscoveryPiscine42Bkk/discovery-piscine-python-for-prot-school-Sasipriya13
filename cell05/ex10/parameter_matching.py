import sys
if len(sys.argv) == 2:
    parameter = sys.argv[1]
    user_input = input("Enter a word: ")
    if user_input == parameter:
        print("Good jop!")
    else:
        print("Nope, sorry...")
else:
    print("none")