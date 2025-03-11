while True:
    user_input = input("Enter something (thpe 'STOP' to quit): ")
    if user_input.upper() == "STOP":
        print("Goodbye!")
        break
    print(f"I got that: {user_input}")