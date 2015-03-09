__author__ = 'zsherman'

import csv

class WeatherData:
    def __init__(self):
        self._data = []
        self._pairs = []
        self._count = 0

    def loadFromFile(self, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self._count += 1
                self._data.append(row)
                try:
                    self._pairs.append([float(row[-2]), int(row[-1])])
                except ValueError:
                    print("Caught value error: " + row[-2] + row[-1])

        #removes the label entry
        self._data.pop(0);

    def prettyPrint(self):
        for row in self._data:
            print(row)

    def cleanData(self, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            newData = []
            for row in reader:
                date = row[2]
                try:
                    year = int(date[0:4])
                    month = int(date[4:6])
                    day =  int(date[6:])
                    newRow = [row[0], row[1], year, month, day, row[3], row[4]]
                    newData.append(newRow)
                except:
                    print("Oops!")

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in newData:
                writer.writerow(row)



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