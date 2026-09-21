tickets = int(input("Enter number of concert tickets: "))
if ticketes >= 25:
  price_per_ticket = 50.00
elif tiickets >= 10:
  price_per_ticket = 60.00
elif tickets >= 5:
  price_per_ticket = 70.00
else:
  price_per_ticket = 75.00
total_cost = tickets * price_per_ticket
print("Number of Tickets:", tickets)
print(f"Price Per Ticket: ${price_per_ticket:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
