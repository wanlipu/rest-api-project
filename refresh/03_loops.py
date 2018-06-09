my_variable = "hello"

for char in my_variable: # iterables are strings, lists, sets, tuples, and more
    print (char)

for i in range(len(my_variable)):
    print (my_variable[i])

my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print (number ** 2)

user_wants_number = True
while user_wants_number == True:
    print (10)
    user_input = input("Should we print again? (y/n)")  # python3 OK, might not work for python2
    if user_input == 'n':
        user_wants_number = False