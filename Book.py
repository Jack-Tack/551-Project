# Authors: Ryan DeSantis, Aidan Rudd, Jarrett Aaronson
# Date: 4/23/24
# Description: Book class that is a subclass of Media from Media.py
from Media import Media

class Book(Media):
    def __init__(self, id, title, rating, authors, isbn, isbn13, lang, numPage, numRate, pubDate, pub):
        super().__init__(id, title, rating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__lang = lang
        self.__numPage = numPage
        self.__numRate = numRate
        self.__pubDate = pubDate
        self.__pub = pub

    def getAuthors(self):
        return self.__authors

    def setAuthors(self, authors):
        self.__authors = authors

    def getISBN(self):
        return self.__isbn

    def setISBN(self, isbn):
        self.__isbn = isbn

    def getISBN13(self):
        return self.__isbn13

    def setISBN13(self, isbn13):
        self.__isbn13 = isbn13

    def getLang(self):
        return self.__lang

    def setLang(self, lang):
        self.__lang = lang

    def getNumPage(self):
        return self.__numPage

    def setNumPage(self, numPage):
        self.__numPage = numPage

    def getNumRate(self):
        return self.__numRate

    def setNumRate(self, numRate):
        self.__numRate = numRate

    def getPubDate(self):
        return self.__pubDate

    def setPubDate(self, pubDate):
        self.__pubDate = pubDate

    def getPub(self):
        return self.__pub

    def setPub(self, pub):
        self.__pub = pub
