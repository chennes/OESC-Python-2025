from person import Person

class Librarian(Person):
    def __init__(self, name:str):
        super().__init__(name)
        self.shelf = []

    def shelve_book(self, title:str):
        self.shelf.append(title)