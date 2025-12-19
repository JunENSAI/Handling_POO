# Option 1 : in your class you have list item as attributes

class Library:
    def __init__(self,books:list[str]):
        self.books = books

    
    def __iter__(self):
        return iter(self.books)

# for the loop part, you can use lib.books without define __iter__(self). lib.books is list so it is iterable

lib = Library(["1984", "Harry Potter", "Dune"])
for book in lib:
    print(book)

# Option 2 : need to define __iter__ and __next__ logic to make loop over the object Countdown

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        num = self.current
        self.current -= 1
        return num
    
for num in Countdown(3):
    print(num) 
