def add_one(number):
    return number + 1
def main():
    my_var = 5
    print(f"Initial value of my_var: {my_var}")
    my_var = add_one(my_var)
    print(f"Updated value of my_var after add_one: {my_var}")
if __name__ == "__main__":
    main()