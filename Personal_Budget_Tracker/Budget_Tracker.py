from budget_utils import BudgetTracker
from datetime import datetime

def display_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add Transaction")
    print("2. View Spending by Category")
    print("3. View Total Spending")
    print("4. View Transactions by Date Range")
    print("5. Exit")

def add_transaction(tracker):
    print("\nAdd New Transaction")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    
    if tracker.add_transaction(date, category, amount):
        print("Transaction added successfully!")
    else:
        print("Invalid input! Please enter a valid date and amount.")

def view_spending_by_category(tracker):
    print("\nSpending by Category")
    print("-" * 40)
    print(f"{'Category':<20} | {'Amount':>15}")
    print("-" * 40)
    
    categories = tracker.get_spending_by_category()
    for category, amount in categories.items():
        print(f"{category:<20} | ${amount:>14.2f}")
    
    print("-" * 40)
    print(f"{'Total':<20} | ${tracker.get_total_spending():>14.2f}")

def view_total_spending(tracker):
    print("\nTotal Spending")
    print("-" * 30)
    print(f"Total: ${tracker.get_total_spending():.2f}")

def view_transactions_by_date(tracker):
    print("\nView Transactions by Date Range")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    try:
        transactions = tracker.get_transactions_by_date_range(start_date, end_date)
        print(f"\nTransactions from {start_date} to {end_date}")
        print("-" * 60)
        print(f"{'Date':<12} | {'Category':<20} | {'Amount':>15}")
        print("-" * 60)
        
        for t in transactions:
            print(f"{t.date:<12} | {t.category:<20} | ${t.amount:>14.2f}")
        
        total = sum(t.amount for t in transactions)
        print("-" * 60)
        print(f"{'Total':<34} | ${total:>14.2f}")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")

def main():
    tracker = BudgetTracker()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_transaction(tracker)
        elif choice == '2':
            view_spending_by_category(tracker)
        elif choice == '3':
            view_total_spending(tracker)
        elif choice == '4':
            view_transactions_by_date(tracker)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
main()