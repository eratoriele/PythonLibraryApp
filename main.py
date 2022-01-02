import datetime
import random

from People.Librarian import *
from People.LibraryPatron import *
from Books.Books import *


if __name__ == "__main__":

    book_list = generate_random_books(250)
    library_patron_list = generate_random_library_patrons(75)
    librarian_list = generate_random_librarians(15)

    for i in range(book_list.__len__()):
        print(book_list[i].to_string())
