total_tuition = 0
student_count = 0
file = open("students.txt", "r")
while True:
  last_name = file.readline().strip()
  if last name == "":
    break
  district_code = file.readline().strip()
  credits = int(file.readline())
  if dostrict code == "I":
    cost_per_credit = 250.00
  else:
    cost_per_credit = 500.00
  tuition = credits * cost_per_credit
  student_count = student_count + 1
  print("Student:", last_name)
  print("Credits Taken:", credits)
  print("Tuition Owed: $", format(tuition, ".2f"))
  print()
file.close()
print("Total Tuition Owed: $", format(total_tuition, ".2f))
print("Number of Students:", student_count)
  
