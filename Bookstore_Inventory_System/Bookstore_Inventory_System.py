from inventory import Inventory

def display_menu():
    print("\nBookstore Inventory System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Search Books")
    print("4. List All Books")
    print("5. Exit")

def add_book(inventory):
    print("\nAdd New Book")
    title = input("Title: ")
    author = input("Author: ")
    price = input("Price: ")
    stock = input("Stock: ")
    
    try:
        if inventory.add_book(title, author, price, stock):
            print(f"Book '{title}' added successfully!")
    except ValueError:
        print("Invalid input! Please enter valid price and stock.")

def update_book(inventory):
    print("\nUpdate Book")
    title = input("Enter book title to update: ")
    
    print("Leave blank to keep current value")
    author = input(f"New author [{inventory.books[title].author if title in inventory.books else 'N/A'}]: ") or None
    price = input(f"New price [{inventory.books[title].price if title in inventory.books else 'N/A'}]: ") or None
    stock = input(f"New stock [{inventory.books[title].stock if title in inventory.books else 'N/A'}]: ") or None
    
    try:
        if inventory.update_book(title, author, price, stock):
            print(f"Book '{title}' updated successfully!")
    except ValueError:
        print("Invalid input! Please enter valid price and stock.")
    except KeyError:
        print("Book not found!")

def search_books(inventory):
    print("\nSearch Books")
    query = input("Enter search term (title or author): ")
    results = inventory.search_books(query)
    
    if results:
        print("\nSearch Results:")
        print("-" * 60)
        print(f"{'Title':<30} | {'Author':<20} | {'Price':>6} | {'Stock':>5}")
        print("-" * 60)
        for book in results:
            print(f"{book.title:<30} | {book.author:<20} | ${book.price:>5.2f} | {book.stock:>5}")
    else:
        print("No books found matching your search.")

def list_books(inventory):
    books = inventory.list_books()
    if not books:
        print("No books in inventory.")
        return
    
    print("\nCurrent Inventory:")
    print("-" * 60)
    print(f"{'Title':<30} | {'Author':<20} | {'Price':>6} | {'Stock':>5}")
    print("-" * 60)
    for book in books:
        print(f"{book.title:<30} | {book.author:<20} | ${book.price:>5.2f} | {book.stock:>5}")

def main():
    inventory = Inventory()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_book(inventory)
        elif choice == '2':
            update_book(inventory)
        elif choice == '3':
            search_books(inventory)
        elif choice == '4':
            list_books(inventory)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
main()