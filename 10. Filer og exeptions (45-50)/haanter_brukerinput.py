# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:44:41 2021

@author: Erlend Tøssebro
"""

fortsetter = True
while fortsetter:
    try:
        tall = int(input("Skriv inn tallet du ønsker fakultet av: "))
        if tall < 0:    
            print("Fakultet for negative tal finnes ikke!")
        else:
            fortsetter = False
    except ValueError:
        print("Du må skrive inn et tall!")

resultat = 1
for i in range(1, tall+1):
    print(i)
    resultat *= i
print("Etter for-løkka er ferdig")
print(resultat)

