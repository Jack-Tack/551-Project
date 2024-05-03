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
        self.__nb.add(self.__movieTab, text="Movies")
        self.__movieText = tkinter.Text(self.__movieTab, wrap=tkinter.WORD)
        self.__movieStats = tkinter.Text(self.__movieTab, wrap=tkinter.WORD)
        self.__movieText.pack()
        self.__movieStats.pack()


def main():
    app = RecommenderGUI()
    tkinter.mainloop()


main()







