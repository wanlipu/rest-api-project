def my_method(arg1, arg2):
    return arg1 + arg2


print (my_method(5, 6))


def my_method2(*args):
    return sum(args)

print (my_method2(1, 2, 3, 4, 5, 6))


def what_are_kwargs(*args, **kwargs):
    print (args)
    print (kwargs)


what_are_kwargs(12, 34, 56, name = "Jose", location = "UK")


def what_are_kwargs(name, location):
    print (name)
    print (location)


what_are_kwargs(location = "UK", name = "Jose")


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    def go_to_school(self):
        print ("I'm going to {}.".format(self.school))

    @classmethod
    def friend(cls, origin, friend_name, **kwargs):
        # return a new Student called "friend_name" in the same school as self
        return cls(friend_name, origin.school, **kwargs)


anna = Student("Anna", "Oxford")
friend = Student.friend(anna, "Greg")

print (friend.name, friend.school)


##


class WorkingStudent(Student):
    def __init__(self, name, school, salary, title):
        super().__init__(name, school)
        self.salary = salary
        self.title = title

    # @classmethod
    # def friend(cls, origin, friend_name, salary):
    #     # return a new Student called "friend_name" in the same school as self
    #     return WorkingStudent(friend_name, origin.school, salary)


anna = WorkingStudent("Anna", "Oxford", salary=20.00, title = "pro")
print (anna.salary)

friend = WorkingStudent.friend(anna, "Greg", salary = 17.5, title = "student")

print (friend.name, friend.school, friend.salary, friend.title)
