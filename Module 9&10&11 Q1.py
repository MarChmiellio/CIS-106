def compute_extended_price(quantity, unit_price):
  extended_price = quantity * unit_price
  if extended_price > 10000:
    extended_price = extended_price * 0.90
  return extended_price
total_ext_price = 0
answer = input("Do you want to enter an item? Enter yes or no: ")
while answer == "yes":
  quantity = int(input("Enter quantity: "))
  unit_price = float(input("Enter unit price: "))
  extended_price = compute_extended_price(quantity, unit_price)
  print("Quantity:", quantity)
  print("Unit Price: $", unit_price)
  print("Extended Price: $", extended_price)
  total_ext_price = total_ext_price + extended_price
  answer = input("Do you want to enter another item? Enter yes or no: ")
print("Total Extended Price:  $", total_ext_price)
