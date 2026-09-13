# Problem #1 Weighted Exam Scores
# This program asks the user for two exam scores.
# Exam 1 is worth 60% and Exam 2 is worth 40%.

exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))

total_score = (exam1 * 0.60) + (exam2 * 0.40)

print(f"Total weighted exam score: {total_score:.2f}")
