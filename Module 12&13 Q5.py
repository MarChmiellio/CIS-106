students = {"Smith": [85, 90, 88], "Jhonson": [92, 89, 94], "Chmiel": [97, 95, 96], "Bukowski": [73, 78, 80], "Snopek": [88, 90, 85], "Steliha": [100, 98, 97], "Anderson": [89, 91, 90], "Koshy": [83, 86, 84], "Lewandowski": [98, 95, 99], "Olise": [91, 89, 93] }
def class_averages(students):
  grade1_total = 0
  grade2_total = 0
  grade3_total = 0
  for name in students:
    grade1_total = grade1_total + students[name][0]
    grade2_total = grade2_total + students[name][1]
    grade3_total = grade3_total + students[name][2]
  grade1_average = grade1_total / float(len(students))
  grade2_average = grade2_total / float(len(students))
  grade3_average = grade3_total / float(len(students))
  averages = [grade1_average, grade2_average, grade3_average]
  return averages
print("Student Name    Average")
print("-----------------------")
for name in students:
  student_average = (students[name][0] + students[name][1] + students[name][2]) / 3.0
  print(name + "   " + str(round(student_average, 2)))
averages = class_averages(students)
print("")
print("Class Grade Averages")
print("--------------------")
print("Grade 1 Average: " + str(round(averages[0], 2)))
print("Grade 2 Average: " + str(round(averages[1], 2)))
print("Grade 3 Average: " + str(round(averages[2], 2)))
