class Expense:
    """
    Represents a single expense record.
    """
    def __init__(self, date, amount, category, note):
        """
        Initialize an Expense object.

        Args:
            date (str): The date of the expense (YYYY-MM-DD).
            amount (float): The cost of the expense.
            category (str): The category (e.g., Food, Transport).
            note (str): A brief description.
        """
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note
