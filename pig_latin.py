# # text = 'hello'

# # vowels = 'aeiou'
# # new_str = text[1:] + text[0] + 'ay'

# # print(new_str)






# # --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# # 1. Create a list of the square of each number
# # Input: [1, 2, 3, 4, 5]
# # Expected Output: [1, 4, 9, 16, 25]
# # digits = [1, 2, 3, 4, 5]

# digits = [1, 2, 3, 4, 5, 6]
# digit_list = []

# for i in digits:
#     calc =  (i ** 2 )
#     digit_list.append(calc)
# print(digit_list)


# #### correction #####

# square_of_digits = [digitt**2 for digitt in digits]

# print(square_of_digits)
    



# # 2. Create a list of names that contain the letter 'a'
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: ["Sara", "Amanda"]
# # names = ["John", "Sara", "Mike", "Amanda"]




# names = ['john', 'sara', 'mike', 'amanda']

# names_with_a = []

# for name in names:
#     if 'a' in name:
#         names_with_a.append(name)

# print(names_with_a)

# ##### correction #####

# names_with_letter_a = [namee for namee in names if 'a' in namee]

# print(names_with_letter_a)

# # 3. Create a list of Booleans indicating if each number is greater than 10
# # Input: [5, 12, 3, 18, 7]
# # Expected Output: [False, True, False, True, False]
# # values = [5, 12, 3, 18, 7]

# nums = [5, 12, 3, 18, 7]

# num_bool = []

# for num in nums:
#     is_grater =  num > 10
#     num_bool.append(is_grater)
# print(num_bool)





# # 4. Create a list of the last characters of each word
# # Input: ["dog", "cat", "lion", "tiger"]
# # Expected Output: ["g", "t", "n", "r"]
# # animals = ["dog", "cat", "lion", "tiger"]

# words = ['dog', 'cat', 'lion', 'tiger']

# last_char_of_word = []

# for word in words:
#     char = word[-1]
#     last_char_of_word.append(char)
# print(last_char_of_word)


# # 5. Are all the numbers greater than 10?
# # Input: [5, 12, 3, 18, 7]
# # Expected Output: False
# # values = [5, 12, 3, 18, 7]



# nums = [5, 12, 3, 18, 7]

# num_bool = []

# for num in nums:
#     bool4 =  num > 10
#     num_bool.append(bool4)

# print("Are all numbers greater than 10? ")
# print(all(num_bool))
    







# # 6. Is there any name that contains the letter 'a'?
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: True
# # names = ["John", "Sara", "Mike", "Amanda"]


# names = ['john', 'sara', 'mike', 'amanda']

# names_with_a = []

# for name in names:
#     bool3 = 'a' in name
#     names_with_a.append(bool3)
    
        

# print(any(names_with_a))

# # 7. Are all the words made up of only uppercase letters?
# # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # Expected Output: False

# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# bool_greeting = []

# # for greeting in greetings:
# #     bool2 = greeting is 
# #     bool_greeting.append(bool2)
# #     if greeting is  :
# #         bool_greeting.append(bool2)
# # print(bool_greeting)


# # 8. Is there any word that starts with 'z'?
# # Input: ["apple", "zebra", "mango", "lemon"]
# # Expected Output: True

# words = ["apple", "zebra", "mango", "lemon"]
# word_with_bool = []
# for word in words:
#     bool1 = word[0] == 'z'
#     word_with_bool.append(bool1)
    
        
# print(any(word_with_bool))
        





# # 9. Is there any email address that contains ".org"?
# # Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# # Expected Output: True
# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# email_with_org = []
# for email in emails:
#     bool5 = 'org' in email
#     email_with_org.append(bool5)
    
        
# print(any(email_with_org))
        

# # 10. Are all numbers odd?
# # Input: [1, 3, 5, 7, 9]
# # Expected Output: True

# values = [1, 3, 5, 7, 9]
# bool_values =[]

# for value in values:
#     bool6 =  value % 2 != 0
#     bool_values.append(bool6)
    
       
# print(all(bool_values))



# # 11. Are all words longer than 2 characters?
# # Input: ["hi", "dog", "go", "sun"]
# # Expected Output: False

# words = ["hi", "dog", "go", "sun"]
# bool_words = []

# for word in words:
#     bool7 = len(word) > 2
#     bool_words.append(bool7)

# print(all(bool_words))
        



# # 12. Create a list of triple the value of each number
# # Input: [2, 4, 6, 8]
# # Expected Output: [6, 12, 18, 24]

# nums = [2, 4, 6, 8]
# nums_output = []

# for num in nums:
#     cal = num * 3
#     nums_output.append(cal)
    

# print(nums_output)



# # 13. Are all temperatures above 0°C?
# # Input: [12, 7, 3, -1, 5]
# # Expected Output: False

# temperatures = [12, 7, 3, -1, 5]
# temp_output = []

# for temp in temperatures:
#     bool8 = temp > 0

#     temp_output.append(bool8)
#     if all(temp_outp
#         print(temp_output)
#         break


# # 14. Do all words end with a vowel?
# # Input: ["banana", "mango", "kiwi", "grape"]
# # Expected Output: True
# fruits = ["banana", "mango", "kiwi", "grape"]
# fruit_with_vowel_at_the_end = []

# for fruit in fruits:
#     if fruit[-1] == 'aeiou':
#         bool9 = fruit[-1] == 'aeiou'
#         fruit_with_vowel_at_the_end.append(bool9)
#     if any(fruit_with_vowel_at_the_end):
#         print(fruit_with_vowel_at_the_end)
#         break


# # 15. Create a list of words in lowercase
# # Input: ["HELLO", "WORLD", "PYTHON"]
# # Expected Output: ["hello", "world", "python"]
# greetings = ["HELLO", "WORLD", "PYTHON"]

# greeting_lower = []

# for greeting in greetings:
     
#     greeting_lower.append(greeting.islower())
# print(greeting_lower)



# # 16. Is there any number less than 0?
# # Input: [5, -2, 3, 0, 8]
# # Expected Output: True
# numbers = [5, 4, 3, 3, 8]
# num_outputs = []

# for number in numbers:
#     if num < 0:
#         bol = num < 0
#         num_outputs.append(bol)
#     if any(num_outputs):
#         print(num_outputs)
#         break


# # 17. Create a list of words that contain the letter 'e'
# # Input: ["sky", "tree", "rock", "stone"]
# # Expected Output: ["tree", "stone"]
# items = ["sky", "tree", "rock", "stone"]


# # 18. Are all names starting with uppercase letters?
# # Input: ["Alice", "Bob", "charlie", "David"]
# # Expected Output: False
# names = ["Alice", "Bob", "charlie", "David"]


# # 19. Is there any sentence longer than 20 characters?
# # Input: ["Short one", "This is a much longer sentence", "Okay"]
# # Expected Output: True

# sentences = ["Short one", "This is a much longer sentence", "Okay"]

# sentence_check = []
# for sentence in sentences:
#     more_than_20 = len(sentence) >= 20
#     sentence_check.append(more_than_20)
#     if any(sentence_check):
#         print(sentence_check)
#         break






