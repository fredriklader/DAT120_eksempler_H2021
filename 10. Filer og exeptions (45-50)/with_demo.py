# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:25:23 2021

@author: Erlend Tøssebro
"""

filnavn = input("Hvilken fil skal leses? ")
fila = 0
try:
    with open(filnavn, "r", encoding="UTF8") as fila:
        summen = 0
        for linje in fila:
            summen += int(linje)
        print(f"Summen ble: {summen}")
except FileNotFoundError:
    print("Finner ikke denne fila!")
except ValueError:
    print("Fila har feil format")
except:
    print("En annen feil har oppstått")

