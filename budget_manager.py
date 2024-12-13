def set_budget():
    """Prompt the user to set a monthly budget."""
    try:
        budget = float(input("Enter your monthly budget: "))
        return budget
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def track_budget(expenses, budget):
    """Track the total expenses against the budget."""
    total_expenses = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: {total_expenses:.2f}")
    if total_expenses > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print(f"You have {budget - total_expenses:.2f} left for the month.")