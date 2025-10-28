# # def power(num1, num2):
# #     print(num1 ** num2)

# # power(5, 7)
# # power(5, 2)



# # numbers = [3, 5, 2, 2, 5, 4, 6, 56, 3, 65, 34, 56, 3, 4]

# # def avg(average_list):
# #     # numbers_sum = ?sum(average_list)
# #     print(sum(average_list)// len(average_list))
# # avg(numbers)


# # def multiply(multiply_list):
# #     count = 1
# #     for num in multiply_list:
# #         count *= num
# #     print(count)



# # multiply(numbers)


# # def cube(num):
# #     result = num ** 3
# #     return result

# # solution = cube(5)
# # print(solution)







# import string
# # -----------------------------------------ASSIGNMENT-----------------------------------------------

# # 1. Create a function called turn_to_upper(names) that takes in a list of names,
# #  and returns a list of names uppercased
# # after, print the result of the function.
# # For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], 
# # the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]
# list_of_names = ['kayla', 'hina', 'arshely', 'happi']
# def turn_to_upper(names):
#     flop = []
#     for ch in names:
#         flop.append(ch.upper())
#     print(flop)
# turn_to_upper(list_of_names)


# # 2. Create a function called get_middle_name that accepts one paramter `name_dict`
# #  that takes in a dictionary with keys "first", "middle", and "last".
# # The function should return only the middle name.
# # For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"},
# #  then the result would be "James". Another example is if name_dict is
# #  {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".

# name = {"first": "Tola", "middle": "James", "last": "Akin"}

# def get_middle_name(name_dict):
#     return name_dict['middle']

# output = get_middle_name(name)
# print(output)

# # 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# # For example, if the string is "Python", the result would be "nohtyP".

# word = input('enter the string:')
# def reverse_string(item):
    
#     return item[::-1]

# result = reverse_string(word)
# print(result)


# # 4. Create a function called count_vowels that accepts a string and returns 
# # the number of vowels (a, e, i, o, u) in it.
# # For example, if the string is "beautiful", the result would be 5.

# textt = input('enter a word:')
# vowel = 'aeiou'
# def count_vowels(text):
#     score = 0
#     for ch in text:
#         if ch in vowel:
#             score += 1
#     return score

# out_put = count_vowels(textt)
# print(out_put)


# # 5. Create a function called even_numbers that takes in a list of integers 
# # and returns a new list containing only the even numbers.
# # For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].

# the_list_is = [1, 2, 3, 4, 5, 6]
# def even_numbers(num):
#     new_list = []
#     for ch in num:
#         if ch % 2 == 0:
#              new_list.append(ch)
#     return new_list

# even_int = even_numbers(the_list_is)
# print(even_int)




# # 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# # For example, if the list is [12, 45, 3, 67, 23], the result would be 67.

# my_numbers =  [12, 45, 3, 67, 23]
# def find_max(num):
#     return max(num)

# maximum = find_max(my_numbers)
# print(maximum)

# # 7. Create a function called sum_dict_values that takes in a dictionary 
# # with numeric values and returns the sum of all the values.
# # For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.

# number_dict = {"a": 10, "b": 20, "c": 5}

# def sum_dict_values(num):
#     return sum(num.values())

# num_sum = sum_dict_values(number_dict)
# print(num_sum)

# # 8. Create a function called word_lengths that takes in a list of words
# #  and returns a dictionary where each word is a key and its length is the value.
# # For example, if the list is ["apple", "banana", "cherry"], the result would be 
# # {"apple": 5, "banana": 6, "cherry": 6}.

# # keys = 'a', 'b', 'c'
# # list_of_words =  ["apple", "banana", "cherry"]
# # def word_lengths( words, value):
    
# #     return  words , value
# # for ch in list_of_words:
# #         length = len(ch)
# # result = word_lengths( list_of_words, length)
# # print(result)



# # 9. Create a function called is_palindrome that takes in a string and returns
# #  True if the string is a palindrome (same forwards and backwards), otherwise False.
# # For example, if the string is "level", the result would be True. If the string is "hello",
# #  the result would be False.

# palindrome = input('enter a word:')
# def is_palindrome(word):
#      return word == word[::-1] 
# output = is_palindrome('token')
# print(output)
   

# # output = is_palindrome(palindrome)
# # print(output)
          


# # 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# # For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].

# # list1 = [1, 2, 3]
# # list2 = [3, 4, 5]
# # def mearge_list(listt, listt1):
# #      return listt.append(listt1)

# # output1 = mearge_list(list1, list2)
# # print(output1)
     

# # 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# # If the second number is not provided, it should default to 2.
# # Example 1: multiply_numbers(5) → 10
# # Example 2: multiply_numbers(5, 3) → 15



# # 12. Create a function called greet_user(first_name, last_name="") that returns a greeting string.
# # If last_name is not provided, it should only greet with the first name.
# # Example 1: greet_user("Ada") → "Hello, Ada!"
# # Example 2: greet_user("Tola", "Akin") → "Hello, Tola Akin!"

# # 13. Create a function called power(base, exponent=2) that raises the base to the power of the exponent.
# # The exponent should default to 2 (square).
# # Example 1: power(4) → 16
# # Example 2: power(2, 3) → 8

# # 14. Create a function called format_full_name(first, middle="", last="") 
# # that returns the full name as a single string.
# # If middle or last is not provided, it should still work correctly.
# # Example 1: format_full_name("John", "Paul", "Smith") → "John Paul Smith"
# # Example 2: format_full_name("Ada", last="Okeke") → "Ada Okeke"

# # 15. Create a function called calculate_discount(price, discount=10, tax=0)
# #  that calculates the final price after applying
# # a discount (percentage) and then adding tax (percentage).
# # Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# # Example 2: calculate_discount(200, discount=20, tax=5) → 168.0

# # -----------------------------------------ASSIGNMENT-----------------------------------------------



# def find_minimum(mini):
#     minimum = mini[0]
#     for num in mini:
#         if num < minimum:
#             minimum = num
#     return minimum

# output = find_minimum([1,3,5,2,0,-1,-2])

# print(output)




# def is_alliteration(two_word_string):
#     splitted_word = two_word_string.lower().split()
#     return splitted_word[0][0] == splitted_word[1][0]
       
    
# print(is_alliteration('hello cowdy'))







































# 1 Write a function sum_numbers(a, b) that returns the sum of two numbers.

def sum_number(a, b):
    return a + b

print(sum_number(5,7))

# 2 Write a function is_even(n) that returns True if n is even and False if n is odd.

def is_even(n):
    return n % 2 == 0 

print(is_even(4))

# 3 Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

def is_prime(n):
    return n / 1 == n and n / n == 1

print(is_prime(16))

# 4 Using the is_prime(n) function from number 3, write a function that asks a user for an input n and 
# returns all the prime numbers up to n.



# 5 Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers
#  if both numbers are even, but returns the greater if one or both numbers are odd.



# 6 Write a function is_alliteration(two_word_string) that takes a two-word string  
# and returns True if both words begin with the same letter.is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False



# 7 Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

def old_macdonald(n):
     n[0].upper()
     n[3].upper()
     return n



# 8 Write a function spy_game(list_of_ints) that takes in a list of integers and
#  returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False



# 9 Write a function vol(radius) that computes the volume of a sphere given its radius.

# 10 Write a function range_check(num, low, high) that checks whether a number is in a given range
#  (inclusive of high and low).



# 11 Write a function upper_lower(text) that accepts a string and calculates
#  the number of uppercase letters and lowercase letters.



# 12 Write a function unique_list(list_items) that takes in a list and 
# returns a new list with unique elements of the first list. Do not use the set() constructor.


    
#  13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24



#  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.



#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.



#  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.



#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).

