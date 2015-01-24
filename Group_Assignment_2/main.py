__author__ = 'zsherman'

import Lockers

def main():
    l = Lockers.Locker()
    l.loadFromFile('samples.txt', 7)
    l.prettyPrint()


if __name__ == '__main__':
    main()