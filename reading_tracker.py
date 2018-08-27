"""
Lucy Smith
22.08.2018
BRIEF PROGRAM DETAILS:
Link to program on Github
"""

MENU = """Menu:
    L - List all books
    A - Add new book
    Q - Quit"""

def main():
    books = open("books.csv", "r")

    print("Reading Tracker 1.0 - by Lucy Smith")

    book_count = 0
    '''counts total number of books'''
    for book in books:
        book_count = book_count + 1
    print("{} books loaded from books.csv".format(book_count))

    menu_choice = "B"
    while menu_choice != "Q":

        print(MENU)
        menu_choice = input(">>>").upper()

        if menu_choice == "L":
            page_count = list_books(books)
            print("You need to read {} pages in {} books.".format(page_count, book_count))
            print("{} books.".format(book_count))

        elif menu_choice == "A":
            add_book()

        elif menu_choice != "Q":
            print("Invalid menu choice")

        elif menu_choice == "Q":
            print("{} books saved to books.csv")
            print("Have a nice day!")


def list_books(books):
    page_count = 0

    for line_str in books:
        print(line_str.strip())

        """counts number of pages """
        fields = line_str.split(',')
        page_count += int(fields[-2])

    books.close()

    return page_count


def add_book():
    books = open("books.csv", "a+")
    error_message = "Input can not be blank"

    book_title = input("Title: ").title()
    while len(book_title) == 0:
        print(error_message)
        book_title = input("Title: ").title()

    book_author = input("Author: ").title()
    while len(book_author) == 0:
        print(error_message)
        book_author = input("Author: ").title()

    page_number = input("Pages: ")
    while page_number == "" or page_number.isalpha() == True:
        print("Invalid input; enter a valid number")
        page_number = input("Pages: ")

    try:
        while int(page_number) <= 0:
            print("Number must be > 0")
            page_number = input("Pages: ")

    except ValueError:
        print("Number must be > 0")
        page_number = input("Pages: ")

    books.write("\n{}, {}, {}, r".format(book_author, book_title, page_number))
    print("{} by {}, ({} pages) added to Reading Tracker".format(book_title, book_author, page_number))
    books.close()

    pass

main()