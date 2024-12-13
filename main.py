from library import Library

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("0. Exit")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Lend Book")
        print("6. Return Book")
        
        choice = input("Choose an option: ")
        
        if choice == '0':
            print("Exiting the program...")
            break
        elif choice == '1':
            title = input("Enter book title: ")
            authors = input("Enter book authors: ")
            publishing_year = input("Enter publishing year: ")
            price = input("Enter book price: ")
            quantity = input("Enter book quantity: ")
            library.add_book(title, authors, int(publishing_year), float(price), int(quantity))
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            isbn = int(input("Enter book ISBN to update: "))
            title = input("Enter new book title (leave empty to keep unchanged): ")
            authors = input("Enter new book authors (leave empty to keep unchanged): ")
            publishing_year = input("Enter new publishing year (leave empty to keep unchanged): ")
            price = input("Enter new book price (leave empty to keep unchanged): ")
            quantity = input("Enter new book quantity (leave empty to keep unchanged): ")
            library.update_book(isbn, title, authors, int(publishing_year) if publishing_year else None, float(price) if price else None, int(quantity) if quantity else None)
        elif choice == '4':
            isbn = int(input("Enter book ISBN to delete: "))
            library.delete_book(isbn)
        elif choice == '5':
            title = input("Enter book title to lend: ")
            borrower_name = input("Enter borrower name: ")
            borrower_phone = input("Enter borrower phone: ")
            library.lend_book(title, borrower_name, borrower_phone)
        elif choice == '6':
            title = input("Enter book title to return: ")
            borrower_name = input("Enter borrower name: ")
            library.return_book(title, borrower_name)
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
