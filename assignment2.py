# 1 Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".


name = input('enter name:')

print(f" hello {name}")



# 2 Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”


birth_year = int(input('enter birth year:'))
present_year =int(input('enter present year:'))
age = present_year - birth_year

print(f'you are {age} years old')


# 3 Ask the user for their favourite color. Print a statement that includes the color in the format  
# “Your favorite color is {favourite_color}.”


favourite_color = input('enter color:')

print (f'your favourite color is {favourite_color}')


# 4 Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.

text = input('enter text:')
reversed_word = text[::-1]

is_palindrome = text == reversed_word

print(f'it is {is_palindrome} that {text} is a palindrome')





# 5 Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

password = input('enter password:')
is_valid = len(password)>=8 and len(password)<=30

print(f'it is {is_valid} that the password fulfils the criteria')


# 6  Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
weight = float(input('enter a value:'))
               
height = float(input('enter height:'))
bmi = weight /(height **2)
print(f'your BMI is{bmi}')








