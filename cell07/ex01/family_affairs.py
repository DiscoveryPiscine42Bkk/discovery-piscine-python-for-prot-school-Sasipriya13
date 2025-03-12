def find_the_redheads(family_dict):
    redheads = list(filter(lambda x: family_dict[x] == 'red', family_dict))
    return redheads
if __name__ == "__main__":
    family = {
        "John": "brown",
        "Alice": "red",
        "Bob": "blonde",
        "Emma": "red",
        "Charlie": "black"
    }
    print(find_the_redheads(family))