person_dict = { 
    'firstname': 'arshely',
    'lastname': 'kayla', 
    'age': 4,
    'city': 'ibadan',
    "graduation_year": 2005



}

# print(person_dict)

# print(person_dict['firstname'])

# print(f'first name is {person_dict['lastname']} and the last name is {person_dict['firstname']}')

# print(person_dict.setdefault('city', 'lagos'))



# print(list(person_dict.items()))
# print(list(person_dict.keys()))
# print(list(person_dict.values()))





cars = {
    "Toyota": {
        "Sedan": ["Camry", "Corolla", "Avalon"],
        "SUV": ["RAV4", "Highlander", "4Runner"]
    },
    "Ford": {
        "Sedan": ["Fusion", "Taurus"],
        "SUV": ["Escape", "Explorer", "Expedition"]
    },
    "BMW": {
        "Sedan": ["3 Series", "5 Series", "7 Series"],
        "SUV": ["X1", "X3", "X5"]
    }
}

# print(list(cars.items()))


# print(cars['Toyota']['Sedan'])


print(f'{cars['Ford']['SUV'][-1]} ,{(cars['BMW']['Sedan'][0:2])}')







