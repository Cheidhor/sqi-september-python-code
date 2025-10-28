questions = [{'question': 'what is a verb', 'keyword': {'word': 2, 'action': 5, 'doing': 3}},
             {'question': 'what is the full meaning of sss', 'keyword':
               {'state': 2, 'security': 3, 'service': 3, 'corps': 2}},
               {'question': 'whats a noun', 'keyword':{'naming': 5,'animal': 2, 'place': 3 }},
               {'question': 'what is the full meaning of nafdac', 'keyword': {'food': 5, 'drug': 5}},
               {'question': 'what is an adverb', 'keyword': {'qualifies': 5, 'verb': 5}}]
total_score = 0
for question in questions:
    print(question['question'])
    student_answer = input('enter your answer:') 
    for keyword , score in question['keyword'].items():
        if keyword in student_answer:
            total_score += score
    print('current score:', total_score)


print('your total score is:', total_score)

