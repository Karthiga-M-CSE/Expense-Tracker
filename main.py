import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    expenses = load_expenses()
    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n--- Your Expenses ---")
    total = 0
    for exp in expenses:
        print(f"{exp['title']} - ₹{exp['amount']}")
        total += exp["amount"]
    print(f"\nTotal Spent: ₹{total}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
