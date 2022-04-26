class Student:
    university = 'university'
    min_avg = 4.7

    def __init__(self, name, last, grades):
        self.name = name
        self.last = last
        self.grades = grades

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return f'{self.last}.{self.name}@university.com'

    def grand_scholarship(self):
        if self.grades > self.min_avg:
            print("You get scholarship")
        else:
            print("Not this time")

    @classmethod
    def set_new_avg(cls, new_value):
        cls.min_avg = new_value



obj_anna = Student('anna', 'kowalska', 4.72)
obj_michal = Student('michal', 'nowak', 4.69)

obj_michal.grand_scholarship()

obj_michal.set_new_avg(4.5)
obj_michal.grand_scholarship()

print(obj_anna.min_avg)
print(obj_michal.min_avg)
print('****')
Student.set_new_avg(4.1)
print(obj_anna.min_avg)
print(obj_michal.min_avg)