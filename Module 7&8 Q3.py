total_bonus = 0
file = open("emplyees.txt", "r")
while True:
  last_name = file.readline().strip()
  if last_name == "":
    break
  salary = float(file.readline())
  if salary>= 100000:
    bonus_rate = 0.20
  elif salary >+ 50000:
    bonus_rate = 0.15
  else:
    bonus_rate = 0.10
  bonus = salary * bonus_rate
  total_bonus = total_bonus + bonus
  print("Employee:", last_name)
  print("Salary: $", format(salary, ".2f"))
  print("Bonus: $", format(bonus, ".2f"))
file.close()
