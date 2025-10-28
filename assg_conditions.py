# 1 Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.


# a = int(input('enter first number:'))
# b = int(input('enter second number:'))

# if (a > 0) and (b > 0): 
#  print('a and b are both positive')

# elif a > 0 or b > 0:
#  print ('only one is positive')

# else: 
#  print('neither is positive')


# 2 Collect three numbers x, y and z as a comma separated string input from the user and print
# "Increasing order" if they are in STRICTLY increasing order,
# "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x = int(input('enter number1:'))
# y = int(input('enter number2:'))
# z = int(input('enter number3:'))

# if x > y > z:
#  print('in increasing order')

# elif
# else:
#  print('decreasing')



# 3 Write a program that reads a string called `palindrome` supplied through user input 
# and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".


# statemant = str(input('enter a word:'))

# word = (input('enter a word:'))

# reversed_word = word[::-1]


# if word == reversed_word:
#  print('it is a palindrome')

# else: 
#  print ('not a palindrome')





#4  You have three variables: x, y, and z collected as 3 separate inputs from the user. 
# Write an if statement that checks if exactly two out of the three variables are equal
#  and prints "Two are equal" if this is true. Otherwise, print
#  "All different" or "All same" accordingly.

# x = input('enter word:')
# y = input('enter word2:')
# z = input('enter word3:')

# if x==y or y==z or x==z
#  print('two are equal')
# else:
#  print('all different')

    

#5  Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, 
# use if statements to check if they can form a valid triangle.
#  Print "Valid triangle" if the sum of the angles is 180 degrees 
# and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = int(input('enter value1:'))

# angle2 = int(input('enter value2:'))

# angle3 = int(input('enter value3:'))

# if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
#  print('it is a valid triangle')
# else:
#  print("it isn'nt valid")



#6  You have a single character variable `ch` supplied through user input. 
# Write an if statement that prints "Vowel" if ch is a vowel
#  (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. 
# Assume that the input is a single alphabet character.

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

CH = set(input('enter a value:'))

if CH in vowels:
 print('vowels')

else:
 print('consonant')




# 7 Given a comma separated string input from the user of three colors color1, color2, and color3,
#  write an if statement to check if all three colors are primary colors
#  (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".






#8  You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". 
# Write an if statement that prints "Manual mode activated" if mode is "manual",
#  "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".


# mode = input('enter:')


#9 Given a string `message` entered by the user,
#  use if statements to check if the message contains any of the words "urgent", "important", 
# or "immediate". If it contains any of these words, print "High priority message".
#  Otherwise, print "Normal message".


# message = str(input('enter message:'))

# if 'urgent' in message or ('important'in message) or ('immediate' in message):

#  print('highly priority message')
# else:
 
#  print('normal message')
