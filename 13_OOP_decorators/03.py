# Sprawdźmy czy dzień nie wypada w oficjalne święto, wystarczy nam moduł holidays

import datetime
from holidays import Poland

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

  @classmethod
  def set_new_grades(cls, new_value):
    cls.grades = new_value

  @staticmethod
  def get_salary_net_under_26(salary):
      if salary < 85000:
          return salary
      else:
          return 8500 - (salary - 85000) * 0.17

  @staticmethod
  def is_academic_day(day):
      is_weekday = day.weekday() in [5,6]

      free_day_pl = Poland()
      is_free_day = day in free_day_pl

      return not is_weekday and not  is_free_day


obj_anna = Student('anna', 'kowalska', 4.72)
obj_michal = Student('michal', 'nowak', 4.69)

obj_michal.grand_scholarship()

obj_michal.set_new_avg(4.5)
obj_michal.grand_scholarship()

print(obj_anna.min_avg)
print(obj_michal.min_avg)
print('**')
Student.set_new_avg(4.1)
print(obj_anna.min_avg)
print(obj_michal.min_avg)


Student.grades= [2,4,3,5]
Student.set_new_grades([4,4,4,3])
print(Student.grades)

annual_salary = obj_michal.get_salary_net_under_26(4300 * 12)
print(annual_salary)


today = datetime.date.today()
print(today, today.weekday())
print('Czy dzisiaj idziemy na uczelnie?', obj_michal.is_academic_day(today))
