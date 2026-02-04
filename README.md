# Python Expense Tracker

A simple, command-line interface (CLI) application to track your daily expenses, analyze your spending habits, and visualize data. Built with Python, Pandas, and Matplotlib.

## 🚀 Features

- **Add Expenses**: Record date, amount, category, and notes for each expense.
- **View Expenses**: See a list of all recorded expenses.
- **Data Persistence**: All data is saved to a CSV file (`data/expenses.csv`), so you never lose your records.
- **Analysis**: View total spending and a breakdown of spending by category.
- **Visualization**: Generate a bar chart to visually compare category spending.
- **Input Validation**: Ensures valid dates and positive dollar amounts.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10 or higher.

### Installation

1.  **Clone or Download** this repository.
2.  **Navigate** to the project folder:
    ```bash
    cd expense_tracker
    ```
3.  **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv .venv
    ```
4.  **Activate the Virtual Environment**:
    - Windows: `.\.venv\Scripts\activate`
    - Mac/Linux: `source .venv/bin/activate`
5.  **Install Dependencies**:
    ```bash
    pip install pandas matplotlib
    ```

## 📖 Usage

Run the main application file:

```bash
python main.py
```

### Menu Options
1.  **Add Expense**: Follow prompts to enter date (YYYY-MM-DD), amount, category, and note.
2.  **View Expenses**: Lists all saved expenses.
3.  **Exit**: Closes the application.
4.  **View Analysis**: Displays total spent and spending per category in the terminal.
5.  **Visualize Expenses**: Opens a popup window with a bar chart of your spending.

## 📂 Project Structure

```
expense_tracker/
├── main.py          # Entry point and menu logic
├── expense.py       # Expense class definition
├── analysis.py      # Data analysis and visualization logic
├── README.md        # Project documentation
└── data/
    └── expenses.csv # Data storage file
```
