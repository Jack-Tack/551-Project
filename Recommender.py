# Authors: Ryan DeSantis, Aidan Rudd, Jarrett Aaronson
# Date: 4/23/24
# Description: Recommender class for Media For You system

# Here we import the classes from the Book.py and Show.py programs as well as tkinter
from Book import Book
from Show import Show
import tkinter.filedialog
import os
import tkinter.messagebox

# This is the recommender class that creates dictionaries to store the books, shows, and associations
class Recommender:
    def __init__(self):
        # self.__book = {Book.getID(book): book}
        self.__books = {}
        # self.__show = {Show.getID(show): show}
        self.__shows = {}
        # self.__dictionaries = {Book.getID(book): {Show.getID(show): numAssociated}}
        self.__associations = {}

    def loadBooks(self):
        """
        This loads books from a file into a book inventory

        It prompts the user to select a file using a file dialog box.
        It will repeatedly prompt the user until they submit a valid file.
        Once a valid file is submitted it reads the file line by line and
        extracts the information from the file and adds it to the book inventory
        :return:
            None
        :raises:
            FileNotFoundError if selected file doesn't exist
            ValueError if the file format is incorrect
        """
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
        """
        This loads shows from a file into a show inventory

        It prompts the user to select a file using a file dialog box.
        It will repeatedly prompt the user until they submit a valid file.
        Once a valid file is submitted it reads the file line by line and
        extracts the information from the file and adds it to the show inventory
        :return:
            None
        :raises:
            FileNotFoundError if selected file doesn't exist
            ValueError if the file format is incorrect
        """
        self.__shows.clear()
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while not os.path.exists(f"{filename}"):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        with open(filename, 'r') as file:
            for line in file:
                show_info = line.strip().split(",")
                id, type, title, directors, actors, rating, countryCode, dateAdded, releaseYear, showRate, duration, genre, description = show_info
                show = Show(id, type, title, rating, directors, actors, countryCode, dateAdded, releaseYear, showRate,
                            duration, genre, description)
                self.__shows[id] = show

    def loadAssociations(self):
        """
        Loads associations betweens books and shows from a file into an association inventory

        It prompts the user to select a file using a file dialog box.
        It will repeatedly prompt the user until they submit a valid file.
        Once a valid file is submitted it reads the file line by line and
        extracts the information from the file and adds it to the association inventory
        :return:
            None
        :raises:
            FileNotFoundError if selected file doesn't exist
            ValueError if the file format is incorrect
        """
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
        """
        Gets a list of movies along with their titles and runtimes

        Generates a list of movies by going over the shows inventory and
        filtering for those with type "Movie" and creates a formatted list of movies
        :return:
            list of movies and their runtimes
        """
        movieList = []
        title_width = max(len(show.getTitle()) for show in self.__shows.values() if show.getType() == "Movie")
        run_width = max(len(show.getDuration()) for show in self.__shows.values() if show.getType() == "Movie")
        movieList.append(f"{'Title':<{title_width}} {'Runtime':<{run_width}}")
        for show in self.__shows.values():
            if show.getType() == "Movie":
                movieList.append(f"{show.getTitle():<{title_width}} {show.getDuration():<{run_width}}")
        return movieList

    def getTVList(self):
        """
        Gets a list of tv shows along with their titles and number of seasons

        Generates a list of shows by going over the shows inventory and
        filtering for those with type "TV Show" and creates a formatted list of movies
        :return:
            list of shows and their seasons
        """
        showsList = []
        title_width = max(len(show.getTitle()) for show in self.__shows.values() if show.getType() != "Movie")
        s_width = len("Seasons")
        showsList.append(f"{'Title':<{title_width}} {'Seasons':<{s_width}}")
        for show in self.__shows.values():
            if show.getType() == "TV Show":
                showsList.append(f"{show.getTitle():<{title_width}} {show.getDuration():<{s_width}}")
        return showsList

    def getBookList(self):
        """
        Gets a list of books along with their titles and authors

        Generates a list of books by going over the books inventory and
        calculates the max width of the title and author to format properly
        :return:
            list of book titles and movies
        """
        booksList = []
        title_width = max(len(book.getTitle()) for book in self.__books.values())
        auth_width = max(len(book.getAuthors()) for book in self.__books.values())
        booksList.append(f"{'Title':<{title_width}} {'Authors':<{auth_width}}")
        for book in list(self.__books.values())[1:]:
            booksList.append(f"{book.getTitle():<{title_width}} {book.getAuthors():<{auth_width}}")
        return booksList

    def getMovieStats(self):
        """
        Gets the stats for movies in inventory

        It calculates various statistics for movies in the inventory
        including the amount of each rating, average duration, most frequent
        director, most frequent actor, and most frequent genre
        :return:
            tuple containing amount of each rating, average duration, most frequent
            director, most frequent actor, and most frequent genre
        """
        ratings_count = {}
        total_duration = 0
        directors = {}
        actors = {}
        genres = {}
        amount = 0
        total = 0
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
            total += round(percent, 2)
            ratings_count[rating] = round(percent, 2)
        if "None" in ratings_count:
            fix_offset = 1 - total
            ratings_count["None"] += fix_offset
        avg_duration = round(total_duration / amount, 2)
        max_director = sorted(directors.items(), reverse=True, key=lambda x: x[1])[0][0]
        max_actor = sorted(actors.items(), reverse=True, key=lambda x: x[1])[0][0]
        freq_genre = sorted(genres.items(), reverse=True, key=lambda x: x[1])[0][0]
        return ratings_count, avg_duration, max_director, max_actor, freq_genre

    def getTVStats(self):
        """
        Gets the stats for TV shows in inventory

        It calculates various statistics for tv shows in the inventory
        including the amount of each rating, total seasons, most frequent actor,
        and most frequent genre
        :return:
            tuple containing amount of each rating, average duration,
            most frequent actor, and most frequent genre
        """
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
                if actor.split():
                    actors[actor] = actors.get(actor, 0) + 1
            genres[show.getGenre()] = genres.get(show.getGenre(), 0) + 1
        for show in self.__shows.values():
            if show.getType() == "TV Show":
                amount += 1
        for rating, count in ratings_count.items():
            percent = count / amount
            ratings_count[rating] = round(percent, 2)
        avg_duration = round(total_seasons / amount, 2)
        max_actor = sorted(actors.items(), reverse=True, key=lambda x: x[1])[0][0]
        freq_genre = sorted(genres.items(), reverse=True, key=lambda x: x[1])[0][0]
        return ratings_count, avg_duration, max_actor, freq_genre

    def getBookStats(self):
        """
        Gets the stats for books in inventory

        It calculates various statistics for books in the inventory
        including the average page count, most frequent author, and most frequent
        publisher
        :return:
            tuple containing average page count, most frequent author, and most frequent
            publisher
        """
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
        avg_count = round(page_count / (len(self.__books) - 1), 2)
        max_author = sorted(authors.items(), reverse=True, key=lambda x: x[1])[0][0]
        max_publisher = sorted(publishers.items(), reverse=True, key=lambda x: x[1])[0][0]
        return avg_count, max_author, max_publisher

    def searchTVMovies(self, type, title, director, actor, genre):
        """
        Searches the collection of tv shows and movies based on various
        criteria

        :parameter:
            type: show or movie
            title: title of show or movie
            director: Name of director
            actor: Name of actor
            genre: Genre of show

        :returns:
            list of search results or "No Results"
        """
        type = type.strip()
        if type != "Movie" and type != "TV Show":
            tkinter.messagebox.showerror(title="Error", message="You must select Movie or TV Show from Type first.")
            return "No Results"
        title = title.strip()
        director = director.strip()
        actor = actor.strip()
        genre = genre.strip()
        if title == "" and director == "" and actor == "" and genre == "":
            tkinter.messagebox.showerror(title="Error",
                                         message="You must enter information for at least one category first.")
            return "No Results"
        results = []
        maxMovieTitleWidth = max(len(show.getTitle()) for show in self.__shows.values() if show.getType() == "Movie")
        maxMovieDirectorWidth = max(
            len(show.getDirectors()) for show in self.__shows.values() if show.getType() == "Movie")
        maxMovieActorWidth = max(len(show.getActors()) for show in self.__shows.values() if show.getType() == "Movie")
        maxMovieGenreWidth = max(len(show.getGenre()) for show in self.__shows.values() if show.getType() == "Movie")
        maxTVTitleWidth = max(len(show.getTitle()) for show in self.__shows.values() if show.getType() == "TV Show")
        maxTVDirectorWidth = len("Directors ")
        maxTVActorWidth = max(len(show.getActors()) for show in self.__shows.values() if show.getType() == "TV Show")
        maxTVGenreWidth = max(len(show.getGenre()) for show in self.__shows.values() if show.getType() == "TV Show")
        if type == "Movie":
            results.append(
                f"{'Title':<{maxMovieTitleWidth}}{'Directors':<{maxMovieDirectorWidth}}{'Actors':<{maxMovieActorWidth}}{'Genre':<{maxMovieGenreWidth}}")
        elif type == "TV Show":
            results.append(
                f"{'Title':<{maxTVTitleWidth}}{'Directors ':<{maxTVDirectorWidth}}{'Actors':<{maxTVActorWidth}}{'Genre':<{maxTVGenreWidth}}")
        for show in self.__shows.values():
            if show.getType() == type:
                match = True
                if title and title not in show.getTitle():
                    match = False
                if director and director not in show.getDirectors():
                    match = False
                if actor and actor not in show.getActors():
                    match = False
                if genre and genre not in show.getGenre():
                    match = False

                if match:
                    if type == "Movie":
                        show_details = f"{show.getTitle():<{maxMovieTitleWidth}}{show.getDirectors():<{maxMovieDirectorWidth}}{show.getActors():<{maxMovieActorWidth}}{show.getGenre():<{maxMovieGenreWidth}}"
                    elif type == "TV Show":
                        show_details = f"{show.getTitle():<{maxTVTitleWidth}}{show.getDirectors():<{maxTVDirectorWidth}}{show.getActors():<{maxTVActorWidth}}{show.getGenre():<{maxTVGenreWidth}}"
                    results.append(show_details)
        if len(results) == 0:
            return "No Results"
        return results

    def searchBooks(self, title, author, publisher):
        """
        Searches the collection of books based on various criteria

        :parameter:
            title: title of show or movie
            author: Name of author
            publisher: Name of publisher

        :returns:
            list of search results or "No Results"
        """
        title = title.strip()
        author = author.strip()
        publisher = publisher.strip()
        if title == "" and author == "" and publisher == "":
            tkinter.messagebox.showerror(title="Error",
                                         message="You must enter information for at least one category first.")
            return "No Results"
        results = []
        maxTitleWidth = max(len(book.getTitle()) for book in self.__books.values())
        maxAuthorWidth = max(len(book.getAuthors()) for book in self.__books.values())
        maxPublisherWidth = max(len(book.getPub()) for book in self.__books.values())
        results.append(f"{'Title':<{maxTitleWidth}}{'Authors':<{maxAuthorWidth}}{'Publishers':<{maxPublisherWidth}}")
        for book in self.__books.values():
            match = True
            if title and title not in book.getTitle():
                match = False
            if author and author not in book.getAuthors():
                match = False
            if publisher and publisher not in book.getPub():
                match = False
            if match:
                book_details = f"{book.getTitle():<{maxTitleWidth}}{book.getAuthors():<{maxAuthorWidth}}{book.getPub():<{maxPublisherWidth}}"
                results.append(book_details)
        if len(results) == 0:
            return "No Results"
        return results

    def getRecommendations(self, type, title):
        """
        Gathers recommendations based on the type and title of
        book, tv show, or movie

        Takes in the type of media the user wants to use whether it be a
        "Movie", "Book", or "Tv Show" and then the user inputs the title of that
        media type. It then searches for associated pieces of media based on the input

        :parameter:
            type: show, book, or movie
            title: title of media

        :return:
            Information about the recommended media that's associated
            with the information the user inputted
        """
        type = type.strip()
        title = title.strip()
        if type == "Movie" or type == "TV Show":
            show_id = None
            for show_id, show in self.__shows.items():
                if show.getTitle() == title:
                    show_id = show.getID()
                    break
            if show_id is None or title == "":
                tkinter.messagebox.showerror(title="Error", message="There are no recommendations for this title")
                return "No Results"
            recommendations = []
            if show_id in self.__associations:
                for assoc_id, num_assoc in self.__associations[show_id].items():
                    if assoc_id in self.__books:
                        book = self.__books[assoc_id]
                        recommendations.append(f"Book Title: {book.getTitle()}\n")
                        recommendations.append(f"Authors: {book.getAuthors()}\n")
                        recommendations.append(f"Rating: {book.getRating()}\n")
                        recommendations.append(f"ISBN: {book.getISBN()}\n")
                        recommendations.append(f"ISBN13: {book.getISBN13()}\n")
                        recommendations.append(f"Language: {book.getLang()}\n")
                        recommendations.append(f"Number of Pages: {book.getNumPage()}\n")
                        recommendations.append(f"Number of Ratings: {book.getNumRate()}\n")
                        recommendations.append(f"Date of Publication: {book.getPubDate()}\n")
                        recommendations.append(f"Publisher: {book.getPub()}\n")
                        recommendations.append("************************************")
                        recommendations.append("\n")
            if not recommendations:
                return "No Results"
            else:
                return "\n".join(recommendations)
        elif type == "Book":
            book_id = None
            for book_id, book in self.__books.items():
                if book.getTitle() == title:
                    book_id = book.getID()
                    break
            if book_id is None or title == "":
                tkinter.messagebox.showerror(title="Error", message="There are no recommendations for this title")
                return "No Results"
            recommendations = []
            if book_id in self.__associations:
                for assoc_id, num_assoc in self.__associations[book_id].items():
                    if assoc_id in self.__shows:
                        show = self.__shows[assoc_id]
                        recommendations.append(f"Show Title: {show.getTitle()}\n")
                        recommendations.append(f"Type: {show.getType()}\n")
                        recommendations.append(f"Directors: {show.getDirectors()}\n")
                        recommendations.append(f"Actors: {show.getActors()}\n")
                        recommendations.append(f"Rating: {show.getRating()}\n")
                        recommendations.append(f"Country: {show.getCountryCode()}\n")
                        recommendations.append(f"Date Added: {show.getDateAdded()}\n")
                        recommendations.append(f"Release Year: {show.getReleaseYear()}\n")
                        recommendations.append(f"Duration: {show.getDuration()}\n")
                        recommendations.append(f"Genre: {show.getGenre()}\n")
                        recommendations.append(f"Description: {show.getDescription()}\n")
                        recommendations.append("************************************")
                        recommendations.append("\n")
            if not recommendations:
                return "No Results"
            else:
                return "\n".join(recommendations)
