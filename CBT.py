questions = [{'question': 'whats the color of the sky', 'options': ['a. blue', 'b. yellow'], 'answer': 'a'}, 
{'question': 'What is 2 + 2?', 'options': ['a. 3', 'b. 4'], 'answer': 'b'}, 
{'question': 'How many legs does a spider have?', 'options': ['a. 8', 'b. 6'], 'answer': 'a'}, 
{'question': 'What sound does a cow make?', 'options': ['a. moo', 'b. meow'], 'answer': 'a'}, 
{'question': 'What is the opposite of hot?', 'options': ['a. ice', 'b. cold'], 'answer': 'b'}
             ]

score = 0
for question in questions:
    print(question['question'])
    options = question['options']
    print('\n'.join(options))
    answer = input('enter answer:')
    if answer == question['answer']:
        print('correct answer')
        score += 10
    else:
        print('incorrect')

print('total score is:', score)