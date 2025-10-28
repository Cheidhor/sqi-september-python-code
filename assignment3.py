# 1 Create a list called fruits with items "apple", "banana", and "orange". Print the first item.

fruits = ['apple', 'banana', 'orange']

print(fruits[0])



# 2  ceate a list called colors with items "red", "green", "blue". Print the last item using 
# negative indexing.

colors = ['red', 'green', 'blue', ]

print(colors[-1])


# 3  Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7
#  (inclusive of index 3, exclusive of 8).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[3:7])



# 4  Create a list called alphabets with items "a", "b", "c", ..., "z".
#  Print a slice from index -3 to the end.
import string 
alphabets = string.ascii_lowercase
print(alphabets[-3:])

# 5 Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.

ages = [20, 30, 40]

ages[1] = 35
print(ages)








