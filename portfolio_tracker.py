#!/usr/bin/env python3
"""
CodeAlpha Python Internship
Task 2: Stock Portfolio Tracker

An interactive tool to track a user's stock portfolio, calculate real-time
investment values based on hardcoded market prices, display summaries, and
export report cards in TXT and CSV formats.
"""

import csv
import os

# Hardcoded catalog of available stocks and their current market prices ($)
STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 420.0,
    "AMZN": 190.0
}

# The user's active portfolio dictionary: {stock_symbol: quantity}
portfolio = {}


def show_stock_catalog():
    """
    Displays the catalog of available stocks and their pre-configured prices.
    """
    print("\n" + "-" * 40)
    print("    AVAILABLE STOCKS & CURRENT PRICES    ")
    print("-" * 40)
    for index, (symbol, price) in enumerate(STOCK_PRICES.items(), 1):
        print(f" {index}. {symbol:<6} : ${price:,.2f}")
    print("-" * 40)


def add_or_update_stock():
    """
    Prompts user for a stock symbol and quantity to add or update in the portfolio.
    Includes input validation.
    """
    show_stock_catalog()
    
    # 1. Input & Validate Stock Symbol
    while True:
        symbol = input("Enter the stock symbol (e.g., AAPL): ").strip().upper()
        if symbol in STOCK_PRICES:
            break
        print(f"Error: '{symbol}' is not in our stock catalog. Please select a valid stock.")

    # 2. Input & Validate Quantity
    while True:
        qty_str = input(f"Enter quantity of {symbol} shares to add/update: ").strip()
        try:
            quantity = int(qty_str)
            if quantity <= 0:
                print("Error: Quantity must be a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Error: Invalid quantity! Please enter a valid whole number.")
            
    # 3. Add to portfolio
    if symbol in portfolio:
        portfolio[symbol] += quantity
        print(f"\nSuccess: Added {quantity} more shares of {symbol}. Total shares now: {portfolio[symbol]}")
    else:
        portfolio[symbol] = quantity
        print(f"\nSuccess: Added {quantity} shares of {symbol} to your portfolio.")


def remove_stock():
    """
    Removes or reduces shares of a stock from the user's active portfolio.
    """
    if not portfolio:
        print("\nYour portfolio is currently empty! Nothing to remove.")
        return

    print("\n" + "-" * 40)
    print("           CURRENT HOLDINGS             ")
    print("-" * 40)
    for symbol, qty in portfolio.items():
        print(f" * {symbol:<5} : {qty} shares")
    print("-" * 40)

    while True:
        symbol = input("Enter the stock symbol to remove/reduce: ").strip().upper()
        if symbol in portfolio:
            break
        print("Error: This stock is not in your current portfolio.")

    # Ask for reduction quantity
    current_shares = portfolio[symbol]
    while True:
        qty_str = input(f"Enter number of shares to remove (Max {current_shares}): ").strip()
        try:
            qty_to_remove = int(qty_str)
            if qty_to_remove <= 0:
                print("Error: Quantity must be positive.")
                continue
            if qty_to_remove > current_shares:
                print(f"Error: You only own {current_shares} shares of {symbol}.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

    if qty_to_remove == current_shares:
        del portfolio[symbol]
        print(f"\nSuccess: Completely removed {symbol} from your portfolio.")
    else:
        portfolio[symbol] -= qty_to_remove
        print(f"\nSuccess: Removed {qty_to_remove} shares. Remaining {symbol} shares: {portfolio[symbol]}")


def calculate_portfolio_summary():
    """
    Calculates details for individual stock holdings and the grand total value.
    Returns:
        holdings_details (list of dicts): Individual holding values.
        grand_total (float): Total portfolio valuation.
    """
    holdings_details = []
    grand_total = 0.0
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        total_value = quantity * price
        grand_total += total_value
        holdings_details.append({
            "Symbol": symbol,
            "Shares": quantity,
            "Price": price,
            "TotalValue": total_value
        })
        
    return holdings_details, grand_total


def display_portfolio():
    """
    Prints a beautiful, formatted breakdown of the portfolio and grand total.
    """
    if not portfolio:
        print("\n" + "=" * 45)
        print("         YOUR PORTFOLIO IS EMPTY             ")
        print("=" * 45)
        return

    holdings, grand_total = calculate_portfolio_summary()
    
    print("\n" + "=" * 55)
    print("               PORTFOLIO VALUE SUMMARY              ")
    print("=" * 55)
    print(f"{'STOCK':<8} | {'SHARES':<10} | {'UNIT PRICE':<12} | {'TOTAL VALUE':<15}")
    print("-" * 55)
    
    for item in holdings:
        print(f"{item['Symbol']:<8} | {item['Shares']:<10} | ${item['Price']:<11,.2f} | ${item['TotalValue']:<14,.2f}")
        
    print("-" * 55)
    print(f"{'GRAND TOTAL INVESTMENT VALUE:':<35} | ${grand_total:,.2f}")
    print("=" * 55 + "\n")


def export_reports():
    """
    Saves portfolio values to both portfolio_report.txt and portfolio_report.csv files.
    """
    if not portfolio:
        print("\nError: Cannot export an empty portfolio. Please add stocks first!")
        return

    holdings, grand_total = calculate_portfolio_summary()
    
    # 1. Export as a Text Report (.txt)
    txt_filename = "portfolio_report.txt"
    try:
        with open(txt_filename, "w", encoding="utf-8") as f:
            f.write("=" * 55 + "\n")
            f.write("           STOCK PORTFOLIO TRACKER REPORT          \n")
            f.write("=" * 55 + "\n")
            f.write(f"{'STOCK':<8} | {'SHARES':<10} | {'UNIT PRICE':<12} | {'TOTAL VALUE':<15}\n")
            f.write("-" * 55 + "\n")
            for item in holdings:
                f.write(f"{item['Symbol']:<8} | {item['Shares']:<10} | ${item['Price']:<11,.2f} | ${item['TotalValue']:<14,.2f}\n")
            f.write("-" * 55 + "\n")
            f.write(f"{'GRAND TOTAL INVESTMENT VALUE:':<35} | ${grand_total:,.2f}\n")
            f.write("=" * 55 + "\n")
            f.write("Report generated successfully.\n")
            
        print(f"\n[+] Text report saved to: {os.path.abspath(txt_filename)}")
    except IOError as e:
        print(f"Error saving Text report: {e}")

    # 2. Export as a CSV Spreadsheet (.csv)
    csv_filename = "portfolio_report.csv"
    try:
        with open(csv_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write headers
            writer.writerow(["Stock Symbol", "Shares Owned", "Price Per Share ($)", "Total Value ($)"])
            # Write individual rows
            for item in holdings:
                writer.writerow([item['Symbol'], item['Shares'], item['Price'], item['TotalValue']])
            # Write total summary
            writer.writerow([])
            writer.writerow(["GRAND TOTAL", "", "", grand_total])
            
        print(f"[+] CSV spreadsheet exported to: {os.path.abspath(csv_filename)}")
    except IOError as e:
        print(f"Error saving CSV report: {e}")


def main():
    """
    Main controller for the interactive Stock Portfolio CLI.
    """
    print("\n" + "=" * 45)
    print("      CODEALPHA STOCK PORTFOLIO TRACKER      ")
    print("=" * 45)
    
    while True:
        print("\n--- Main Menu ---")
        print("1. View Stock Price Catalog")
        print("2. Add/Update Stock in Portfolio")
        print("3. Remove Stock from Portfolio")
        print("4. View Portfolio & Grand Total")
        print("5. Save & Export Report (TXT + CSV)")
        print("6. Exit Program")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            show_stock_catalog()
        elif choice == "2":
            add_or_update_stock()
        elif choice == "3":
            remove_stock()
        elif choice == "4":
            display_portfolio()
        elif choice == "5":
            export_reports()
        elif choice == "6":
            print("\nThank you for using CodeAlpha Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
