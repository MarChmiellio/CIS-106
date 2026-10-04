def compute_scores(exam1, exam2, exam3):
  total_points = exam1 + exam2 +exam3
  average = total_points / 3
  return total_points, average
last_name = input("Enter student's last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))
total_points, average = compute_scores(exam1, exam2, exam3)
print("Last Name:", last_name)
print("Total Points:", total_points)
print("Average Exam Score:", average)
