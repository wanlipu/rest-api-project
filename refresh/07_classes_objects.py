lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

print (lottery_player_dict)


class LotteryPlayer:
    def __init__(self, name = 'Rolf'):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('John')

print (player_one.name, player_one.numbers)
print (player_one.total())

print (player_one == player_two)
print (player_one.name == player_two.name)
print (player_one.numbers == player_two.numbers)

player_one.numbers = (1, 2, 3, 6, 7, 8)
print (player_one.numbers == player_two.numbers)

##


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
    def go_to_school2(cls):
        print("I'm going to school")

    @staticmethod
    def go_to_school3():
        print("I'm going to school, haha")

anna = Student("Anna", "MIT")
anna.marks.append(56)
print (anna.marks)
anna.marks.append(71)
print (anna.average())
anna.go_to_school()
anna.go_to_school2()
anna.go_to_school3()
Student.go_to_school3()

