from library import Library

class users:
    def __init__(self, id: str, username: str):
        self.id=id
        self.username=username

        self.library_access=Library()

    def adds_book(self,book_obj: object):
        self.library_access.add_book(book_obj)
        print(f"Successfully added {book_obj.title}")

    def removes_book(self,book_obj:object):
        self.library_access.remove_book(book_obj)
        print(f'Successfully removed {book_obj.title}')

    def turns_page(self):
        if self.library_access.active_books is not None: #active books is storing the title
            self.library_access.active_books.turn_page()
            print("Page is turned")
        else:
            print("open a book first")



    

        