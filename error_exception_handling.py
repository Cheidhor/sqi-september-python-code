# num1 = int(input('enter num1:'))
# num2 = int(input('enter num2:'))

# solution = num1 / num2 

# print(solution)



# while True:
#     if num2 and num1 in 
#     print(num1 / num2)
#     break




# try:
#     def safe_devide(a=5, b=9):
#         return a / b
#     print(safe_devide(9, 0))
# except ZeroDivisionError:
#     print('wrong input, 0 should not be provided')
# except TypeError:
#     print('enter an interger')
# except ValueError:
#     print('invalid value provided')
# except Exception:
#     print('error')
    




class negativenumbererror(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)