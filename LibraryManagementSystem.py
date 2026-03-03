from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, book_name):
        self.book_name = book_name

    @abstractmethod
    def issue(self):
        pass

class Book(LibraryItem):
    def __init__(self, book_name):
        super().__init__(book_name)

    def issue(self):
        print(f"The book '{self.book_name}' has been issued for 14 days.")

book_name = input("Enter the name of the book: ")
book1 = Book(book_name)
book1.issue()   