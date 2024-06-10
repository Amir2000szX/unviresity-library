from typing import List
import os

class Book:
    count = 1
    def __init__(self, name: str, release_year: int, authors: str):
        self.name = name
        self.release_year = release_year
        self.authors = authors
        self.key = Book.count
        Book.count += 1

class Library:
    def __init__(self, name: str, address: str, start_books: List[Book] = None):
        if start_books is None:
            start_books = []

        self.name = name
        self.address = address
        self.books = start_books
        
        
        
        self.file_path = r"C:\Users\hiva laptop\Desktop\project\library"
        lib_filename = f"lib_{self.name}.txt"
        lib_file_path = os.path.join(self.file_path, lib_filename)
        
        if os.path.exists(lib_file_path):
            print("Library exists")
        else:
            with open(lib_file_path, "w") as libfile:
                for book in self.books:
                    libfile.write(f"{book.name}_{book.release_year}_{book.authors}_{book.key}\n")
    
    def add_new_book(self, book: Book):
        self.books.append(book)
        lib_filename = f"lib_{self.name}.txt"
        lib_file_path = os.path.join(self.file_path, lib_filename)
        
        with open(lib_file_path, "a") as libfile:
            libfile.write(f"{book.name}_{book.release_year}_{book.authors}_{book.key}\n")

