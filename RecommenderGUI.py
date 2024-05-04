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
        self.__nb.add(self.__movieTab, text="Movies")
        self.__nb.add(self.__showsTab, text="TV Shows")
        self.__nb.add(self.__booksTab, text="Books")
        self.__movieText = tkinter.Text(self.__movieTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__movieStats = tkinter.Text(self.__movieTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__showsText = tkinter.Text(self.__showsTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__showsStats = tkinter.Text(self.__showsTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__booksText = tkinter.Text(self.__booksTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__booksStats = tkinter.Text(self.__booksTab, wrap=tkinter.WORD, state=tkinter.DISABLED)
        self.__movieText.pack(expand=1, fill=tkinter.BOTH)
        self.__movieStats.pack(expand=1, fill=tkinter.BOTH)
        self.__showsText.pack(expand=1, fill=tkinter.BOTH)
        self.__showsStats.pack(expand=1, fill=tkinter.BOTH)
        self.__booksText.pack(expand=1, fill=tkinter.BOTH)
        self.__booksStats.pack(expand=1, fill=tkinter.BOTH)
        self.__loadShowsButton = tkinter.Button(self.__main_window, text="Load Shows", command=self.loadShows)
        self.__loadShowsButton.pack(expand=1)
        self.__loadBooksButton = tkinter.Button(self.__main_window, text="Load Books", command=self.loadBooks)
        self.__loadBooksButton.pack(expand=1)

    def loadShows(self):
        self.__movieText.configure(state=tkinter.NORMAL)
        self.__movieStats.configure(state=tkinter.NORMAL)
        self.__showsText.configure(state=tkinter.NORMAL)
        self.__showsStats.configure(state=tkinter.NORMAL)
        self.__recommender.loadShows()
        self.__movieText.delete("1.0", tkinter.END)
        self.__movieStats.delete("1.0", tkinter.END)
        self.__showsText.delete("1.0", tkinter.END)
        self.__showsStats.delete("1.0", tkinter.END)
        showsList = self.__recommender.getTVList()
        movieList = self.__recommender.getMovieList()
        for show in showsList:
            self.__showsText.insert(tkinter.END, show + "\n")
        ratingCount, avgDuration, maxActor, freqGenre = self.__recommender.getTVStats()
        self.__showsStats.insert(tkinter.END, "Ratings:\n")
        for rating, percentage in ratingCount.items():
            self.__showsStats.insert(tkinter.END, f"{rating}: {percentage*100}%\n")
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
            self.__movieStats.insert(tkinter.END, f"{rating}: {percentage*100}%\n")
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
def main():
    app = RecommenderGUI()
    tkinter.mainloop()

main()
