students = {"Smith": 85, "Jhonson": 92, "Chmiel": 97, "Bukowski": 73, "Snopek": 88, "Steliha": 100, "Anderson": 89, "Koshy": 83, "Lewandowski": 98, "Olise": 91}
total = 0
print("Students Name", "Grade")
for name in students:
  print(name, students[name])
  total = total + students[name]
average = total / len(students)
print("Class Average:", average)
