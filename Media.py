# Author's: Ryan DeSantis, Aiden Rudd, Jarrett Aaronson
# Date: 4/23/24
# Description: Media class for Media For You system

class Media:
    def __init__(self, id, title, rating):
        self.__id = id
        self.__title = title
        self.__rating = rating

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getRating(self):
        return self.__rating

    def setRating(self, rating):
        self.__rating = rating

