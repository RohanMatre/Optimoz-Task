from expense_tracker import add_expense, view_expenses
from budget_manager import set_budget, track_budget
from file_handler import save_expenses, load_expenses

def main():
    expenses = load_expenses()
    budget = 0

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            if budget == 0:
                budget = set_budget()
            track_budget(expenses, budget)
        elif choice == "4":
            save_expenses(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()