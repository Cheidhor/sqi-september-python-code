# books = [ 
# {'title': 'the shadow blade', 'author': 'madi agnes' , 'year of publication': 2005, 'ISBN':'isbn-1453221' , 'available': True},
# {'title': 'hunter x hunter' ,'author': 'james' , 'year of publication': 2015, 'ISBN':'isbn-1474649' , 'available': True},
# {'title': 'king slayers' ,'author': 'laureth' , 'year of publication': 2018, 'ISBN':'isbn-1432765' , 'available': False}

#   ]
         

# def add_book():
#     title = input('enter title:')
#     author = input('enter author:')
#     year_of_publication = input('enter year:')
#     isbn = input('enterisbn number:')
#     available = bool(int(input('enter 1 if true or 0 if wrong:')))
#     new_book = {'title': title, 'author': author, 'year of publication': year_of_publication, 
#                  'ISBN': isbn, 'available': available} 
#     books.append(new_book)

#     print('new book added!!')



# def view_book ():
#     print('TITLE \t\t|AUTHOR\t\t|YEAR OF PUBLICATION\t\t|ISBN\t\t|AVAILABLE')


#     for book in books:
#      print(f'{book['title']}\t\t|{book['author']}\t\t|{book['year of publication']}\t\t|{book['ISBN']}\t\t|{book['available']}')


# def update_book (isbn):
#     # isbn_number = input('enter isbn number:')
#     for book in books:
#         if book['ISBN'] == isbn:
#             new_year =  input('enter new year of publication:')
#             new_available =  input(int(('enter 1 for true and 0 for false:')))
#             book['year of publication'] = new_year
#             book['available'] = new_available
#             print('your books has been updated!!')
#             break
#         else:
#             print('book not found')


# def delete_book(isbn):
#     for book in books:
#         if book['ISBN'] == isbn:
#             books.remove(book)
#             print(f'book with isbn {isbn} deleted successfully')
#             break
#     else:
#         print(f'book with isbn{isbn} not found')



# def search_book(title):
#     for book in books:
#         if book ['title'].lower() == title.lower():
#             print(book)
#             break
#     else:
#         print(f'book with title {title} not found')



# def borrow_book(isbn):
#     for book in books:
#         if book['available']:

    




# # def return_book(isbn):
# #     for book in books:
# #         if book






# # while True:
    

# #     print('choose from the options below:')
# #     print('''
# #    1 add_book
# #    2 view_book
# #    3 update_book 
# #    4 delete_book 
# #    5 search_book 
# #    6 borrow_book 
# #    7 return_book  ''')
    
#     # option = input('enter an option:')

#     # if option == 1:
#     #     add_book() 
#     # elif option == 2:
#     #     view_book()
#     # elif option == 3:
#     #     update_book()
#     # elif option == 4:
#     #     delete_book()
#     # elif option == 5:
#     #     search_book()
#     # elif option == 6:
#     #     borrow_book()
#     # # elif option == 7:
#     # #     return_book()
