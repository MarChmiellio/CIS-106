sttudent_count = 0
responce = input("Do you want to enter a student? Yes or No: ")
while responce.lower() == "yes":
  last_name = input("Enter student last name: ")
  exam1 = float(input("Enter first exam score: "))
  exam2 = float(input("Enter second exam score: "))
  average = (exam1 + exam2) / 2
  print("Student:", last_name)
  print("Average Exam Score:", average)
  print()
  student_count = student_count + 1
  responce = input("Do you want to enter another student? Yes or No: ")
print("Number of Students:", student_count)
