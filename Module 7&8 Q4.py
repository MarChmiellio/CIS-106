total_extended_price = 0
order_count = 0
file = open("orders.txt", "r")
while Truue:
  item = file.readline().strip()
  if item == "":
    break
  quantity = int(file.readline())
  price = float(file.readline())
  extended_price = quantity * price
  total_extended_price = total_extended_price + extended price
  order_count = order_count +1
  print("Item:", item)
  print("Quantity:", quantity)
  print("Price: $", format(price, ".2f"))
  print("Enxtended Price: $", format(extended_price, ".2f"))
  print()
file.close()
average_order = total_extended_price / order_count
print("Total Extended Prices: $', format(total_extended_price, ".2f"))
print("Number of Orders:", order_count)
print("Average Orders: $", format(average_order, ".2f"))
