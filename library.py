from enum import Enum
class Reading_state(Enum):
    UNREAD=1
    CURRENTLY_READING=2
    COMPLETED=3

class Book:
    def __init__(self,title,author,total_number_of_pages):
        self.title=title
        self.author=author
        self.total_number_of_pages=total_number_of_pages
        self.status=Reading_state.UNREAD
        self.current_page=0
    
    def turn_page(self):
        if self.current_page<self.total_number_of_pages:
            self.current_page+=1
            if self.status==Reading_state.UNREAD:
                self.status=Reading_state.CURRENTLY_READING

        elif self.current_page==self.total_number_of_pages:
            self.status=Reading_state.COMPLETED
    

    

#learnt that parameters are only passed inside the constructor if the object
# created needs some external attributes, status is sth thats default to UNREAD when object
# is created, so no need to be mentioned when declaring the object, similarly
# in library class, default attributes like books attribute is an empty default value.

#when using self.attribute, to visualize, assume that the self is the class itself that 
# holds place for the object.

class Library:
    def __init__(self):
        self.books={}
        self.total_books=0
        self.active_books=None
    
    def add_book(self,book_object):
        self.books[book_object.title]=book_object
        self.total_books=len(self.books)
    
    def remove_book(self,book_object):
        self.books.pop(book_object.title)
        self.total_books=len(self.books)-1
    
    def active_book(self,book_title):
        if book_title in self.books:
            self.active_book=self.books[book_title]#stores whole book object

            if self.active_book.status==Reading_state.UNREAD:
                self.active_book.status=Reading_state.CURRENTLY_READING
                print(f"{book_title} is now your current Active book")
                return True
        else:
            print(f"{book_title} is not in the book library")
            return False




        
        



    


    



