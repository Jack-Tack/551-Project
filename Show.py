# Authors: Ryan Desantis, Aidan Rudd, Jarrett Aaronson
# Date: 4/24/24
# Description: Show class that is a subclass of Media from Media.py
from Media import Media

class Show(Media):
    def __init__(self, id, title, rating, directors, actors, countryCode, dateAdded, releaseYear, showRate, duration, genre, description):
        super().__init__(id, title, rating)
        self.__directors = directors
        self.__actors = actors
        self.__countryCode = countryCode
        self.__dateAdded = dateAdded
        self.__releaseYear = releaseYear
        self.__showRate = showRate
        self.__duration = duration
        self.__genre = genre
        self.__description = description

    def getDirectors(self):
        return self.__directors

    def setDirectors(self, directors):
        self.__directors = directors

    def getActors(self):
        return self.__actors

    def setActors(self, actors):
        self.__actors = actors

    def getCountryCode(self):
        return self.__countryCode

    def setCountryCode(self, countryCode):
        self.__countryCode = countryCode

    def getDateAdded(self):
        return self.__dateAdded

    def setDateAdded(self, dateAdded):
        self.__dateAdded = dateAdded

    def getReleaseYear(self):
        return self.__releaseYear

    def setReleaseYear(self, releaseYear):
        self.__releaseYear = releaseYear

    def getShowRate(self):
        return self.__releaseYear

    def setShowRate(self, showRate):
        self.__showRate = showRate

    def getDuration(self):
        return self.__duration

    def setDuration(self, duration):
        self.__duration = duration

    def getGenre(self):
        return self.__genre

    def setGenre(self, genre):
        self.__genre = genre

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

