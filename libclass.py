from typing import List
import os 
class Book:
    count = 1
    def __init__(self, name: str, release_year: int, authors: str):
        self.name = name
        self.release_year = release_year
        self.authors = authors
        self.key = Book.count
        Book.count +=1
class Library:
    Liblist = []
    def __init__(self, name: str, address: str, start_books: List[Book]=[]):
        self.name = name
        self.address = address
        self.books = start_books
        
        Library.Liblist.append((self.name,self.address))
        
        self.file_path = f"C:/Users/hiva laptop/Desktop/project/library/lib_{self.name}.txt"
        libraries = os.listdir(self.file_path)
        for nameFile in libraries :
            if f"lib_{self.name}.txt" == nameFile:
                print("library exists")
                break
            else:
                with open(self.file_path, "w+") as libfile:
                    for book in self.books:
                        libfile.write(f"{book.name}_{book.release_year}_{book.authors}_{book.key}\n")

    def add_new_book(self, book: Book):
        self.books.append(book)
        with open(self.file_path, "a") as libfile:
            libfile.write(f"{self.books[-1].name}_{self.books[-1].release_year}_{self.books[-1].authors}_{self.books[-1].key}\n")



lib1 = Library("azadegan","khabgah")
print(Library.Liblist)