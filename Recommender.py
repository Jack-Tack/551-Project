# Authors: Ryan DeSantis, Aidan Rudd, Jarrett Aaronson
# Date: 4/23/24
# Description: Recommender class for Media For You system
from Book import Book
from Show import Show
import tkinter.filedialog
import os

class Recommender:
    def __init__(self):
        # self.__book = {Book.getID(book): book}
        self.__books = {}
        # self.__show = {Show.getID(show): show}
        self.__shows = {}
        # self.__dictionaries = {Book.getID(book): {Show.getID(show): numAssociated}}
        self.__associations = {}

    def loadBooks(self):
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while not os.path.exists(f"{filename}"):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        with open(filename, 'r') as file:
            for line in file:
                book_info = line.strip().split(",")
                id, title, authors, rating, isbn, isbn13, lang, numPage, numRate, pubDate, pub = book_info
                book = Book(id, title, rating, authors, isbn, isbn13, lang, numPage, numRate, pubDate, pub)
                self.__books[id] = book

    def loadShows(self):
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while not os.path.exists(f"{filename}"):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        with open(filename, 'r') as file:
            for line in file:
                show_info = line.strip().split(",")
                id, type, title, directors, actors, rating, countryCode, dateAdded, releaseYear, showRate, duration, genre, description = show_info
                show = Show(id, type, title, rating, directors, actors, countryCode, dateAdded, releaseYear, showRate, duration, genre, description)
                self.__shows[id] = show

    def loadAssociations(self):
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while not os.path.exists(f"{filename}"):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        with open(filename, 'r') as file:
            for line in file:
                first_id, second_id = line.strip().split(',')
                if first_id not in self.__associations:
                    self.__associations[first_id] = {}
                if second_id not in self.__associations[first_id]:
                    self.__associations[first_id][second_id] = 1
                else:
                    self.__associations[first_id][second_id] += 1
                if second_id not in self.__associations:
                    self.__associations[second_id] = {}
                if first_id not in self.__associations[second_id]:
                    self.__associations[second_id][first_id] = 1
                else:
                    self.__associations[second_id][first_id] += 1

    def getMovieList(self):
        title_width = max(len(show.title) for show in self.__shows.values() if show.type == "Movie")
        run_width = max(len(show.duration) for show in self.__shows.values() if show.type == "Movie")
        print(f"{'Title':<{title_width}} {'Runtime':<{run_width}}")
        for show in self.__shows.values():
            if show.type == "Movie":
                print(f"{show.title:<{title_width}} {show.duration:<{run_width}}")

    def getTVList(self):
        title_width = max(len(show.title) for show in self.__shows.values() if show.type != "Movie")
        s_width = len("Seasons")
        print(f"{'Title':<{title_width}} {'Seasons':<{s_width}}")
        for show in self.__shows.values():
            if show.type != "Movie":
                print(f"{show.title:<{title_width}} {show.seasons:<{s_width}}")

    def getBookList(self):
        title_width = max(len(book.title) for book in self.__books.values())
        auth_width = max(len(book.authors) for book in self.__books.values())
        print(f"{'Title':<{title_width}} {'Authors':<{auth_width}}")
        for book in self.__books.values():
            print(f"{book.title:<{title_width}} {book.authors:<{auth_width}}")
