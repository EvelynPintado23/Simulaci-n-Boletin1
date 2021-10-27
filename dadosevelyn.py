# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:02:08 2021

@author: Estudiante
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def calcular(lanzamientos):
    
    sumas = []
    
    for i in range(0, lanzamientos):
        
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1+dado2
        sumas.append(suma)
        print(sumas)
    
    plt.title("Sumatorias")
    plt.hist(sumas, bins=60, alpha=1, edgecolor='black')
    plt.show()
    

calcular(10000)   