import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """
    Loads expense data from CSV into a Pandas DataFrame.

    Returns:
        pd.DataFrame: DataFrame containing expenses, or None if file not found/empty.
    """
    try:
        df = pd.read_csv("data/expenses.csv")
        if df.empty:
            return None
        
        # Ensure correct data types
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Drop rows with invalid amounts
        df = df.dropna(subset=['amount'])
        return df
    except FileNotFoundError:
        return None

def analyze_expenses():
    """
    Calculates and prints total spending and spending by category.
    """
    print("\n--- Expense Analysis ---")
    df = load_data()
    if df is None or df.empty:
        print("No data available to analyze or file not found.")
        return

    try:
        # 1. Total Spending
        total_spending = df['amount'].sum()
        print(f"\nTotal Spending: ${total_spending:.2f}")

        # 2. Spending by Category
        print("\nSpending by Category:")
        category_summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
        print(category_summary)
        
        return category_summary 
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

def visualize_expenses():
    """
    Generates and displays a bar chart of spending by category using Matplotlib.
    """
    print("\n--- Visualizing Expenses ---")
    df = load_data()
    if df is None or df.empty:
        print("No data available to visualize.")
        return

    try:
        category_summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
        
        # Plotting
        plt.figure(figsize=(10, 6))
        category_summary.plot(kind="bar", color="skyblue")
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show() # This will block execution until window is closed
        print("Graph displayed.")
        
    except Exception as e:
        print(f"An error occurred during visualization: {e}")

