__author__ = 'zsherman'

import WeatherData as WD
from WeatherData import enum as E

def main():
    data = WD.WeatherData()
    data.loadFromFile('Corvallis.csv')

if __name__ == '__main__':
    main()