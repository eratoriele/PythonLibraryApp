import datetime
import random

from People.Librarian import *
from People.LibraryPatron import *
from Books.Books import *


def increase_floor_and_sections(flr, sct):
    if sct != MAX_SECTION:
        sct += 1
    elif flr != MAX_FLOOR:
        flr += 1
        sct = MIN_SECTION
    # We reached the last floor of last section, throw an error
    else:
        raise IndexError("Not enough space for books!")

    return [flr, sct]

def test1():
    cur_flr_sct = [0, 1]
    i = 0
    for book in book_list:
        if cur_flr_sct != [book.position.floor, book.position.section]:
            # print(cur_flr_sct[0], cur_flr_sct[1], book.position.floor, book.position.section, i, book.genre, "\n")
            cur_flr_sct = [book.position.floor, book.position.section]
            i = 0
            print("\n------------", cur_flr_sct[0], "--", cur_flr_sct[1], "------------")
        print("Name:", book.name, "Genre:", book.genre.value[0])
        i += 1


if __name__ == "__main__":

    book_list = generate_random_books(500)
    # Give library patron list the books so people can be generated with borrowed books
    library_patron_list = generate_random_library_patrons(125, book_list)
    librarian_list = generate_random_librarians(15)

    # TASK 1: Sort the book positions according to their genres, and in those genres, sort them by alphabetic order
    # Notes: there are 5 floors, from 0 to 4, and 5 sections on each floor, from 1 to 5. Each section can hold
    # 30 books. Each section can only have 1 genre on it. There might be multiple sections for a genre.
    # (Hope that random generation does not exceed these limits)

    MIN_FLOOR = 0
    MAX_FLOOR = 4
    MIN_SECTION = 1
    MAX_SECTION = 5
    MAX_BOOKS_IN_A_SECTION = 30

    # First sort by name, the sort by genre
    # Due to how sorting works, the second sort should not break the first alphabetical sort
    book_list.sort(key=lambda book: book.name)
    book_list.sort(key=lambda book: book.genre.value[1])

    current_floor = MIN_FLOOR
    current_section = MIN_SECTION
    amount_of_books_in_section = 0
    last_genre = book_list[0].genre
    for i in range(len(book_list)):
        current_genre = book_list[i].genre
        # If we are still handling books in the same genre
        if current_genre == last_genre:
            book_list[i].position.floor = current_floor
            book_list[i].position.section = current_section

            amount_of_books_in_section += 1
            if amount_of_books_in_section == MAX_BOOKS_IN_A_SECTION:
                amount_of_books_in_section = 0
                [current_floor, current_section] = increase_floor_and_sections(current_floor, current_section)
        # Skipped to the next genre, change floor/section
        else:
            amount_of_books_in_section = 0
            last_genre = current_genre
            [current_floor, current_section] = increase_floor_and_sections(current_floor, current_section)

            book_list[i].position.floor = current_floor
            book_list[i].position.section = current_section
            amount_of_books_in_section += 1

    test1()

