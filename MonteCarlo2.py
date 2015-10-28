# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:41:13 2015

@author: jakobunfried
"""

import math
import random

def calc(epsilon):
    value = math.pi
    iterations = 0.0
    hitcounter = 0.0
    approx = 0.0

    iterations += 1
    x = random.random()
    y = random.random()
    if(x**2 + y**2 <= 1):
        hitcounter +=1
    approx = 4 * hitcounter / iterations    
    
    while( abs(value - approx) > epsilon):
        iterations += 1
        x = random.random()
        y = random.random()
        if(x**2 + y**2 <= 1):
            hitcounter +=1
        approx = 4 * (hitcounter / iterations)
        print"[%d] pi ~ %f" % (iterations,approx)
    print"[DONE] %d Iterationen wurden benötigt" % (iterations)
    

epsilon = raw_input("Wie nah soll approximiert werden? ")
epsilon = float(epsilon)
calc(epsilon)