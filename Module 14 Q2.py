class Student:
  def __init__(self, first, last, district, credits):
    self.first = first
    self.last = last
    self.district = district
    self.credits = credits
  def tuition(self):
    if self.district == "I":
      total = self.credits * 250
    else:
      total = self.credits * 500
    return total
first = input("Enter first name: ")
last = input("Enter last name: ")
district = input("Enter district code (I or O): ")
credits = int(input("Enter enrolled credits: "))
#Even though the instructions only called for instantiating the object and adding the data I felt that making an input addition would make it more interactive and better suite the problem
student1 = Student(first, last, district, credits)
print("First Name:", student1.first)
print("Last Name:", student1.last)
print("District Code:", student1.district)
print("Enrolled Credits:", student1.credits)
print("Tuition Owed:", student1.tuition())
