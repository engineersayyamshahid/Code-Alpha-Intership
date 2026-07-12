# Dictionary of stocks
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170
}

print("📈 Stock Portfolio Tracker")
print("---------------------------")
print("Available Stocks:")

# Display all stocks one by one
for stock in stocks:
    print(stock)

# user enter specific stock and quantity
stock_name = input("\nEnter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))


# Check if stock exists
if stock_name in stocks:
    price = stocks[stock_name]  # stock price
    total = price * quantity  # total investment

    
    print("\n------ Portfolio Summary ------")
    print("Stock Name :", stock_name)
    print("Price      :", price)
    print("Quantity   :", quantity)
    print("Total Value:", total)


    file = open("Stock Portfolio Tracker/portfolio.txt", "w")

    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    file.write(f"Stock Name : {stock_name}\n")
    file.write(f"Price      : {price}\n")
    file.write(f"Quantity   : {quantity}\n")
    file.write(f"Total Value: {total}\n")

    file.close()

    print("\n✅ Data saved in portfolio.txt")

else:
    print("\n❌ Stock not found!")