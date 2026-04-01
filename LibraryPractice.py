class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.isthis = True   # Available

    def __str__(self):
        return f"{self.title} | {self.author} | {self.genre} | Available: {self.isthis}"


class Member:
    def __init__(self, username):
        self.username = username
        self.borrowedbooks = []

    def borrowbook(self, book):
        if len(self.borrowedbooks) < 5 and book.isthis:
            self.borrowedbooks.append(book)
            book.isthis = False
            return True
        return False

    def returnbook(self, book):
        if book in self.borrowedbooks:
            self.borrowedbooks.remove(book)
            book.isthis = True
            return True
        return False


books = []
members = []
admin = "admin"
password = "password"
loginmember = None

books.append(Book("Science", "John", "Education"))
books.append(Book("Maths", "Killer", "Education"))


def addbook():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    genre = input("Enter the book genre: ")
    books.append(Book(title, author, genre))
    print("Book added successfully")


def findbybooktitle(title):
    for book in books:
        if book.title == title:
            return book
    return None


def updatebook():
    title = input("Enter the book title to update: ")
    book = findbybooktitle(title)
    if book:
        book.title = input("New title: ")
        book.author = input("New author: ")
        book.genre = input("New genre: ")
        print("Book updated")
    else:
        print("Book not found")


def removebook():
    title = input("Enter the book title: ")
    book = findbybooktitle(title)
    if book:
        books.remove(book)
        print("Book removed")
    else:
        print("Book not found")


def addmember():
    username = input("Enter username: ")
    members.append(Member(username))
    print("Member added")


def displayallbooks():
    if not books:
        print("No books available")
    else:
        for book in books:
            print(book)


def displayallmembers():
    if not members:
        print("No members available")
    else:
        for m in members:
            print(f"{m.username} | Borrowed books: {len(m.borrowedbooks)}")


def adminmenu():
    while True:
        print("\n1.Add Book 2.Update Book 3.Remove Book 4.Add Member 5.Display Books 6.Display Members 7.Exit")
        choice = input("Choice: ")
        if choice == "1":
            addbook()
        elif choice == "2":
            updatebook()
        elif choice == "3":
            removebook()
        elif choice == "4":
            addmember()
        elif choice == "5":
            displayallbooks()
        elif choice == "6":
            displayallmembers()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


def loginasadmin():
    user = input("Username: ")
    key = input("Password: ")
    if user == admin and key == password:
        adminmenu()
    else:
        print("Invalid admin credentials")


def borrowbooks():
    title = input("Enter book title: ")
    book = findbybooktitle(title)
    if book and loginmember.borrowbook(book):
        print("Book borrowed")
    else:
        print("Cannot borrow book")


def returnbooks():
    title = input("Enter book title: ")
    book = findbybooktitle(title)
    if book and loginmember.returnbook(book):
        print("Book returned")
    else:
        print("Cannot return book")


def usermenu():
    while True:
        print("\n1.Borrow 2.Return 3.Display Books 4.Exit")
        choice = input("Choice: ")
        if choice == "1":
            borrowbooks()
        elif choice == "2":
            returnbooks()
        elif choice == "3":
            displayallbooks()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


def findcreatemember(username):
    for m in members:
        if m.username == username:
            return m
    new = Member(username)
    members.append(new)
    return new


def loginasuser():
    global loginmember
    username = input("Enter username: ")
    loginmember = findcreatemember(username)
    print("Logged in as user")
    usermenu()




if __name__ == "__main__":
    while True:
        role = input("\nEnter role (admin/user/exit): ")
        if role == "admin":
            loginasadmin()
        elif role == "user":
            loginasuser()
        elif role == "exit":
            break
        else:
            print("Invalid role")
