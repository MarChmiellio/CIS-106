def display_names(names):
  print("Names:")
  for i in range(len(names)):
    print(names[i])
def display_reverse(names):
  print("\nNames in reverse order:")
  for i in range(len(names) -1, -1, -1):
    print(names[i])   
last_names = ["Smith", "Jhonson", "Chmiel", "Bukowski", "Snopek", "Steliha", "Anderson", "Koshy", "Lewandowski", "Olise"]
display_names(last_names)
display_reverse(last_names)
