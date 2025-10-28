# 1 Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".



student2 = {'name': 'john', 'age': '20', 'grade': 'A'}

print(student2['name'])



#2  Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.



product = {'name': 'laptop', 'price': 999.99, 'stock': 50}

product['price'] = 899.99

print(product)




#3  Create a dictionary called `employee` with keys "name" and "position", 
# and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.


employee = {'name': 'alice', 'position': 'manager'}

employee['salary'] = 50000

print(employee)




# 4 Create a dictionary called `inventory` with keys "apple", "banana", and "orange",
#  and values 10, 5, and 8 respectively. Remove the key "banana".

inventory = {'apple': 10, 'banana': 5, 'orange': 8}
# inventory.clear()
# del inventory['banana']

# print(inventory)

# 5 Create a dictionary called person with keys "name", "age", and "city", 
# and corresponding values "Bob", 25, and "New York". 
# Use the copy() method to make a copy of the dictionary and call it person_copy.


person = {'name':'bob', 'age':25, 'city':'newyork'}


person_copy = person.copy()

print(person_copy)

# 6 Create a nested dictionary called `family` with keys "child1", "child2", and "child3",
#  each containing a dictionary with keys "name" and "age" with appropriate values.
#  Access and print the age of "child2".




family = {'child1': {'name': input('enter name:'), 'age': input('enter age:')}, 
          'child2': {'name': input('enter name:'), 'age': input ('enter age')}, 
          'child3': {'name': input('enter name:'), 'age': input('enter age:')}}

print(family)



#7  Create a dictionary called `car` with keys "brand", "model", and "year", 
# and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".

cars = {'brand': 'toyota', 'model': 'corolla', 'year': 2020}

print(cars['model'])


# 8 Create a dictionary called `settings` with keys "volume", "brightness", and "language", 
# and corresponding values 50, 75, and "English". Change the "language" to "Spanish".

settings = {'volume': 50, 'brighteness': 75, 'language': 'english'}

settings['language'] = 'spsnish'

print(settings)


#9  Create a dictionary called `scores` with keys "math", "science", and "english",
#  and corresponding values 90, 85, and 88. Remove the key "science".


scores = {'math': 90, 'science': 85, 'english': 88}

scores.pop('science')

print(scores)

# 10 Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", 
# and corresponding values "Soup", "Steak", and "Ice Cream". 
# Check if the key "appetizer" is present in the dictionary.


menu = {'starter': 'soup', 'main_course': 'steak', 'dessert': 'ice cream'}




# 11 Create a dictionary called `config` with keys "theme", "language", and "timezone",
#  and corresponding values "dark", "English", and "UTC". Clear the dictionary.


config = {'theme': 'fark', 'language': 'english', 'timezone': 'UTC'}

config.clear()

print(config)

#  12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.

phone_book = {
    'Alice' : "0909888833",
    'Bob' : "09998883828"
}

print(len(phone_book))

# phone_book = {'alice': }

#  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.


grades = {'math': 'A', 'science': 'B', 'history': 'C'}

print(list(grades.keys()))

#  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.


employe = {'name': 'david', 'position': 'engineer', 'salary': 70000}

print(list(employe.values()))



#  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.

game = {'title': 'minecraft', 'genre': 'sandbox', 'rating': '4.5'}

print(list(game.keys()))
































# ===============================
# Nested Dictionary Modification Exercises
# ===============================

# Q1. Given this dictionary, change the "math" score to 95.
# student = {
    # "name": "Alice",
    # "scores": {"math": 80, "english": 85}}

student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}}

student['scores']['math'] = 95
print(student)




# Expected Output:
# {'name': 'Alice', 'scores': {'math': 95, 'english': 85}}


# Q2. Add a new subject "science" with score 90 inside "scores".
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }

student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}

student['scores']['science'] = 90

print(student)





# Q3. Change the author's name of "Python 101" to "Mike".
# library = {
#     "Python 101": {"author": "Tom", "year": 2020},
#     "Data Science": {"author": "Jane", "year": 2021}
# }

library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}


library['Python 101']['author'] = 'mike'

print(library)




# Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
# library = {
#     "Python 101": {"author": "Tom", "year": 2020},
#     "Data Science": {"author": "Jane", "year": 2021}
# }




library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}}


library['Data Science']['publisher'] = "o'Reilly"

print(library)





# Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
# contacts = {
#     "Alice": {"home": "555-123", "mobile": "555-456"},
#     "Bob": {"home": "555-789"}
# }



contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}


contacts['Alice']['work'] = '555-999'

print(contacts)




# Q6. Change Bob’s "home" number to "555-000".
# contacts = {
#     "Alice": {"home": "555-123", "mobile": "555-456"},
#     "Bob": {"home": "555-789"}
# }


contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}

contacts['Bob']['home'] = '555-456'

print(contacts)




# Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# into the list of students.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]


students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]

new_student = {'name': 'eve', 'scores': {'math': 88, 'english': 92}}

students.append(new_student)

print(students)






# Q8. Change Bob's english score from 70 to 78.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]


students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]

students[1]['scores']['english'] = 78


print(students)




# Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# inside Alice’s record under a new key "enrollment".
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 78}}
# ]

students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 78}}
]


new_dictionary ={'enrollment': {'year': 2022, 'semester': 'spring'}}

students.append(new_dictionary)

print(students)




# Q10. In this shop cart, add a new product "Notebook" with price 200.
# cart = {
#     "items": [
#         {"name": "Pen", "price": 10},
#         {"name": "Book", "price": 50}
#     ],
#     "owner": "Alice"
# }


cart = {
    "items": [{"name": "Pen", "price": 10},{"name": "Book", "price": 50}],
    "owner": "Alice"
                       }

new_product = {'name': 'notebook', 'price': 200}

cart['items'].append(new_product)

print(cart)






# Expected Output:
# {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
#  'owner': 'Alice'}



