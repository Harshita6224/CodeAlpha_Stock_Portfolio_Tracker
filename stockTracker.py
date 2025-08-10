# ---------------------------
# Stock Portfolio Tracker
# ---------------------------
import csv

# 1. Hardcoded dictionary for stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 130,
    "MSFT": 330
}

portfolio = {}  # To store stock and quantity
total_value = 0

# 2. Display welcome message & available stocks
print("📊 Welcome to Stock Portfolio Tracker")
print("Available stocks & prices:")
for stock, price in stock_prices.items():
    print(f"  {stock} : ${price}")

# 3. Take user input for stocks
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("❌ Please enter a valid number for quantity.")
        continue

    # Add quantity to portfolio (if stock already exists, add to existing qty)
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# 4. Calculate total investment value
print("\n📈 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_value += investment
    print(f"{stock} - {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_value}")

# 5. Ask if user wants to save to a file
save_option = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save_option == "yes":
    # Save to TXT file
    txt_filename = "portfolio_report.txt"
    with open(txt_filename, "w") as f:
        f.write("Stock Portfolio Report\n")
        f.write("=====================\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            f.write(f"{stock} - {qty} shares × ${price} = ${investment}\n")
        f.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Report saved to {txt_filename}")

    # Save to CSV file
    csv_filename = "portfolio_report.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Stock", "Quantity", "Price", "Investment Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            writer.writerow([stock, qty, price, investment])
        writer.writerow(["", "", "Total", total_value])
    print(f"✅ Report saved to {csv_filename}")

print("\n🎯 Tracking Complete. Thank you for using the Stock Portfolio Tracker!")
