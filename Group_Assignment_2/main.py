__author__ = 'zsherman'

import Lockers

def main():
    for i in range(7):
        l = Lockers.Locker()
        loadfromfile('samples2.txt', i)
        l.prettyprint()
        print l.algorithm_two_dynamic()
        print



if __name__ == '__main__':
    main()