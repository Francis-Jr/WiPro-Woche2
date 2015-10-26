# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:38:55 2015

@author: jakobunfried
"""

""" 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Bitweise Operationen %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print("\n \n Bitweise Operatoren\n")

print(3<<2) #in Binär : 011 << 2 = 1100

#Bitweise logik: '&' bitwise and ; '|' bitwise or ; ‘^‘ bitwise XOR ; '~' complement
print(3&2) # 011 & 010 = 010
print(3|2) # 011 | 010 = 011
print(3^2) # 011 ^ 010 = 001
print(~3)  # komlizierter... (Vorzeichen bit wird auch umgedreht etc...)

""" 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%      Modul math      %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print("\n \n Modul math\n")

import math
print(math.sqrt(2))
print(math.pi)

from math import sqrt
print(sqrt(2)) #ohne Extra Paketaufruf

""" 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%        Strings       %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print("\n \n Strings\n")

s1 = "bla"
s2 = "blabla"
print(s1 + s2)
print(3*s1)
print(s2[1]+s1[2]) #Achtung erster Index ist Null
print(s2[1:3]) #Achtung 3 gehört nicht dazu! "dazwischen:
# +---+---+---+---+---+---+
# | b | l | a | b | l | a |
# 0---1---2---3---4---5---6

print(s2[-2]) #von hinten
print(s2[3:])
print(s2[0:-1:2]) #von Index 0 (=ersten) bis zum letzten in 2er Schritten

#s1[2] = "4"   geht so nicht!

print(len(s2))

s = "   Frodo and Sam an Bilbo"
print(s.strip())
print(s.strip().center(len(s.strip())+4))
print(s.find("Bilbo"))
print(s.find("Nemo"))
print(s.find("and"))
print(s.rfind("and"))


""" 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%     Print-Mehtode    %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print("\n \n Print-Mehtode\n")
a = 3 ; b = 4.5 ; c ="text"
print a,b,c #fügt ' ' ein

print "int: %d, float: %f und string: %s " % (4 , 3.5 , 'Bla')

a=7.357
print "%f, %.2f, %8.1f" % (a,a,a)
print "23%%f und %f" % (2.1)

""" 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%         Tupel        %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print("\n \n Tupel\n")

t = (1, "zwei" , (3,4,5)) #beliebige Objekte, Tupel sind auch Objekte
print t[1]
print t[1][2]
print t[2][0]

""" 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%        Listen        %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print("\n \n Listen\n")
# Unterschied zu Tupeln: beschreibar, aber nicht sehr effizient
l = [1,"zwei",(3,4,5)]
print l[0]
l[0] = "eins"
print l[0]
l.append("sechs")
print(l[3])
l.insert(2,"zweieinhalb")
print l
l.pop() # löscht das letzte
print l

"""
bisschen was fehlt noch, musste früher gehen
"""