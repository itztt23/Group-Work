__author__ = 'zsherman'

import csv

class WeatherData:
    def __init__(self):
        self._data = []
        self._count = 0

    def loadFromFile(self, filename):
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self._count += 1
                self._data.append(row)
        #removes the label entry
        self._data.pop(0);

    def prettyPrint(self):
        for row in self._data:
            print(row)

class enum:
    STATION = 0
    DATE = 1
    TMAX = 2
    TMIN = 3
    YEAR = 4
    MONTH = 5
    DAY = 6
    AVERAGE = 7
    DAYS_SINCE_START = 8