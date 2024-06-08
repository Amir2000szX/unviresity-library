from libclass import *
from tkinter import *
from tkinter.ttk import *
import os
def addLib():
    def library(name: str, address: str, count: IntVar, window: Toplevel):
        lib = Library(name, address)
        file_path = f"C:/Users/hiva laptop/Desktop/project/library/lib_{lib.name}.txt"
        with open(file_path, "w") as libfile:  # Changed to "w" for creating a new file
            addBook(lib.name, count.get(), 0)  # Start adding books with the initial count
        window.destroy()

    new_window = Toplevel(root)
    new_window.title("New Library")
    new_window.geometry("400x200")

    name_var = StringVar()
    address_var = StringVar()
    bookcount = IntVar()

    nameLabel = Label(new_window, text="Name of the Library")
    nameLabel.grid(column=0, row=0, pady=10)
    nameEntry = Entry(new_window, width=40, textvariable=name_var)
    nameEntry.grid(column=1, row=0, pady=10)

    addressLabel = Label(new_window, text="Address of the Library")
    addressLabel.grid(column=0, row=2, pady=10)
    addressEntry = Entry(new_window, width=40, textvariable=address_var)
    addressEntry.grid(column=1, row=2, pady=10)

    countLabel = Label(new_window, text="How many books")
    countLabel.grid(column=0, row=3, pady=10)
    countEntry = Entry(new_window, textvariable=bookcount, width=40)
    countEntry.grid(column=1, row=3, pady=10)

    submit = Button(new_window, text="Add", command=lambda: library(name_var.get(), address_var.get(), bookcount, new_window))
    submit.grid(column=1, row=4, pady=15)

def addBook( total_books, current_book):
    def submit(name: str, release_year: int, authors: str, window: Toplevel,library_name:StringVar):
        book = Book(name, release_year, authors)
        file_path = f"C:/Users/hiva laptop/Desktop/project/library/lib_{library_name.get()}.txt"
        with open(file_path, "a") as library:
            library.write(f"{book.name}_{book.release_year}_{book.authors}_{book.key}\n")
        window.destroy()
        if current_book + 1 < total_books:
            addBook(library_name, total_books, current_book + 1)

    new_window = Toplevel(root)
    new_window.title(f"Add Book {current_book + 1}/{total_books}")
    new_window.geometry("500x320")

    name_var = StringVar()
    release_var = IntVar()
    release_var.set(2000)
    author_var = StringVar()
    combo_var = StringVar()

    nameLabel = Label(new_window, text="Name of the Book",font=("arial",12))
    nameLabel.grid(column=0, row=0, pady=10)
    nameEntry = Entry(new_window, width=50, textvariable=name_var,font=("arial",10))
    nameEntry.grid(column=1, row=0, pady=10)

    yearLabel = Label(new_window, text="Release Year of Book",font=("arial",12))
    yearLabel.grid(column=0, row=2, pady=10)
    yearEntry = Entry(new_window, width=50, textvariable=release_var,font=("arial",10))
    yearEntry.grid(column=1, row=2, pady=10)

    authorLabel = Label(new_window, text="Author of the Book",font=("arial",12))
    authorLabel.grid(column=0, row=3, pady=10)
    authorEntry = Entry(new_window, textvariable=author_var, width=50,font=("arial",10))
    authorEntry.grid(column=1, row=3, pady=10)
    
    comboLabel = Label(new_window, text="which library:",font=("arial",15))
    comboLabel.grid(column=1, row=4, pady=10)
    

    libraries = []
    for i in range(len(Library.Liblist)):
        libraries.append(Library.Liblist[i][0])

    comboLib = Combobox(new_window,textvariable=combo_var,width=25)
    comboLib['values']=tuple(libraries)
    comboLib.grid(column=1,row=5)
    comboLib.current()

    submitBut = Button(new_window, text="Submit", command=lambda: submit(name_var.get(), release_var.get(), author_var.get(), new_window,combo_var))
    submitBut.grid(column=1, row=6, pady=15)

def delLib():
    new_window = Toplevel(root)
    new_window.title("Delete Library")
    new_window.geometry("300x200")

def delBook():
    new_window = Toplevel(root)
    new_window.title("Delete Book")
    new_window.geometry("300x200")

def changeBook():
    

    def find(name, library_name: StringVar, newName: StringVar, newRelease: StringVar, newAuthor: StringVar):
        file_path = f"C:/Users/hiva laptop/Desktop/project/library/lib_{library_name.get()}.txt"
    
        with open(file_path, "r") as file:
            lineList = file.readlines()
    
    # Flags to track if updates were made
        name_updated = False
        release_updated = False
        author_updated = False
    
        for i in range(len(lineList)):
            firstpart = lineList[i].find("_")
        
            if firstpart != -1 and name == lineList[i][0:firstpart]:
                # Update the name if newName is provided
                if newName.get() != "":
                    lineList[i] = newName.get() + lineList[i][firstpart:]
                    name_updated = True
            
            # Update the release year if newRelease is provided
                if newRelease.get() != "":
                    secondpart = lineList[i].find("_", firstpart + 1)
                    if secondpart != -1:
                        parts = lineList[i].split("_")
                        parts[1] = str(newRelease.get())
                        lineList[i] = "_".join(parts)
                        release_updated = True
            
            # Update the author if newAuthor is provided
                if newAuthor.get() != "":
                    secondpart = lineList[i].find("_", firstpart + 1)
                    if secondpart != -1:
                        thirdpart = lineList[i].find("_", secondpart + 1)
                        if thirdpart != -1:
                            lineList[i] = lineList[i][:secondpart + 1] + newAuthor.get() + lineList[i][thirdpart:]
                            author_updated = True
        
        # If at least one update is made, break the loop
            if name_updated or release_updated or author_updated:
                break
    
        with open(file_path, "w") as file:
            file.writelines(lineList)

    # Print update status
        if name_updated:
            print("Name updated successfully.")
        if release_updated:
            print("Release year updated successfully.")
        if author_updated:
            print("Author updated successfully.")
        if not (name_updated or release_updated or author_updated):
            print("No matching line found or no updates made.")
 

    new_window = Toplevel(root)
    new_window.title("Change Book")
    new_window.geometry("600x350")

    name_var = StringVar()
    combo_var = StringVar()

    new_name = StringVar()
    new_release = IntVar()
    new_author = StringVar()

    nameLabel = Label(new_window, text="name of the book you want to change",font=("arial",12))
    nameLabel.grid(column=0, row=0, pady=10)
    nameEntry = Entry(new_window, width=35, textvariable=name_var,font=("arial",10))
    nameEntry.grid(column=1, row=0, pady=10)

    nameLabel = Label(new_window, text="new name",font=("arial",12))
    nameLabel.grid(column=0, row=1, pady=10)
    nameEntry = Entry(new_window, width=35, textvariable=new_name,font=("arial",10))
    nameEntry.grid(column=1, row=1, pady=10)

    nameLabel = Label(new_window, text="new release year",font=("arial",12))
    nameLabel.grid(column=0, row=2, pady=10)
    nameEntry = Entry(new_window, width=35, textvariable=new_release,font=("arial",10))
    nameEntry.grid(column=1, row=2, pady=10)

    nameLabel = Label(new_window, text="new aouthor",font=("arial",12))
    nameLabel.grid(column=0, row=3, pady=10)
    nameEntry = Entry(new_window, width=35, textvariable=new_author,font=("arial",10))
    nameEntry.grid(column=1, row=3, pady=10)

    libraries = []
    for i in range(len(Library.Liblist)):
        libraries.append(Library.Liblist[i][0])

    comboLib = Combobox(new_window,textvariable=combo_var,width=25)
    comboLib['values']=tuple(libraries)
    comboLib.grid(column=1,row=4)
    comboLib.current()

    butfind = Button(new_window,text="find",command=lambda:find(name_var.get(),comboLib,new_name,new_release,new_author))
    butfind.grid(column=1,row=5)



def show():
    new_window = Toplevel(root)
    new_window.title("Show Data")
    new_window.geometry("300x200")

root = Tk()
root.geometry("400x300")
frame = Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

title_font = ('Helvetica', 16, 'bold')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

lblTitle = Label(frame, text="Library Management", padding=20, font=title_font)
lblTitle.grid(row=0, column=0, columnspan=2, pady=(0, 10))

btnAddLibrary = Button(frame, text="Add Library", command=addLib, padding=10)
btnAddLibrary.grid(row=1, column=0, columnspan=2, sticky="ew")

btnAddBook = Button(frame, text="Add a New Book", command=lambda: addBook( 1, 0), padding=10)  # Default value for testing
btnAddBook.grid(row=2, column=0, columnspan=2, sticky="ew")

btnDelLibrary = Button(frame, text="Delete a Library", command=delLib, padding=10)
btnDelLibrary.grid(row=3, column=0, columnspan=2, sticky="ew")

btnDelBook = Button(frame, text="Delete a Book", command=delBook, padding=10)
btnDelBook.grid(row=4, column=0, columnspan=2, sticky="ew")

btnChangeBook = Button(frame, text="Change a Book", command=changeBook, padding=10)
btnChangeBook.grid(row=5, column=0, columnspan=2, sticky="ew")

btnPrint = Button(frame, text="Print (Show) the Data", command=show, padding=10)
btnPrint.grid(row=6, column=0, columnspan=2, sticky="ew")

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

root.mainloop()
