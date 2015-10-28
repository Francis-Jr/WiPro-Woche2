# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:59:11 2015

@author: jakobunfried
"""

import random
import math

iter = raw_input("Wieviele Zufallspaare pro Berechnung? ")
iter = int(iter)
am = raw_input("Wieviele Berechnungen? ")
am = int(am)

def calcOnce(iterations):
    insidecounter = 0.0
    for i in xrange(iterations):
        x = random.random()
        y = random.random()
        if (x**2 + y**2 < 1):
            insidecounter += 1
    
    return insidecounter/iterations

def calc(iterations,amount):
    sum = 0.0
    ls = [calcOnce(iterations)]
    for i in range(amount-1):
        tmp = calcOnce(iterations)
        sum += tmp
        ls.append(tmp)
        
    print("Werte:")
    print ls
    print("Durchschnitt: %f" ) % (sum/(am-1))
    
calc(iter,am)