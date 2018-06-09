def my_print_method():
    print("Hello")
    print("World")

my_print_method()

# new function with the same name will overwrite the previous function
def my_print_method(my_argument):
    print(my_argument)

my_print_method("hahaha")


def my_multiply_method(number_one, number_two):
    return number_one * number_two

result = my_multiply_method(5, 3)
print (result)
my_print_method(result)