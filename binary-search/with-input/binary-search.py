list_ = input("List: ")
list_listed = list_.split()
print("The list is", list_listed)

number = input("The number to find: ")
if number in list_listed:
    print("Are the number")
else:
    print("Here is not the number")
