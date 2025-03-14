def famous_births(people_dict):
    sorted_people = sorted(people_dict.values(), key=lambda x: x['date_of_birth'])
    for person in sorted_people:
        print(f"{person['name']} was born in {person['date_of_birth']}.")
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)