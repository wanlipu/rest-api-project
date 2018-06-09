grades = [77, 80, 90]

print (grades)
print (len(grades))
print (sum(grades))
print (sum(grades)/len(grades))


tuple_grades = (77, 80, 90) # immutable
print (tuple_grades)

set_grades = {77, 80, 90}
print (set_grades)


grades.append(100)
print (grades)

tuple_grades = tuple_grades + (100,) # immutable, but could be reassigned with new value
print (tuple_grades)

set_grades.add(100)
print (set_grades)
set_grades.add(100)
print (set_grades)


print (grades[0])
print (tuple_grades[0])
# print (set_grades[0])   # 'set' object does not support indexing

grades[0] = 60
print (grades)
# tuple_grades[0] = 60 # 'tuple' object does not support item assignment


## advanced set operations
set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print (set_one.intersection(set_two))
print (set_one.union(set_two))
print (set_one.difference(set_two))

print (set_one, set_two)

print (set_one.intersection_update(set_two))
print (set_one, set_two)

print (set_one.difference(set_two))
print (set_two.difference(set_one))




