__author__ = 'zsherman'

import WeatherData as WD
from pulp import *
import math
import time

def main():
    data = WD.WeatherData()

    data.loadFromFile('Salem.csv')

    #starting linear programming crap
    prob = LpProblem("min abs dev", LpMinimize)
    x0 = LpVariable("x0")
    x1 = LpVariable("x1")
    x2 = LpVariable("x2")
    x3 = LpVariable("x3")
    x4 = LpVariable("x4")
    x5 = LpVariable("x5")
    tvar = LpVariable("tvar")
    prob += tvar

    DAY = 1
    TEMP = 0

    #Use
    points = data._pairs
    print(points)
    for P in points:
        prob += (P[TEMP] - ((x0 + x1 * P[DAY]) + (x2 * math.cos((2*math.pi*P[DAY])/365.25) + x3 * math.sin((2*math.pi*P[DAY])/365.25)) + (x4*math.cos((2*math.pi*P[DAY])/(365.25*10.7)) + x5*math.sin((2*math.pi*P[DAY])/(365.25*10.7))))) <= tvar
        prob += (P[TEMP] - ((x0 + x1 * P[DAY]) + (x2 * math.cos((2*math.pi*P[DAY])/365.25) + x3 * math.sin((2*math.pi*P[DAY])/365.25)) + (x4*math.cos((2*math.pi*P[DAY])/(365.25*10.7)) + x5*math.sin((2*math.pi*P[DAY])/(365.25*10.7))))) >= -tvar

    status = prob.solve()

    print(value(x0))
    print(value(x1))
    print(value(x2))
    print(value(x3))
    print(value(x4))
    print(value(x5))


if __name__ == '__main__':
    main()