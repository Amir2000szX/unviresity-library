from typing import List

class Book:
    count = 1
    def __init__(self, name: str, release_year: int, authors: str):
        self.name = name
        self.release_year = release_year
        self.authors = authors
        self.key = Book.count
        Book.count +=1
class Library:
    
    def __init__(self, name: str, address: str, start_books: List[Book]):
        self.name = name
        self.address = address
        self.__books = start_books
        
        
        self.file_path = f"C:/Users/hiva laptop/Desktop/project/lib_{self.name}.txt"
        with open(self.file_path, "w+") as libfile:
            for book in self.__books:
                libfile.write(f"{book.name}_{book.release_year}_{book.authors}_{book.key}\n")

    def add_new_book(self, book: Book):
        self.__books.append(book)
        with open(self.file_path, "a") as libfile:
            libfile.write(f"{self.__books[-1].name}_{self.__books[-1].release_year}_{self.__books[-1].authors}_{self.__books[-1].key}\n")


book1 = Book("Alchemist", 2019, "David")
book2 = Book("Me Before You", 2020, "Jojo")
markazi = Library("Markazi", "Near the Department of Mathematics", [book1, book2])
