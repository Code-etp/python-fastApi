import json
import os
import math

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(float(price), 2) 
        self.stock = int(stock)

class Inventory:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self._load_books()
    
    def _load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return {book['title']: Book(**book) for book in data}
        return {}
    
    def save_books(self):
        books_data = [{
            'title': book.title,
            'author': book.author,
            'price': book.price,
            'stock': book.stock
        } for book in self.books.values()]
        
        with open(self.filename, 'w') as f:
            json.dump(books_data, f, indent=2)
    
    def add_book(self, title, author, price, stock):
        if title in self.books:
            print("Book already exists in inventory!")
            return False
        
        self.books[title] = Book(title, author, price, stock)
        self.save_books()
        return True
    
    def update_book(self, title, author=None, price=None, stock=None):
        if title not in self.books:
            print("Book not found in inventory!")
            return False
        
        book = self.books[title]
        if author: book.author = author
        if price: book.price = round(float(price), 2)
        if stock: book.stock = int(stock)
        
        self.save_books()
        return True
    
    def search_books(self, query):
        query = query.lower()
        results = []
        for book in self.books.values():
            if (query in book.title.lower() or 
                query in book.author.lower()):
                results.append(book)
        return results
    
    def list_books(self):
        return list(self.books.values())