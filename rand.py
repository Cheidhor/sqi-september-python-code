import random


# computer_guess1 = random.randint(1, 20)
# computer_guess2 = random.randint(1, 20)
# computer_guess3 = random.randint(1, 20)
# # 
# computer_guesss = [computer_guess1, computer_guess2, computer_guess3]

# print (f'hint: {computer_guess1}, {computer_guess2}, {computer_guess3}')

# user_guess1 = int(input('enter first guess:'))
# user_guess2 = int(input('enter second guess:'))
# user_guess3 = int(input('enter third guess:'))

# user_gusses = [user_guess1, user_guess2, user_guess3]

# user_guesses2 = input('enter the three guess [hint: 1-10]')
# print(user_gusses2)

# if computer_guesss == user_gusses:
#     print('congrat!!!! you just won..')

# else:
#     print('oops! try again')











score = 0
computer_guess1 = random.randint(1, 20)
computer_guess2 = random.randint(1, 20)
computer_guess3 = random.randint(1, 20)
# 
computer_guesss = [computer_guess1, computer_guess2, computer_guess3]

print (f'hint: {computer_guess1}, {computer_guess2}, {computer_guess3}')

user_guess1 = int(input('enter first guess:'))
user_guess2 = int(input('enter second guess:'))
user_guess3 = int(input('enter third guess:'))

user_gusses = [user_guess1, user_guess2, user_guess3]

# user_guesses2 = input('enter the three guess [hint: 1-10]')
# print(user_gusses2)

if computer_guess1 == user_guess1:
    print('congrat!!!! you just won the first round')
    score += 10


if computer_guess2 == user_guess2:
    print('congrat!! you won the second round:')
    score += 10

if computer_guess3 == user_guess3:
    print('congrat!! you won the third round:')
    score += 10

if score >= 20:  
    print('you just passed!!')

else:
    print('you failed!!')


        



