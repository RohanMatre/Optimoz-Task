def add_expense(expenses):
    """Prompt the user to add an expense and store it in the list."""
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Travel): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        
        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

def view_expenses(expenses):
    """Display all stored expenses."""
    if not expenses:
        print("No expenses to display.")
        return

    print("\nDate\t\tCategory\tAmount\tDescription")
    print("-" * 50)
    for expense in expenses:
        if all(key in expense for key in ["date", "category", "amount", "description"]):
            print(f"{expense['date']}\t{expense['category']}\t{expense['amount']:.2f}\t{expense['description']}")
        else:
            print("Incomplete expense entry found. Skipping...")

