import csv

# -----------------------------------
# STOCK PRICE DATABASE
# -----------------------------------

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 150
}

current_market_prices = {
    "AAPL": 195,
    "TSLA": 280,
    "GOOG": 150,
    "MSFT": 350,
    "AMZN": 165
}

portfolio = {}

# -----------------------------------
# ADD STOCK
# -----------------------------------

def add_stock():

    symbol = input(
        "\nEnter Stock Symbol: "
    ).upper()

    if symbol not in stock_prices:

        print("Stock not available.")
        return

    try:

        quantity = int(
            input("Enter Quantity: ")
        )

        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        print("Stock Added Successfully!")

    except ValueError:

        print("Invalid quantity.")

# -----------------------------------
# VIEW PORTFOLIO
# -----------------------------------

def view_portfolio():

    if not portfolio:

        print("\nPortfolio Empty.")
        return

    print("\nYOUR PORTFOLIO")
    print("-" * 30)

    for stock, qty in portfolio.items():

        print(
            f"{stock:<10} {qty} shares"
        )

# -----------------------------------
# INVESTMENT VALUE
# -----------------------------------

def investment_value():

    total = 0

    for stock, qty in portfolio.items():

        total += stock_prices[stock] * qty

    print(
        f"\nTotal Investment = ${total}"
    )

# -----------------------------------
# CURRENT VALUE
# -----------------------------------

def current_value():

    total = 0

    for stock, qty in portfolio.items():

        total += current_market_prices[stock] * qty

    print(
        f"\nCurrent Value = ${total}"
    )

# -----------------------------------
# PROFIT LOSS
# -----------------------------------

def profit_loss():

    invested = 0
    current = 0

    for stock, qty in portfolio.items():

        invested += (
            stock_prices[stock] * qty
        )

        current += (
            current_market_prices[stock] * qty
        )

    difference = current - invested

    if difference > 0:

        print(
            f"\nProfit = ${difference}"
        )

    elif difference < 0:

        print(
            f"\nLoss = ${abs(difference)}"
        )

    else:

        print("\nNo Profit No Loss")

# -----------------------------------
# SAVE CSV
# -----------------------------------

def save_portfolio():

    with open(
        "portfolio.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Stock",
            "Quantity"
        ])

        for stock, qty in portfolio.items():

            writer.writerow([
                stock,
                qty
            ])

    print(
        "\nPortfolio Saved Successfully!"
    )

# -----------------------------------
# LOAD CSV
# -----------------------------------

def load_portfolio():

    try:

        with open(
            "portfolio.csv",
            "r"
        ) as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                stock = row[0]
                qty = int(row[1])

                portfolio[stock] = qty

        print(
            "\nPortfolio Loaded Successfully!"
        )

    except FileNotFoundError:

        print(
            "\nNo saved portfolio found."
        )

# -----------------------------------
# MENU
# -----------------------------------

def menu():

    print("\n" + "="*40)
    print("STOCK PORTFOLIO TRACKER")
    print("="*40)

    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Investment Value")
    print("4. Current Value")
    print("5. Profit/Loss")
    print("6. Save Portfolio")
    print("7. Load Portfolio")
    print("8. Exit")

# -----------------------------------
# MAIN
# -----------------------------------

def main():

    while True:

        menu()

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":
            add_stock()

        elif choice == "2":
            view_portfolio()

        elif choice == "3":
            investment_value()

        elif choice == "4":
            current_value()

        elif choice == "5":
            profit_loss()

        elif choice == "6":
            save_portfolio()

        elif choice == "7":
            load_portfolio()

        elif choice == "8":

            print(
                "\nThank You!"
            )
            break

        else:

            print(
                "Invalid Choice."
            )

if __name__ == "__main__":
    main()
