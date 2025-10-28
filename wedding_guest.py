# 1 Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.


names = ['zoe', 'alice', 'bob']
names.sort()
print (names)


# 2 Create a list called ages with items 25, 35, 20. Sort the list in descending order

ages = [25, 35, 20 ]
ages.sort(reverse = True)
print (ages)


# 3 Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.

words = ['Apple', 'banana', 'Orange']

words.sort()
print(words)



# 4 Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.


numbers = [1, 2, 3, 4]


numbers.sort(reverse = True)

print(numbers)



# 5 Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
 # slicing.


letters = ['a', 'b', 'c', 'd']

print (letters[::-1])




# 6 Create a list called original with items "one", "two", "three". Create a copy of the list.

original = ['one', 'two', 'three']

original_copy = original.copy()

print (original_copy)



# 7 Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# # list2 together.


list1 = ['a', 'b']

list2 = ['c', 'd']

list1.extend(list2)


print(list1)


# 8 Access and print the second subject of the first person in the list.
	# data = [
    # ["Alice", 25, ["Math", "Physics"]],
    # ["Bob", 30, ["Chemistry", "Biology"]],
    # ["Charlie", 35, ["History", "Geography"]]
                                                    #

data = [['alice', 25, ['math', 'physics']], 
        ['bob', 30, ['chemistry', 'biology']],
        ['charlie', 35, ['history', 'geography']]]

print(data[0][2][1])



# 9 Access and print the first value in the list of numbers associated with "San Francisco".
	# records = [
    # ["New York", [10, 20, 30]],
    # ["San Francisco", [40, 50, 60]],
    # ["Austin", [70, 80, 90]]
                                           # ]

records = [['new york', [10, 20, 30]],
           ['san francisco', [40, 50, 60]],
           ['austin', [70, 80, 90]]              ]




print(records[1][1][0])



# 10 Get the first e in Ayo’s gender and Get Ben’s age.
 	# group = [
#    / ["Ayo", ["Female", 12]],
    # ["Ben", ["Male", 9]]
# ]


group = [['ayo', ['female', 12]],
         ['ben', ['male', 9]]]

print(group[0][1][0][1])


print(group[1][1][1])




# 11 Get the l in Nina’s gender and Get Tobi’s age
	# records = [
    # ["Tobi", ["Male", [6]]],
    # ["Nina", ["Female", [7]]]
                                     #]
 

 
record = [['tobi', ['male', [6]]],
          ['nina', ['female', [7]]]
                                        ]
print(record[0][1][1][0]) 

print(record[1][1][0][-2])



# 12 Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
    # ["R2", ["battery", [98]]],
    # ["R5", ["status", "active"]],
    # ["X1", [["joint", "loose"], "error"]]


