def  compute_discount(quantity, price, discount_rate):
  extended_price = quantity * price
  discount_amount = extended_price * discounted_rate
  discounted_price = extended_price - discount_amount
  return discount_amount, discounted_price
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate as a decimal: "))
discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)
print("Quantity:", quantity)
print("Price: $", price)
print("Discount Amount: $", discount_amount)
print("Discounted Price: $", discounted_price)
