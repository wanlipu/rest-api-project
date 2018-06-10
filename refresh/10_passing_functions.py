

def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


print (methodception(add_two_numbers))
print (methodception(lambda: 35+77))

my_list = [13, 56, 77, 484]
# my_list.remove(56)
# my_list.remove(484)
print (my_list)

print (list(filter(lambda x: x!=13, my_list)))
print (filter(lambda x: x!=13, my_list))
print ([x for x in my_list if x!= 13])



print ((lambda x:x*3)(5))

print (list(map(lambda x: x!=13, my_list)))
print (list(map(lambda x: x+13, my_list)))

import functools
print (functools.reduce((lambda x, y: x+y), my_list))


