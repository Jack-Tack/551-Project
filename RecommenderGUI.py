# Authors: Ryan DeSantis, Aidan Rudd, Jarrett Aaronson
# Date: 5/3/24
# Description: GUI for the Media For You system
from Recommender import Recommender
import tkinter
from tkinter import ttk

class RecommenderGUI:
    def __init__(self):
        self.__recommender = Recommender()
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Media For You")
        self.__main_window.geometry("1200x800")
        self.__nb = ttk.Notebook(self.__main_window)
        self.__nb.pack(expand=1, fill=tkinter.BOTH)
        self.__movieTab = ttk.Frame(self.__nb)
        self.__showsTab = ttk.Frame(self.__nb)
        self.__booksTab = ttk.Frame(self.__nb)
        self.__searchMovieShow = ttk.Frame(self.__nb)
        self.__searchBook = ttk.Frame(self.__nb)
        self.__recommendations = ttk.Frame(self.__nb)
        self.__nb.add(self.__movieTab, text="Movies")
        self.__nb.add(self.__showsTab, text="TV Shows")
        self.__nb.add(self.__booksTab, text="Books")
        self.__nb.add(self.__searchMovieShow, text="Search Movies/TV")
        self.__nb.add(self.__searchBook, text="Search Books")
        self.__nb.add(self.__recommendations, text="Recommendations")
        self.__movieText = tkinter.Text(self.__movieTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__movieStats = tkinter.Text(self.__movieTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__showsText = tkinter.Text(self.__showsTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__showsStats = tkinter.Text(self.__showsTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__booksText = tkinter.Text(self.__booksTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__booksStats = tkinter.Text(self.__booksTab, wrap=tkinter.WORD, state=tkinter.DISABLED)

        self.__searchTypeLabel = tkinter.Label(self.__searchMovieShow, text="Type")
        self.__options = ["Movie", "TV Show"]
        self.__searchMovieShowComboBox = ttk.Combobox(self.__searchMovieShow, values=self.__options)
        self.__titleLabel = tkinter.Label(self.__searchMovieShow, text="Title:")
        self.__titleEntry = tkinter.Entry(self.__searchMovieShow, width=30)
        self.__directorLabel = tkinter.Label(self.__searchMovieShow, text="Director:")
        self.__directorEntry = tkinter.Entry(self.__searchMovieShow, width=30)
        self.__actorLabel = tkinter.Label(self.__searchMovieShow, text="Actor:")
        self.__actorEntry = tkinter.Entry(self.__searchMovieShow, width=30)
        self.__genreLabel = tkinter.Label(self.__searchMovieShow, text="Genre:")
        self.__genreEntry = tkinter.Entry(self.__searchMovieShow, width=30)
        self.__searchButton = tkinter.Button(self.__searchMovieShow, text="search", command=self.searchShows)
        self.__searchMovieShowResults = tkinter.Text(self.__searchMovieShow, wrap=tkinter.WORD, state=tkinter.DISABLED)

        self.__titleLabelBook = tkinter.Label(self.__searchBook, text="Title:")
        self.__titleEntryBook = tkinter.Entry(self.__searchBook, width=30)
        self.__authorLabel = tkinter.Label(self.__searchBook, text="Author:")
        self.__authorEntry = tkinter.Entry(self.__searchBook, width=30)
        self.__publisherLabel = tkinter.Label(self.__searchBook, text="Publisher:")
        self.__publisherEntry = tkinter.Entry(self.__searchBook, width=30)
        self.__searchBookButton = tkinter.Button(self.__searchBook, text="search", command=self.searchBooks)
        self.__searchBookResults = tkinter.Text(self.__searchBook, wrap=tkinter.WORD, state=tkinter.DISABLED)

        self.__recommenderSearchTypeLabel = tkinter.Label(self.__recommendations, text="Type")
        self.__recommendOptions = ["Movie", "TV Show", "Book"]
        self.__searchRecommendationsComboBox = ttk.Combobox(self.__recommendations, values=self.__recommendOptions)
        self.__recommendTitleLabel = tkinter.Label(self.__recommendations, text="Title:")
        self.__recommendTitleEntry = tkinter.Entry(self.__recommendations, width=30)
        self.__recommendationsButton = tkinter.Button(self.__recommendations, text="Get Recommendations", command=self.getRecommendations)
        self.__recommendationsResults = tkinter.Text(self.__recommendations, wrap=tkinter.WORD, state=tkinter.DISABLED)

        self.__movieText.pack(expand=1, fill=tkinter.BOTH)
        self.__movieStats.pack(expand=1, fill=tkinter.BOTH)

        self.__showsText.pack(expand=1, fill=tkinter.BOTH)
        self.__showsStats.pack(expand=1, fill=tkinter.BOTH)

        self.__booksText.pack(expand=1, fill=tkinter.BOTH)
        self.__booksStats.pack(expand=1, fill=tkinter.BOTH)

        self.__searchTypeLabel.pack(expand=1)
        self.__searchMovieShowComboBox.pack(expand=1)
        self.__titleLabel.pack(expand=1)
        self.__titleEntry.pack(expand=1)
        self.__directorLabel.pack(expand=1)
        self.__directorEntry.pack(expand=1)
        self.__actorLabel.pack(expand=1)
        self.__actorEntry.pack(expand=1)
        self.__genreLabel.pack(expand=1)
        self.__genreEntry.pack(expand=1)
        self.__searchButton.pack(expand=1)
        self.__searchMovieShowResults.pack(expand=1, fill=tkinter.X)

        self.__titleLabelBook.pack(expand=1)
        self.__titleEntryBook.pack(expand=1)
        self.__authorLabel.pack(expand=1)
        self.__authorEntry.pack(expand=1)
        self.__publisherLabel.pack(expand=1)
        self.__publisherEntry.pack(expand=1)
        self.__searchBookButton.pack(expand=1)
        self.__searchBookResults.pack(expand=1, fill=tkinter.X)

        self.__recommenderSearchTypeLabel.pack(expand=1)
        self.__searchRecommendationsComboBox.pack(expand=1)
        self.__recommendTitleLabel.pack(expand=1)
        self.__recommendTitleEntry.pack(expand=1)
        self.__recommendationsButton.pack(expand=1)
        self.__recommendationsResults.pack(expand=1, fill=tkinter.X)

        self.__loadShowsButton = tkinter.Button(self.__main_window, text="Load Shows", command=self.loadShows)
        self.__loadShowsButton.pack(expand=1, side=tkinter.LEFT)
        self.__loadBooksButton = tkinter.Button(self.__main_window, text="Load Books", command=self.loadBooks)
        self.__loadBooksButton.pack(expand=1, side=tkinter.LEFT)

        self.__creditButton = tkinter.Button(self.__main_window, text="Information", command=self.creditInfoBox)
        self.__creditButton.pack(expand=1, side=tkinter.LEFT)

    def loadShows(self):
        self.__movieText.configure(state=tkinter.NORMAL)
        self.__movieStats.configure(state=tkinter.NORMAL)
        self.__showsText.configure(state=tkinter.NORMAL)
        self.__showsStats.configure(state=tkinter.NORMAL)
        self.__movieText.delete("1.0", tkinter.END)
        self.__movieStats.delete("1.0", tkinter.END)
        self.__showsText.delete("1.0", tkinter.END)
        self.__showsStats.delete("1.0", tkinter.END)
        self.__recommender.loadShows()

        showsList = self.__recommender.getTVList()
        movieList = self.__recommender.getMovieList()
        for show in showsList:
            self.__showsText.insert(tkinter.END, show + "\n")
        ratingCount, avgDuration, maxActor, freqGenre = self.__recommender.getTVStats()
        self.__showsStats.insert(tkinter.END, "Ratings:\n")
        for rating, percentage in ratingCount.items():
            self.__showsStats.insert(tkinter.END, f"{rating}: {percentage*100:.2f}%\n")
        self.__showsStats.insert(tkinter.END, "\n")
        self.__showsStats.insert(tkinter.END, "Average Number of Seasons: " + str(avgDuration) + " seasons" + "\n")
        self.__showsStats.insert(tkinter.END, "\n")
        self.__showsStats.insert(tkinter.END, "Most Prolific Actor: " + str(maxActor) + "\n")
        self.__showsStats.insert(tkinter.END, "\n")
        self.__showsStats.insert(tkinter.END, "Most Frequent Genre: " + str(freqGenre) + "\n")
        for movie in movieList:
            self.__movieText.insert(tkinter.END, movie + "\n")
        ratingCount, avgDuration, maxDirector, maxActor, freqGenre = self.__recommender.getMovieStats()
        self.__movieStats.insert(tkinter.END, "Ratings:\n")
        for rating, percentage in ratingCount.items():
            self.__movieStats.insert(tkinter.END, f"{rating}: {percentage*100:.2f}%\n")
        self.__movieStats.insert(tkinter.END, "\n")
        self.__movieStats.insert(tkinter.END, "Average Movie Duration: " + str(avgDuration) + " minutes" + "\n")
        self.__movieStats.insert(tkinter.END, "\n")
        self.__movieStats.insert(tkinter.END, "Most Prolific Director: " + str(maxDirector) + "\n")
        self.__movieStats.insert(tkinter.END, "\n")
        self.__movieStats.insert(tkinter.END, "Most Prolific Actor: " + str(maxActor) + "\n")
        self.__movieStats.insert(tkinter.END, "\n")
        self.__movieStats.insert(tkinter.END, "Most Frequent Genre: " + str(freqGenre) + "\n")
        self.__movieText.configure(state=tkinter.DISABLED)
        self.__movieStats.configure(state=tkinter.DISABLED)
        self.__showsText.configure(state=tkinter.DISABLED)
        self.__showsStats.configure(state=tkinter.DISABLED)

    def loadBooks(self):
        self.__booksText.configure(state=tkinter.NORMAL)
        self.__booksStats.configure(state=tkinter.NORMAL)
        self.__recommender.loadBooks()
        self.__booksText.delete("1.0", tkinter.END)
        self.__booksStats.delete("1.0", tkinter.END)
        bookList = self.__recommender.getBookList()
        for book in bookList:
            self.__booksText.insert(tkinter.END, book + "\n")
        avgPage, maxAuthor, maxPublisher = self.__recommender.getBookStats()
        self.__booksStats.insert(tkinter.END, "Average Page Count: " + str(avgPage) + " pages" + "\n")
        self.__booksStats.insert(tkinter.END, "\n")
        self.__booksStats.insert(tkinter.END, "Most Prolific Author: " + str(maxAuthor) + "\n")
        self.__booksStats.insert(tkinter.END, "\n")
        self.__booksStats.insert(tkinter.END, "Most Prolific Publisher: " + str(maxPublisher) + "\n")
        self.__booksText.configure(state=tkinter.DISABLED)
        self.__booksStats.configure(state=tkinter.DISABLED)

    def searchShows(self):
        self.__searchMovieShowResults.configure(state=tkinter.NORMAL)
        type = self.__searchMovieShowComboBox.get()
        title = self.__titleEntry.get()
        director = self.__directorEntry.get()
        actor = self.__actorEntry.get()
        genre = self.__genreEntry.get()

        # Perform the search using the Recommender's method
        results = self.__recommender.searchTVMovies(type, title, director, actor, genre)

        # Display results
        self.__searchMovieShowResults.delete('1.0', tkinter.END)
        if results == "No Results":
            self.__searchMovieShowResults.insert(tkinter.END, "No results found.\n")
        else:
            for result in results:
                self.__searchMovieShowResults.insert(tkinter.END, f"{result}\n")
        self.__searchMovieShowResults.configure(state=tkinter.DISABLED)

    def searchBooks(self):
        self.__searchBookResults.configure(state=tkinter.NORMAL)
        title = self.__titleEntryBook.get()
        author = self.__authorEntry.get()
        publisher = self.__publisherEntry.get()

        results = self.__recommender.searchBooks(title, author, publisher)

        self.__searchBookResults.delete('1.0', tkinter.END)
        if results == "No Results":
            self.__searchBookResults.insert(tkinter.END, "No results found.\n")
        else:
            for result in results:
                self.__searchBookResults.insert(tkinter.END, f"{result}\n")
        self.__searchBookResults.configure(state=tkinter.DISABLED)

        def getRecommendations(self):
            self.__recommendationsResults.configure(state=tkinter.NORMAL)
            type = self.__searchRecommendationsComboBox.get()
            title = self.__recommendTitleEntry.get()
            recommendations = self.__recommender.getRecommendations(type, title)

            self.__recommendationsResults.delete('1.0', tkinter.END)
            if recommendations:
                for recommendation in recommendations:
                    self.__recommendationsResults.insert(tkinter.END, f"{recommendation}\n")
            else:
                self.__recommendationsResults.insert(tkinter.END, "No recommendations found.\n")
                self.__recommendationsResults.configure(state=tkinter.DISABLED)

    def creditInfoBox(self):
        tkinter.messagebox.showinfo(title="Information",
                                    message="Programmers: Ryan DeSantis, Jarrett Aaronson, Aidan Rudd\n Completetion Date: 5/5/2024")

def main():
    app = RecommenderGUI()
    tkinter.mainloop()

main()
