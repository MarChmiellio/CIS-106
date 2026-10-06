def display_names(names, scores):
  print("Names and Exam Scores:")
  for i in range(len(names)):
    print("%s %s" % (names[i], scores[i]))
def display_highest(names, scores):
  high_var = 0
  high_index = 0
  for i in range(len(scores)):
    if scores[i] > high_var:
      high_var = scores[i]
      high_index = i
  print("\nHighest Score:")
  print("%s %s" % (names[high_index], high_var))
def display_lowest(names, scores):
  low_var = scores[0]
  low_index = 0
  for i in range(len(scores)):
    if scores [i] < low_var:
      low_var = scores[i]
      low_index = i
  print("\nLowest Score:")
  print("%s %s" % (names[low_index], low_var))
last_names = ["Smith", "Jhonson", "Chmiel", "Bukowski", "Snopek", "Steliha", "Anderson", "Koshy", "Lewandowski", "Olise"]
exam_scores = [85, 92, 97, 73, 88, 100, 89, 83, 98, 91]
display_names(last_names, exam_scores)
display_highest(last_names, exam_scores)
display_lowest(last_names, exam_scores)

  
