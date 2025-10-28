# file = open("words.txt")
# vowel = 'aeiou'
# total_vowel = 0
# for word in file.read().split():
    
#     if word[0] in vowel:
#         total_vowel += 1

# print(total_vowel)






# file = open("words.txt")

# total_num = 0
# for word in file.read().split():
    
#     if len(word) >= 5:
#         total_num += 1 

# print(total_num)





# with open('numbers_with_exponents.txt', 'w') as myfile:
#     for i in range(1,101):
#         myfile.write(f'{i}, {i**2}, {i**3}\n') 



import datetime

today = datetime.datetime.now()


# year = int(input('enter year of birth:'))

# print(f'your current age is {today.year - year } ')


age = int(input('enter current age:'))

print(f'your birth year is {today.year - age}')