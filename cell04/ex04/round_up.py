import math
num = input("Give me a number: ")
try:
    f = float(num)
    rounded = math.ceil(f)
    print(rounded)
except ValueError:
    print("That's not a valid number.")