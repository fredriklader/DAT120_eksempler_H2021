# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:12:59 2021

@author: Erlend Tøssebro
"""

fortsetter = True
while fortsetter:
    filnavn = input("Hvilken fil skal leses? ")
    try:
        fila = open(filnavn, "r", encoding="UTF8")
        fortsetter = False
    except FileNotFoundError:
        print("Kan ikke finne fila")
        print("prøv på nytt")
    
summen = 0
for linje in fila:
    try:
        summen += int(linje)
    except ValueError:
        print("Fant ei linje som ikke kan tolkes som et tall!")
fila.close()
print(f"Summen ble: {summen}")
