
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<


import random  

print('>>>>>>>>>>>> QUOTES OF THE DAY <<<<<<<<<<<<<<')

categories = [ 'love', 'motivation', 'inspiration', 'wisdom']

categories.sort()

print(f'available categories are: {categories}')

user_category_choice = input('enter category of choice:')

love = [{'quote':'where there is love there is life' , 'author': 'Mahatma Gandhi'}, 
               {'quote': 'love is an act of endeless forgiveness', 'author':'Peter Ustinov' },
                {'quote': 'love all, trust few' , 'author': 'William Shakesphere' }, 
                {'quote': 'love is the master key', 'author': 'Henry Ward Beecher' }]



motivation = [{'quote':'believe you can and you are halfway there','author':'Theodore Roosevelt'}, 
               {'quote':'do someting today that your future self will thank you for' , 'author': 'unknown'},
                {'quote' : 'big dream work hard' , 'author': 'unknown'}, 
                {'quote' :'dream big' , 'author':'meeeee' }]



inspiration = [{'quote': 'believe in yourself', 'author': 'unknown'}, 
               {'quote':'dream big' , 'author': 'David McCullough'},
                {'quote': 'never give up', 'author': 'meee'}, 
                {'quote': 'do epic shiiit!!' , 'author':'hina'}]



wisdom = [{'quote':'silence is golden' , 'author':'Thomas Carlyle' }, 
               {'quote': 'patience is bitter but the fruit sweet', 'author':'Jacques Rousseau' },
                {'quote': 'learn from yesterday', 'author':'fredd' }, 
                {'quote':'wisdom begins in wonder' , 'author':'socrtes' }]


# quotes = [love, inspiration, wisdom, motivation]

love_randomindex = random.randint(0, len((love))-1)
inspiration_randomindex = random.randint(0, len((inspiration))-1)
motivation_randomindex = random.randint(0, len((motivation))-1)
wisdom_randomindex = random.randint(0, len((wisdom))-1)




lovequote = love[love_randomindex]['quote']
loveauthor = love[love_randomindex]['author']

# print(inspiration[inspiration_randomindex])

inspirationquote = inspiration[inspiration_randomindex]['quote']
inspirationauthor = inspiration[inspiration_randomindex]['author']



wisdomquote = wisdom[wisdom_randomindex]['quote']
wisdomauthor = wisdom[wisdom_randomindex]['author']


motivationquote = motivation[motivation_randomindex]['quote']
motivationauthor = motivation[motivation_randomindex]['author']



if user_category_choice == categories[0]:
    print(f'{lovequote}                                            {loveauthor}   ')
    


if user_category_choice == categories[1]:
    print (f' {motivationquote}                       {motivationauthor}')



if user_category_choice == categories[2]:
    print (f' {inspirationquote}                       {inspirationauthor}')


if user_category_choice == categories[3]:
    print(f' {wisdomquote}             {wisdomauthor}')




























# >>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<

# print('>>>>>>>>> PASSWORD GENERATOR <<<<<<<<<<<<')

# password_type = ['only numbers', 'letters and numbers', 'letters numbers and symbols']

# print(f'choose from these types : {password_type}')

# user_type = input('enter your type:')

# only_numbers = string.digits
# rand_only_numbers = random.randint(only_numbers)


