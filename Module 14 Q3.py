class Student:
  def __init__(self, first, last, district, credits):
    self.first = first
    self.last = last
    self.district = district
    self.credits = credits
  def tuition(self):
    rates = {"I": 250, "0": 500, "X": 800, "G": 250}
    total = self.credits * rates[self.district]
    return total
student1 = Student("Michael", "Chmiel", "I", 9)
student2 = Student("Justin", "Snopek", "O", 12)
student3 = Student("Max", "Steliha", "X", 15)
student4 = Student("Peter", "Chmiel", "G", 6)
students = [student1, student2, student3, student4]
for student in students:
  print("First Name:", student.first)
  print("Last Name:", student.last)
  print("District Code:", student.district)
  print("Enrolled Credits:", student.credits)
  print("Tuition Owed:", student.tuition())
  print("\n")
