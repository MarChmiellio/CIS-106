def display_names(names, scores):
  print("Names and Exam Scores:")
  for i in range(len(names)):
    print(names[i], scores[i])
def display_reverse(names, scores):
  print("\nNames and Exam Scores in reverse order:")
  for i in range(len(names) -1, -1, -1):
    print(names[i], scores[i])  
last_names = ["Smith", "Jhonson", "Chmiel", "Bukowski", "Snopek", "Steliha", "Anderson",
"Koshy", "Lewandowski", "Olise"]
exam_scores = [85, 92, 97, 73, 88, 100, 89, 83, 98, 91]
display_names(last_names, exam_scores)
display_reverse(last_names, exam_scores)
