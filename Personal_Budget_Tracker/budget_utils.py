import json
import os
from datetime import datetime

class Transaction:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = float(amount)
    
    def to_dict(self):
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount
        }

class BudgetTracker:
    def __init__(self, filename='transactions.json'):
        self.filename = filename
        self.transactions = self._load_transactions()
    
    def _load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Transaction(**t) for t in data]
        return []
    
    def save_transactions(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=2)
    
    def add_transaction(self, date, category, amount):
        try:
            transaction = Transaction(date, category, amount)
            self.transactions.append(transaction)
            self.save_transactions()
            return True
        except ValueError:
            return False
    
    def get_spending_by_category(self):
        categories = {}
        for transaction in self.transactions:
            if transaction.category in categories:
                categories[transaction.category] += transaction.amount
            else:
                categories[transaction.category] = transaction.amount
        return categories
    
    def get_total_spending(self):
        return sum(t.amount for t in self.transactions)
    
    def get_transactions_by_date_range(self, start_date, end_date):
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        
        return [
            t for t in self.transactions
            if start <= datetime.strptime(t.date, '%Y-%m-%d') <= end
        ]