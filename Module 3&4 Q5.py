# Problem 5: Stock gain or loss
# This program asks for the original purchase price per share, the current stock price, and the number of shares owned.
# Calculates how much the investement has increased or decreased.

purchase_price = float(input("Enter the purchase price per share: $"))
current_price = float(input("Enter the current stock price per share: $"))
quantity = int(input("Enter the number of shares: "))

gain_or_loss = (current_price - purchase_price) * quantity

print(f"Increase/decrease in stock value: ${gain_or_loss:.2f}")
