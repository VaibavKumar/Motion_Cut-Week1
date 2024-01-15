import json
from datetime import datetime

# Function to get user input for daily expenses
def get_expense_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Briefly describe the expense: ")
    category = input("Enter expense category (food, transportation, entertainment, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"amount": amount, "description": description, "category": category, "date": date}

# Function to store expense data in a JSON file
def save_expense(expense):
    with open("expenses.json", "a") as file:
        json.dump(expense, file)
        file.write('\n')

# Function to categorize and analyze expenses
def analyze_expenses():
    category_wise_expenses = {}
    total_expense = 0

    with open("expenses.json", "r") as file:
        for line in file:
            expense = json.loads(line)
            total_expense += expense["amount"]
            category = expense["category"]

            if category in category_wise_expenses:
                category_wise_expenses[category] += expense["amount"]
            else:
                category_wise_expenses[category] = expense["amount"]

    return total_expense, category_wise_expenses

# Function to display monthly summaries and category-wise expenditure
def show_summary():
    total_expense, category_wise_expenses = analyze_expenses()

    print("\nMonthly Summary:")
    print(f"Total Expense: ${total_expense:.2f}\n")

    print("Category-wise Expenditure:")
    for category, amount in category_wise_expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")

# User interface loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Enter Daily Expense")
    print("2. View Expense Summary")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        expense_data = get_expense_input()
        save_expense(expense_data)
        print("Expense recorded successfully!")

    elif choice == "2":
        show_summary()

    elif choice == "3":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")