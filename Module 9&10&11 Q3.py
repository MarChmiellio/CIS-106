def compute_forecast(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    forecast_perecent = 0.10
  elif month == "Apr" or month == "May" or month == "Jun":
    forecast_percent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    forecast_percent = 0.20
  else:
    forecast_percent = 0.25
  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales
answer = input("Do you want to enter sales information? Yes or No: ")
while answer == "Yes":
  last_name = input("Enter last name:")
  month = input("Enter month: ")
  sales = float(input("Enter sales: "))
  forecast = compute_forecast(month, sales)
  print("Last Name:", last_name)
  print("Next Month Sales Forecast: $", forecast)
  answer = input("Do you want to enter another? Yes or No: ")
