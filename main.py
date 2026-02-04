import csv
import datetime
import analysis
from expense import Expense

def add_expense():
    """
    Prompts user for expense details and returns an Expense object.
    Includes validation for date and amount.
    """
    print("\n--- Add New Expense ---")
    
    # Date Validation
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Amount Validation
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    category = input("Enter category: ")
    note = input("Enter note: ")

    expense = Expense(date, amount, category, note)
    return expense

def save_expense(expense):
    """
    Appends an Expense object to the CSV file.
    """
    with open("data/expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            expense.date,
            expense.amount,
            expense.category,
            expense.note
        ])

def load_expenses():
    """
    Reads expenses from CSV file.

    Returns:
        list: A list of dictionaries representing expenses.
    """
    expenses = []
    # Check if file exists to avoid error on first run if empty/missing
    try:
        with open("data/expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert amount back to float for consistency
                # Note: CSV stores everything as strings
                # We can store raw dicts as per Day 2 instructions
                # or convert to Expense objects. Instructions say:
                # "expenses.append(row)" implying dicts.
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses


def menu():
    """
    Displays the main menu options.
    """
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    print("4. View Analysis")
    print("5. Visualize Expenses")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose option: ")
        
        if choice == "1":
            try:
                expense = add_expense()
                save_expense(expense)
                print("Expense saved successfully!")
            except Exception as e:
                print(f"Error adding expense: {e}")
        elif choice == "2":
            print("\n--- All Expenses ---")
            expenses = load_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                for ex in expenses:
                    print(f"{ex['date']} | {ex['category']} | ${float(ex['amount']):.2f} | {ex['note']}")
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            analysis.analyze_expenses()
        elif choice == "5":
            analysis.visualize_expenses()
        else:
            print("Invalid choice. Please try again.")
