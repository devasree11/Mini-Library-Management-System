import datetime
import json
import random
import sys
LIBRARY_FILE = "library.json"
library = {}
def load_library():
    global library
    try:
        with open(LIBRARY_FILE, "r") as f:
            library = json.load(f)
    except FileNotFoundError:
        library = {}
def save_library():
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)
def generate_book_id():
    while True:
        book_id = str(random.randint(1000, 9999))
        if book_id not in library:
            return book_id
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = generate_book_id()
    library[book_id] = {
        "title": title,
        "author": author,
        "status": "available",
        "borrower": "",
        "date": ""
    }
    save_library()
    print(f"Book '{title}' added successfully with ID {book_id}.")
    menu()
def borrow_book():
    book_id = input("Enter Book ID to borrow: ")
    if book_id in library:
        if library[book_id]["status"] == "available":
            borrower = input("Enter your name: ")
            library[book_id]["status"] = "borrowed"
            library[book_id]["borrower"] = borrower
            library[book_id]["date"] = str(datetime.date.today())
            save_library()
            print(f"Book '{library[book_id]['title']}' borrowed by {borrower}.")
        else:
            print("Book is already borrowed!")
    else:
        print("Book ID not found.")
    menu()
def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in library:
        if library[book_id]["status"] == "borrowed":
            library[book_id]["status"] = "available"
            library[book_id]["borrower"] = ""
            library[book_id]["date"] = ""
            save_library()
            print(f"Book '{library[book_id]['title']}' returned successfully.")
        else:
            print("This book was not borrowed.")
    else:
        print("Book ID not found.")
    menu()
def show_books():
    print("\nBook Details:")
    print("ID\tTitle\tAuthor\tStatus\tBorrower\tDate")
    print("-"*60)
    for book_id, info in library.items():
        print(f"{book_id}\t{info['title']}\t{info['author']}\t{info['status']}\t{info['borrower']}\t{info['date']}")
    menu()
def search_book():
    keyword = input("Enter keyword to search in book title: ").lower()
    print("\nSearch Results:")
    print("ID\tTitle\tAuthor\tStatus")
    print("-"*50)
    found = False
    for book_id, info in library.items():
        if keyword in info["title"].lower():
            print(f"{book_id}\t{info['title']}\t{info['author']}\t{info['status']}")
            found = True
    if not found:
        print("No books found.")
    menu()
def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id in library:
        confirm = input(f"Are you sure you want to remove '{library[book_id]['title']}'? (y/n): ")
        if confirm.lower() == 'y':
            del library[book_id]
            save_library()
            print("Book removed successfully.")
        else:
            print("Operation cancelled.")
    else:
        print("Book ID not found.")
    menu()
def menu():
    print("\n--- MINI LIBRARY MANAGEMENT ---")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Search Book")
    print("6. Remove Book")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        show_books()
    elif choice == "5":
        search_book()
    elif choice == "6":
        remove_book()
    elif choice == "7":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice!")
        menu()
if __name__ == "__main__":
    load_library()
    menu()
