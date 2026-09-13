# Problem 2: Stock Investment
# This program asks for a stock ticker symbol, the number of shares, and cost per share.
# It then calculates the total amount invested.

ticker = input("Enter the stock ticker symbol: ")
shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: $"))

amount_invested = shares * cost_per_share

print(f"Stock ticker: {ticker}")
print(f"Amount invested: ${amount_invested:.2f}")
