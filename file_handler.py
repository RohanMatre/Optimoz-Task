import csv

def save_expenses(expenses, file_path="data/expenses.csv"):
    """Save all expenses to a CSV file."""
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
            writer.writeheader()
            writer.writerows(expenses)
        print("Expenses saved successfully!")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses(file_path="data/expenses.csv"):
    """Load expenses from a CSV file."""
    try:
        expenses = []
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])  # Convert amount back to float
                expenses.append(row)
        print("Expenses loaded successfully!")
        return expenses
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.")
        return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []