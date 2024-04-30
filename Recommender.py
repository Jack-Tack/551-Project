# Authors: Ryan DeSantis, Aidan Rudd, Jarrett Aaronson
# Date: 4/23/24
# Description: Recommender class for Media For You system
from Book import Book
from Show import Show
import tkinter.filedialog
import os
import tkinter.messagebox

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

    def getMovieStats(self):
        ratings_count = {}
        total_duration = 0
        directors = {}
        actors = {}
        genres = {}

        for show in [show for show in self.__shows.values() if show.getType() == "Movie"]:
            ratings_count[show.getShowRate()] = ratings_count.get(show.getShowRate(), 0) + 1
            total_duration += show.getDuration()

            for director in show.getDirectors().split("\\"):
                directors[director] = directors.get(director, 0) + 1

            for actor in show.getActors().split("\\"):
                actors[actor] = actors.get(actor, 0) + 1

            genres[show.getGenre()] = genres.get(show.getGenre(), 0) + 1


        for rating, count in ratings_count.items():
            percent = count / len(self.__shows)
            ratings_count[rating] = round(percent, 2)

        avg_duration = round(total_duration / len(self.__shows), 2)
        max_director = sorted(directors.items(), reverse=False, key=lambda x: x[1])[0][0]
        max_actor = sorted(actors.items(), reverse=False, key=lambda x: x[1])[0][0]
        freq_genre = sorted(genres.items(), reverse=False, key=lambda x: x[1])[0][0]

        return ratings_count, avg_duration, max_director, max_actor, freq_genre


    def getTVStats(self):
        ratings_count = {}
        total_seasons = 0
        actors = {}
        genres = {}

        for show in [show for show in self.__shows.values() if show.getType() == "TV Show"]:
            ratings_count[show.getShowRate()] = ratings_count.get(show.getShowRate(), 0) + 1
            total_seasons += show.getDuration().strip().replace('Season', '')

            for actor in show.getActors().split("\\"):
                actors[actor] = actors.get(actor, 0) + 1

            genres[show.getGenre()] = genres.get(show.getGenre(), 0) + 1

        for rating, count in ratings_count.items():
            percent = count / len(self.__shows)
            ratings_count[rating] = round(percent, 2)

        avg_duration = round(total_seasons / len(self.__shows), 2)
        max_actor = sorted(actors.items(), reverse=False, key=lambda x: x[1])[0][0]
        freq_genre = sorted(genres.items(), reverse=False, key=lambda x: x[1])[0][0]

        return ratings_count, avg_duration, max_actor, freq_genre

    def getBookStats(self):
        page_count = 0
        author = {}
        publisher = {}

        for book in self.__books.values():
            page_count += book.getNumPage()

            for author in book.getAuthors().split("\\"):
                author[author] = author.get(author, 0) + 1

            for publisher in book.getPub().split("\\"):
                publisher[publisher] = publisher.get(publisher, 0) + 1


        avg_count = round(page_count / len(self.__books), 2)
        max_author = sorted(author.items(), reverse=False, key=lambda x: x[1])[0][0]
        max_publisher = sorted(publisher.items(), reverse=False, key=lambda x: x[1])[0][0]

        return avg_count, max_author, max_publisher

    def searchTVMovies(self, type, title, director, actor, genre):
        type = type.strip().lower()
        if type != "movie" and type != "tv show":
            tkinter.messagebox.showerror(title="Error", message="You must select Movie or TV Show from Type first.")
            return "No Results"
        title = title.strip()
        director = director.strip()
        actor = actor.strip()
        genre = genre.strip()
        if title == "" and director == "" and actor == "" and genre == "":
            tkinter.messagebox.showerror(title="Error", message="You must enter information for at least one category first.")
            return "No Results"
        results = []
        for show in self.__shows.values():
            if show.type.lower() == type:
                if title and title not in show.title.lower():
                    continue
                if director and director not in show.directors.lower():
                    continue
                if actor and actor not in show.actors.lower():
                    continue
                if genre and genre not in show.genre.lower():
                    continue
                results.append(show)
        return results





