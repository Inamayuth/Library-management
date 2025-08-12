class Library:
    
    def __init__(self,list):
        self.book_list = list
        self.available_books_list = list
        self.books_lend = {}#k-book v-user name

    def display_available_books(self):
        for book in self.available_books_list:
            print(book)
    
    def display_all_books(self):
        for book in self.book_list:
            print(book)

    def lend_book(self,name,book):
        if book not in self.book_list:
            print("Incorrect book name. Please check book list")
            return
        if book in self.available_books_list:
            self.books_lend.update({book:name})
            self.available_books_list.remove(book)
            print("you can take the book ")
        else:
            print("The book is already taken by " + self.books_lent[book])
 
    def return_book(self,book):
        del self.books_lend[book]
        self.available_books_list.append(book)

        
if __name__=="__main__":
    Lib = Library(["King","Queen","Tamil","Cricket","News"])
    print("Welcome! Enter an option")
    
    while True:
           print(" 1 Display the available books ")
           print(" 2 Display all books ")
           print(" 3 Borrow a book ")
           print(" 4 Return a book ")
           print(" 5 Quit ")
           
           user_choice = int(input())
           
           if user_choice == 1:
               Lib.display_available_books()
               
           elif user_choice == 2:
                Lib.display_all_books()
                
           elif user_choice == 3:
                name = input(" Enter the name " )
                book = input(" Enter book Name ")
                Lib.lend_book(name,book)
                
           elif user_choice == 4:
                book = input("Enter the name of book ")
                Lib.return_book(book)
                
           elif  user_choice == 5:
                break
            
           else:
                print("invalid Choice")
