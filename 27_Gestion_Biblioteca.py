class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow_book(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = 'Available' if self.available else 'Borrowed'
        return f'[{status}] "{self.title}" by {self.author}'

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = []
    
    def request_book(self, library, book_title):
        success = library.lend_book(book_title)
        if success:
            self.borrowed_book.append(book_title)
            print(f'Success! {self.name} has borrowed {book_title}.\n')
        else:
            print(f'Sorry, "{book_title}" is not available.\n')

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
    
    def list_catalog(self):
        print('\n--- Library Catalog ---')
        for book in self.catalog:
            print(book)
        print('--------------------------')

    def lend_book(self, book_title):
        for book in self.catalog:
            if book.title == book_title:
                if book.available:
                    book.borrow_book()
                    return True
        return False

def main():
    
    # 1. Create a "Library" object:

    my_library = Library()

    # 2. Create some books:

    book_1 = Book('Calculus', 'Spivak')
    book_2 = Book('Introduction to Algorithms', 'Cormen')

    # 3. Add the books to the catalog:

    my_library.add_book(book_1)
    my_library.add_book(book_2)

    # 4. Create a member:

    student = Member('Noemy')

    # 5. Show the initial catalog:

    my_library.list_catalog()

    # 6. The student requests a book:

    student.request_book(my_library, 'Calculus')

    # 7.  Again, show the catalog:

    my_library.list_catalog()

    # 8. The student is trying to get the same book again:

    student.request_book(my_library, 'Calculus')

if __name__ == '__main__':
    main()