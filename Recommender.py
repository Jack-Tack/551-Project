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
        self.__books.clear()
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
        self.__shows.clear()
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
        self.__associations.clear()
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
        movieList = []
        title_width = max(len(show.getTitle()) for show in self.__shows.values() if show.getType() == "Movie")
        run_width = max(len(show.getDuration()) for show in self.__shows.values() if show.getType() == "Movie")
        movieList.append(f"{'Title':<{title_width}} {'Runtime':<{run_width}}")
        for show in self.__shows.values():
            if show.getType() == "Movie":
                movieList.append(f"{show.getTitle():<{title_width}} {show.getDuration():<{run_width}}")
        return movieList

    def getTVList(self):
        showsList = []
        title_width = max(len(show.getTitle()) for show in self.__shows.values() if show.getType() != "Movie")
        s_width = len("Seasons")
        showsList.append(f"{'Title':<{title_width}} {'Seasons':<{s_width}}")
        for show in self.__shows.values():
            if show.getType() == "TV Show":
                showsList.append(f"{show.getTitle():<{title_width}} {show.getDuration():<{s_width}}")
        return showsList

    def getBookList(self):
        booksList = []
        title_width = max(len(book.getTitle()) for book in self.__books.values())
        auth_width = max(len(book.getAuthors()) for book in self.__books.values())
        booksList.append(f"{'Title':<{title_width}} {'Authors':<{auth_width}}")
        for book in list(self.__books.values())[1:]:
            booksList.append(f"{book.getTitle():<{title_width}} {book.getAuthors():<{auth_width}}")
        return booksList

    def getMovieStats(self):
        ratings_count = {}
        total_duration = 0
        directors = {}
        actors = {}
        genres = {}
        amount = 0
        for show in [show for show in self.__shows.values() if show.getType() == "Movie"]:
            showRate = show.getShowRate() if show.getShowRate() else "None"
            ratings_count[showRate] = ratings_count.get(show.getShowRate(), 0) + 1
            total_duration += int(show.getDuration().strip().replace("min", ""))
            for director in show.getDirectors().split("\\"):
                if director.strip():
                    directors[director] = directors.get(director, 0) + 1
            for actor in show.getActors().split("\\"):
                if actor.split():
                    actors[actor] = actors.get(actor, 0) + 1
            genres[show.getGenre()] = genres.get(show.getGenre(), 0) + 1
        for show in self.__shows.values():
            if show.getType() == "Movie":
                amount += 1
        for rating, count in ratings_count.items():
            percent = count / amount
            ratings_count[rating] = round(percent, 2)
        avg_duration = round(total_duration / amount, 2)
        max_director = sorted(directors.items(), reverse=True, key=lambda x: x[1])[0][0]
        max_actor = sorted(actors.items(), reverse=True, key=lambda x: x[1])[0][0]
        freq_genre = sorted(genres.items(), reverse=True, key=lambda x: x[1])[0][0]
        return ratings_count, avg_duration, max_director, max_actor, freq_genre


    def getTVStats(self):
        ratings_count = {}
        total_seasons = 0
        actors = {}
        genres = {}
        amount = 0
        for show in [show for show in self.__shows.values() if show.getType() == "TV Show"]:
            showRate = show.getShowRate() if show.getShowRate() else "None"
            ratings_count[showRate] = ratings_count.get(show.getShowRate(), 0) + 1
            total_seasons += int(show.getDuration().strip().replace('Season', '').replace('s', ''))
            for actor in show.getActors().split("\\"):
                if actor.strip():
                    actors[actor] = actors.get(actor, 0) + 1
            genres[show.getGenre()] = genres.get(show.getGenre(), 0) + 1
        for show in self.__shows.values():
            if show.getType() != "Movie":
                amount += 1
        for rating, count in ratings_count.items():
            percent = count / amount
            ratings_count[rating] = round(percent, 2)
        avg_duration = round(total_seasons / amount, 2)
        max_actor = sorted(actors.items(), reverse=True, key=lambda x: x[1])[0][0]
        freq_genre = sorted(genres.items(), reverse=True, key=lambda x: x[1])[0][0]
        return ratings_count, avg_duration, max_actor, freq_genre

    def getBookStats(self):
        page_count = 0
        authors = {}
        publishers = {}
        for book in list(self.__books.values())[1:]:
            page_count += int(book.getNumPage())
            for author in book.getAuthors().split("\\"):
                if author.strip():
                    authors[author] = authors.get(author, 0) + 1
            for publisher in book.getPub().split("\\"):
                if publisher.strip():
                    publishers[publisher] = publishers.get(publisher, 0) + 1
        avg_count = round(page_count / len(self.__books), 2)
        max_author = sorted(authors.items(), reverse=True, key=lambda x: x[1])[0][0]
        max_publisher = sorted(publishers.items(), reverse=True, key=lambda x: x[1])[0][0]
        return avg_count, max_author, max_publisher

    def searchTVMovies(self, type, title, director, actor, genre):
        type = type.strip()
        if type != "Movie" and type != "TV Show":
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
            if show.getType() == type:
                match = True
                if title and title != show.getTitle():
                    match = False
                if director and title != show.getDirectors():
                    match = False
                if actor and title != show.getActors():
                    match = False
                if genre and title != show.getGenre():
                    match = False

                if match:
                    show_details = f"Title: {show.getTitle()}, Directors: {show.getDirectors()}, Actors: {show.getActors()}, Genre: {show.getGenre()}"
                    results.append(show_details)
        if len(results) == 0:
            return "No Results"
        return results

    def searchBooks(self, title, author, publisher):
        title = title.strip()
        author = author.strip()
        publisher = publisher.strip()
        if title == "" and author == "" and publisher == "":
            tkinter.messagebox.showerror(title="Error", message="You must enter information for at least one category first.")
            return "No Results"
        results = []
        for book in self.__books.values():
            match = True
            if title and title != book.getTitle():
                match = False
            if author and author != book.getAuthors():
                match = False
            if publisher and publisher != book.getPub():
                match = False
            if match:
                results.append(f"Title: {book.getTitle()}, Author: {book.getAuthors()}, Publisher: {book.getPub()}")
        if len(results) == 0:
            return "No Results"
        return results

    def getRecommendations(self, type, title):
        type = type.strip().lower()
        title = title.strip().lower()
        if type == "movie" or type == "tv show":
            show_id = None
            for show_id, show in self.__shows.items():
                if show.title.lower() == title:
                    break
            else:
                tkinter.messagebox.showerror(title="Error", message="There are no recommendations for this title")
                return "No Results"
            recommendations = []
            if show_id in self.__associations:
                for assoc_id, num_assoc in self.__associations[show_id].items():
                    if assoc_id in self.__books:
                        book = self.__books[assoc_id]
                        recommendations.append(f"Book Title: {book.title}")
                        recommendations.append(f"Authors: {book.authors}")
                        recommendations.append(f"Rating: {book.rating}")
                        recommendations.append(f"ISBN: {book.isbn}")
                        recommendations.append(f"ISBN13: {book.isbn13}")
                        recommendations.append(f"Language: {book.lang}")
                        recommendations.append(f"Number of Pages: {book.numPage}")
                        recommendations.append(f"Number of Ratings: {book.numRate}")
                        recommendations.append(f"Date of Publication: {book.pubDate}")
                        recommendations.append(f"Publisher: {book.pub}")
            if not recommendations:
                return "No Results"
            else:
                return "\n".join(recommendations)
        elif type == "book":
            book_id = None
            for book_id, book in self.__books.items():
                if book.title.lower() == title:
                    break
            else:
                tkinter.messagebox.showerror(title="Error", message="There are no recommendations for this title")
                return "No Results"
            recommendations = []
            if book_id in self.__associations:
                for assoc_id, num_assoc in self.__associations[book_id].items():
                    if assoc_id in self.__shows:
                        show = self.__shows[assoc_id]
                        recommendations.append(f"Show Title: {show.title}")
                        recommendations.append(f"Type: {show.type}")
                        recommendations.append(f"Directors: {show.directors}")
                        recommendations.append(f"Actors: {show.actors}")
                        recommendations.append(f"Rating: {show.rating}")
                        recommendations.append(f"Country: {show.countryCode}")
                        recommendations.append(f"Date Added: {show.dateAdded}")
                        recommendations.append(f"Release Year: {show.releaseYear}")
                        recommendations.append(f"Duration: {show.duration}")
                        recommendations.append(f"Genre: {show.genre}")
                        recommendations.append(f"Description: {show.description}")
            if not recommendations:
                return "No Results"
            else:
                return "\n".join(recommendations)
