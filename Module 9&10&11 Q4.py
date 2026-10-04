def compute_total(msrp, make, model, electric_code):
  if electric_code == "Y":
    percent_off = 0.30
  elif make == "Honda" and model == "Accord":
    percent_off = 0.10
  elif make == "Toyota" and model == "Rav4":
    percent_off = 0.15
  else:
    percent_off = 0.05
  discount = msrp * percent_off
  new_msrp = msrp - discount
  tax = new_msrp * 0.07
  total = new_msrp + tax
  return total
total_msrp = 0
total_sales_price = 0
answer = input)"Do you want to enter a vehicle? Yes or No: ")
while answer == "Yes":
  make = input"Enter make: ")
  model = input("Enter model: ")
  electric_code = input("Is it electric? Y or N: ")
  msrp = float(input("Enter MSRP: "))
  sales_price = compute_total(msrp, make, model, electric_code)
  print("Make:", make)
  print("Model:", model)
  print("Out the Door Price: $", sales_price
  answer = input("Do you want to enter another vehicle? Yes or No: ")
print("Total MSRP of all vehicles: $", total_msrp)
print("total Sales Price of all vehicles: $", total_sales_price)
