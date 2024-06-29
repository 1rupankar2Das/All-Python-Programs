# Build a program that keeps track of stock prices. Use a dictionary to 
# store stock symbols as keys and their corresponding prices as values. 
# Implement functionalities to add new stocks, update prices, and 
# display the current prices for all stocks.
def display_menu():
    print("\nStock Price Manager")
    print("1. Add New Stock")
    print("2. Update Stock Price")
    print("3. Display All Stock Prices")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_stock(stocks):
    symbol = input("Enter stock symbol: ").upper()
    if symbol in stocks:
        print("Stock already exists.")
    else:
        try:
            price = float(input("Enter stock price: "))
            stocks[symbol] = price
            print(f"Stock {symbol} added successfully with price {price}.")
        except ValueError:
            print("Invalid price. Please enter a numeric value.")

def update_stock_price(stocks):
    symbol = input("Enter stock symbol to update: ").upper()
    if symbol in stocks:
        try:
            price = float(input("Enter new stock price: "))
            stocks[symbol] = price
            print(f"Stock {symbol} updated successfully to price {price}.")
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
    else:
        print("Stock not found.")

def display_stock_prices(stocks):
    if stocks:
        print("\nCurrent Stock Prices:")
        for symbol, price in stocks.items():
            print(f"Symbol: {symbol}, Price: {price}")
    else:
        print("No stocks available.")

def main():
    stocks = {}
    while True:
        choice = display_menu()
        if choice == '1':
            add_stock(stocks)
        elif choice == '2':
            update_stock_price(stocks)
        elif choice == '3':
            display_stock_prices(stocks)
        elif choice == '4':
            print("Exiting the Stock Price Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

