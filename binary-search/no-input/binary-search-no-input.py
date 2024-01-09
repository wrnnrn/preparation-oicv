from time import time
t_i = time()

list_ = ['1', '2', '3', '4', '5', '6']

number = input("The number to find (1 to 6): ")
if number in list_:
    print("Are the number")
else:
    print("Here is not the number")
