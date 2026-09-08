class Book:
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page

    def is_think_book(self):
        if self.page <= 0:
            print("Incorrect number of pages")
            return False
        elif 0 < self.page < 300:
            print("Book is not thick")
            return True
        else: 
            self.page >= 300
            print("Book is thick")
            return True
        
gramata = Book("The Body", "Stephen King", 73)
print(gramata.is_think_book())