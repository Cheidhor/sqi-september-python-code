import getpass
import string
symbol = string.punctuation






# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print('fizzbuzz')
#     elif i % 3 == 0:
#         print('fizz')
#     elif i % 5 == 0:
#         print('buzz')
    
#     else:
#         print(i)







# sentence = input('enter a sentence:').split()
# acronym = []
# for word in sentence:
#     acronym.append(word[0].upper())
# print(''.join(acronym))


    





#  3 write a program that continuously prompts the user to enter a password until they enter a valid one.
#  A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

password = input('enter password:')
has_valid_length = [len(password) >= 8  for length in password]
has_upper = any([length.isupper() for length in password])
has_lower = any([length.islower()for length in password])
has_symbols= any([length in symbol for length in password])
has_valid_l= any([len(password) >= 8 for length in password])

is_valid = [has_valid_length, ]


while True:
    password = input('enter password:')
    has_valid_length = len(password) >= 8  and len(password) <= 20
    # is_valid = [has_valid_length, ]
    if  has_valid_length:
        print('password accepted')
        break
    else:
        print('your password must be at least 8 characters long and have a maximum of 25 characters')








# 4  Write a program that asks for the user's age and keeps prompting them until they 
	# enter a valid age (greater than or equal to 0).
	# Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.

while True:
    user_age =int( input('enter age:'))
    if user_age <= 0:
        print('invalid age. please enter a valid age')
        continue
    else:
        print('age accepted')
        break





#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


print('THE CURRENT STORE INVENTORY IS')

inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}
print(inventory)

while True:
    operation = input('enter operation : (add/remove/exit)')
    if operation == 'exit':
        break
    elif operation == 'add':
       item = input('enter item:')
       qnty = int(input('enter quantity:'))
    if item in inventory:
        inventory = inventory[item]
        print(inventory)
        break


    
    