# Probelm 3: Student Exam Points
# This program asks for the students last name, midterm score, and final exam score.
#The midterm is worth 40% and the final is worth 60%.

last_name = input("Enter the student's last name: ")
midterm = float(input("Enter the midterm score: "))
final_exam = float(input("Enter the final exam score: "))

total_exam_points = (midterm * .40) + (final_exam * 0.60)
