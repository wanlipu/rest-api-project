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
    def friend(cls, origin, friend_name):
        # return a new Student called "friend_name" in the same school as self
        return cls(friend_name, origin.school)


anna = Student("Anna", "Oxford")
friend = Student.friend(anna, "Greg")

print (friend.name, friend.school)


##


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @classmethod
    def friend(cls, origin, friend_name, salary):
        # return a new Student called "friend_name" in the same school as self
        return WorkingStudent(friend_name, origin.school, salary)


anna = WorkingStudent("Anna", "Oxford", 20.00)
print (anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 17.5)

print (friend.name, friend.school, friend.salary)
