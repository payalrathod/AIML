class LibraryManagement:
    def __init__(self, listOfbooks):
        self.listOfbooks = listOfbooks
        # self.countofBooks = countofbooks
    def BooksInLibrary(self):
        self.library = {'Think':2, 'Cry':1, 'More':3}
        print("Available books")
        for book in self.listOfbooks:
            print(book)
        for ky, number in library.items():
            if (number > 0):
                number -= 1
                # print(libary[ky] = number)

    def BorrowBooks(self, request):
        if request in self.listOfbooks:
            print("book borrowed", request)
            self.listOfbooks.remove(request)
        else:
            print("book not available")
    def UpdateBooksAfterReturn(self, returnBook):
        self.listOfbooks.append(returnBook)
        print("book returned")

class Customer:
    def requestBook(self):
        print("enter book name")
        self.book = input()
        return  self.book
    def returnBook(self):
        print("enter name:")
        self.returnbook = input()
        return self.returnbook

library = LibraryManagement() #objects
customer = Customer()

while True:
    user = int(input())
    if user is 1:
        library.BooksInLibrary()
    elif user is 2:
        req = customer.requestBook()
        library.BorrowBooks(req)
    elif user is 3:
        ret = customer.returnBook()
        library.UpdateBooksAfterReturn(ret)
    elif user is 4:
        quit()


