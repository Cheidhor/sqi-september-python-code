# class Car:
#     def __init__(self, brand, make_year):
#         print('car brand:', brand)
#         print('year made:', make_year)

# car1 = Car('benz', 1990)
# car2 = Car('lexux', 2000) 





# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2

#     def distance(self):
#         result = ((self.x2 - self.x1) + (self.y2 - self.y1))**0.5
#         return result

#     def slope(self):
#         result = (self.y2 - self.y1)/(self.x2 - self.x1)
#         return result

        
# line1 = Line((2, 4), (3, 6))
# line2 = Line((5, 7), (9, 2))
# print(line1.distance())
# print(line1.slope())
# print(line2.slope())
# print(line2.distance())



# # inheritance , polymorphism , abstraction


# class Artist:
#     def create(self):
#         print("Painting!")

# class Musician:
#     def create(self):
#         print("Composing music!")

# cl\ass Writer:
#     def create(self):
#         print("Writing a book!")


# # a = Artist(self)




# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


