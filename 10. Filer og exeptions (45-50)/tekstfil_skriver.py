# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:56:57 2021

@author: Erlend Tøssebro
"""

teksten = ""
tekstlinje = input("Skriv inn første linje: ")
fila = open("tekstfil.txt", "w", encoding="UTF8")
while tekstlinje != "":
    fila.write(tekstlinje + "\n")
    tekstlinje = input("Skriv inn neste linje: ")
fila.close()
