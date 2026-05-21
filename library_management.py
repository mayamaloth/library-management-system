import os

FILE_NAME = "library.txt"

# Add Book
def add_book():
    title = input("Enter Book Title: ").strip()

    if title == "":
        print("Book title cannot be empty!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(title + "\n")

    print("Book added successfully!")

# View Books
def view_books():
    if not os.path.exists(FILE_NAME):
        print("No books found!")
        return

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    if len(books) == 0:
        print("Library is empty!")
    else:
        print("\nAvailable Books:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book.strip()}")

# Search Book
def search_book():
    keyword = input("Enter book title to search: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("No records found!")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    for book in books:
        if keyword in book.lower():
            print("Book Found:", book.strip())
            found = True

    if not found:
        print("Book not found!")

# Remove Book
def remove_book():
    title = input("Enter book title to remove: ").strip()

    if not os.path.exists(FILE_NAME):
        print("No records found!")
        return

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    updated_books = []
    found = False

    for book in books:
        if book.strip().lower() != title.lower():
            updated_books.append(book)
        else:
            found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_books)

    if found:
        print("Book removed successfully!")
    else:
        print("Book not found!")

# Main Menu
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            view_books()

        elif choice == 3:
            search_book()

        elif choice == 4:
            remove_book()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select between 1-5.")

    except ValueError:
        print("Please enter a valid number!")