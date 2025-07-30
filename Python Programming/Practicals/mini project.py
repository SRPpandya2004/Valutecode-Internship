
"""
A simple expense tracker that lets users:
- Add expenses (amount, category, date)
- View summaries (by category, overall, over time)
- Persist data to a JSON file between runs
- (Bonus) Edit or delete existing expenses
- (Bonus) Plot category breakdown using matplotlib
"""

import json
import os
from datetime import datetime, date
from collections import defaultdict


DATA_FILE = "expenses.json"


def load_data(file_path=DATA_FILE):
    
    #Load expenses from a JSON file. Returns a list of expense dicts.
    
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return json.load(f)


def save_data(expenses, file_path=DATA_FILE):
    
    #Save the list of expense dicts to a JSON file.
    
    with open(file_path, "w") as f:
        json.dump(expenses, f, indent=2, default=str)


def prompt_date():

    #Ask the user for a date string in YYYY-MM-DD format.
    #Default to today if blank or invalid.
 
    inp = input("Enter date (YYYY-MM-DD) [default today]: ").strip()
    if not inp:
        return date.today().isoformat()
    try:
        dt = datetime.strptime(inp, "%Y-%m-%d")
        return dt.date().isoformat()
    except ValueError:
        print("Invalid date format, using today.")
        return date.today().isoformat()


def add_expense(expenses):
    
    #Prompt the user for expense details and append to expenses list.
    
    while True:
        amt = input("Amount (e.g. 50.75): ").strip()
        try:
            amt_val = float(amt)
            break
        except ValueError:
            print("Please enter a valid number.")

    cat = input("Category (e.g. Food, Transport): ").strip() or "Uncategorized"
    dt = prompt_date()

    expense = {
        "amount": amt_val,
        "category": cat,
        "date": dt
    }
    expenses.append(expense)
    save_data(expenses)
    print("Expense added!\n")


def view_overall_summary(expenses):
    
    #Print the total spending across all expenses.
    
    total = sum(e["amount"] for e in expenses)
    print(f"Total spending: ${total:.2f}\n")


def view_category_summary(expenses):
    
    #Ask for a category and show total spending in it.
    
    categories = sorted({e["category"] for e in expenses})
    if not categories:
        print("No expenses recorded yet.\n")
        return

    print("Existing categories:")
    for c in categories:
        print(" -", c)
    chosen = input("Which category? ").strip()

    total = sum(e["amount"] for e in expenses if e["category"].lower() == chosen.lower())
    print(f"Total in '{chosen}': ${total:.2f}\n")


def view_time_summary(expenses):
    
    #show spending grouped by day, week, or month.
    
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    choice = input("Group by [D]ay, [W]eek, [M]onth? ").strip().lower()
    grouping = defaultdict(float)

    for e in expenses:
        dt = datetime.fromisoformat(e["date"])
        if choice == "w":
            key = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
        elif choice == "m":
            key = dt.strftime("%Y-%m")
        else:
            key = dt.strftime("%Y-%m-%d")
        grouping[key] += e["amount"]

    print("\nSpending over time:")
    for period, amt in sorted(grouping.items()):
        print(f"{period}: ${amt:.2f}")
    print()


def delete_expense(expenses):
    
    #List existing expenses with indices, let the user delete one.
    
    if not expenses:
        print("No expenses to delete.\n")
        return

    print("Expenses:")
    for idx, e in enumerate(expenses, 1):
        print(f"{idx}. {e['date']} - {e['category']} - ${e['amount']:.2f}")

    try:
        to_remove = int(input("Enter number to delete (0 to cancel): "))
        if 1 <= to_remove <= len(expenses):
            removed = expenses.pop(to_remove - 1)
            save_data(expenses)
            print(f"Removed {removed}\n")
        else:
            print("Canceled.\n")
    except ValueError:
        print("Invalid.\n")


def edit_expense(expenses):
    
    #List existing expenses, let user pick one to edit fields.
    
    if not expenses:
        print("No expenses to edit.\n")
        return

    print("Expenses:")
    for idx, e in enumerate(expenses, 1):
        print(f"{idx}. {e['date']} - {e['category']} - ${e['amount']:.2f}")

    try:
        sel = int(input("Enter number to edit (0 to cancel): "))
        if 1 <= sel <= len(expenses):
            e = expenses[sel - 1]
            print("Leave blank to keep current value.")
            new_amt = input(f"Amount [{e['amount']}]: ").strip()
            if new_amt:
                e["amount"] = float(new_amt)
            new_cat = input(f"Category [{e['category']}]: ").strip()
            if new_cat:
                e["category"] = new_cat
            new_date = input(f"Date [{e['date']}]: ").strip()
            if new_date:
                try:
                    datetime.fromisoformat(new_date)
                    e["date"] = new_date
                except ValueError:
                    print("Invalid date, keeping old.")
            save_data(expenses)
            print("Expense updated!\n")
        else:
            print("Canceled.\n")
    except ValueError:
        print("Invalid.\n")



def main_menu():
    
    #Display the menu and route user's choice.
    
    expenses = load_data()

    menu = """
Please choose:
1. Add an expense
2. View total spending
3. View spending by category
4. View spending over time
5. Delete an expense
6. Edit an expense
7. Exit
> """
    while True:
        choice = input(menu).strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_overall_summary(expenses)
        elif choice == "3":
            view_category_summary(expenses)
        elif choice == "4":
            view_time_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            edit_expense(expenses)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()



# __________________________________________________

# expences.json
# 
# [
#   {
#     "amount": 85.0,
#     "category": "food",
#     "date": "2025-07-30"
#   },
#   {
#     "amount": 85.0,
#     "category": "1",
#     "date": "2025-07-30"
#   },
#   {
#     "amount": 850.0,
#     "category": "food",
#     "date": "2025-07-30"
#   },
#   {
#     "amount": 200.0,
#     "category": "food",
#     "date": "2025-07-30"
#   },
#   {
#     "amount": 52.0,
#     "category": "4",
#     "date": "2025-07-30"
#   }
# ]