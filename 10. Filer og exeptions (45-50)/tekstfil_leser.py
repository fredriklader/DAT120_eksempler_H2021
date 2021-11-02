# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:19:25 2021

@author: Erlend Tøssebro
"""

filnavn = input("Hvilken fil skal leses? ")
fila = open(filnavn, "r", encoding="UTF8")
for linje in fila:
    print(linje, end="")
fila.close()
