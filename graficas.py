# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:07:44 2022

@author: Sarita
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def valor_dia()->None:
    plt.plot([1, 2, 3, 4],[10,12,16,24])
    plt.ylabel("Valor")
    plt.xlabel("Día")
    plt.show()
    
def evol_amigos()->None:
    num_amigos = [3,2,4,5,2]
    meses = [1,2,3,4,5]
    plt.plot(meses,num_amigos)
    plt.ylabel("Título eje y")
    plt.xlabel("Título eje x")
    plt.show()
    
def estilo_graf()->None:
    t = np.arange(0., 5., 0.25)
    plt.suptitle('Crecimiento Diario')
    plt.ylabel('Valor')
    plt.xlabel('Día')
    plt.plot(t, t, 'r--')
    plt.plot(t, t**2, 'b^')
    plt.plot(t, t**3, "go")
    plt.show()
    
def amigos_reunion()->None:
    num_amigos = [3,2,4,5,2]
    num_reuniones = []
    for i in num_amigos:
        num_reuniones.append(i ** 2)
    meses = [1,2,3,4,5]
    plt.plot(meses,num_amigos,"ro")
    plt.plot(meses,num_reuniones,"b^")
    plt.ylabel("Título eje y")
    plt.xlabel("Título eje x")
    plt.show()

def concentracion_consultas()->None:
    # t = eje x, b = eje y
    # c = color, s = size
    plt.suptitle('Concentración de Consultas')
    plt.ylabel('Concentración')
    plt.xlabel('Día')
    data = {'t': np.arange(0,40,1),
            'c': np.random.randint(0, 100, 40),
            's': np.random.randn(40)}
    data['b'] = [1] * 40
    data['s'] = abs(data["s"]) * np.random.randint(1,500)
    plt.scatter('t', 'b', c='c', s='s', data=data)
    plt.show()
    
def concentracion_consultas2()->None:
    plt.suptitle('Concentración de Consultas')
    plt.ylabel('Concentración')
    plt.xlabel('Día')
    data = {'t': np.arange(0,10,1),
            'color': [40,50,80,90,100,30,70,10,20,10],
            's': np.random.randn(10)}
    data['b'] = [1] * 10
    data['s'] = abs(data['s']) * np.random.randint(1,500)
    plt.scatter('t', 'b', c='color', s='s', data=data)
    plt.show()
    
def concentracion_amigos()->None:
    plt.figure()
    plt.suptitle('Concentración de Amistades')
    plt.ylabel('Concentración')
    plt.xlabel('Mes')
    x = [1,2,3,4,5]
    y = [1,1,1,1,1]
    c = [10,30,50,70,90]
    num_amigos = [3,2,4,5,2]
    s = []
    for i in num_amigos:
        s.append(i * 100)
    data = {'t': x, 'b': y, 'c':c, 's':s}
    plt.scatter('t', 'b', c='c', s='s', data=data)
    plt.show()
    
def subplots_y_variables_categoricas()->None:
    nombres = ['0-17', '18-50', '50-80']
    valores = [15, 35, 50]
    data = {'t': nombres,
    'b': valores,
    'c': [20,80,60 ],
    's': 64.0}
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(nombres, valores)
    plt.subplot(132)
    plt.scatter('t', 'b', c = 'c', s='s', data=data)
    plt.subplot(133)
    plt.plot(nombres, valores)
    plt.suptitle('Variables con Nombre')
    plt.show()
    
def pintar_imagen(imagen:list) -> None:
    plt.imshow(imagen, vmin=0, vmax=255)
    plt.figure()
    
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b] 

def matriz_colorida(tam:int)->list:
    matriz = []
    i = 0
    while i < tam:
        fila = []
        j = 0
        while j < tam:
            fila.append(rand_color())
            j += 1
        matriz.append(fila)
        i += 1
    return matriz

def mitades_i_y_d(tam:int, c1:list, c2:list)->list:
    final = []
    i = 0
    while i < tam:
        fila = []
        j = 0
        while j < tam:
            if j < tam/2:
                fila.append(c1)
            else:
                fila.append(c2)
            j += 1           
        final.append(fila)
        i += 1
    return final

def mitades_a_y_b(tam:int, c1:list, c2:list)->list:
    final = []
    i = 0
    while i < tam:
        fila = []
        j = 0
        while j < tam:
            if i < tam/2:
                fila.append(c1)
            else:
                fila.append(c2)
            j += 1           
        final.append(fila)
        i += 1
    return final

def espejo_eje_vertical(matriz:list)->list:
    tam = len(matriz)
    i = 0
    while i < tam:
        j1 = 0
        j2 = tam - 1
        while j1 < tam/2:
            temp = matriz[i][j1]
            matriz[i][j1] = matriz[i][j2]
            matriz[i][j2] = temp
            j1 += 1    
            j2 -= 1
        i += 1
    return matriz

def espejo_eje_horizontal(matriz:list)->list:
    #intercambiar fila completa
    tam = len(matriz)
    i1 = 0
    i2 = tam - 1
    while i1 < tam/2:
        temp = matriz[i1]
        matriz[i1] = matriz[i2]
        matriz[i2] = temp
        i1 += 1
        i2 -= 1
    return matriz

def cuadrante_inferior_derecho(matriz:list, coord:tuple)->list:
    #pintar por filas desde la misma columna
    tam = len(matriz)
    i = coord[0]
    while i < tam:
        j = coord[1]
        while j < tam:
            matriz[i][j] = [0, 0, 0]
            j += 1
        i += 1
    return matriz

def diagonal_derecha_negra(matriz:list)->list:
    tam = len(matriz)
    i = 0
    while i < tam - 1:
        j = i + 1
        while j < tam:
            matriz[i][j] = [0, 0, 0]
            j += 1
        i += 1
    return matriz

def color_prom_celda(cel_y_vec:list)->list:
    acumr, acumg, acumb = 0, 0, 0
    tam = len(cel_y_vec)
    i = 0
    for celda in cel_y_vec:
        acumr += celda[0]
        acumg += celda[1]
        acumb += celda[2]
        i += 1
    final = [round(acumr / tam, 4), round(acumg / tam, 4), round(acumb / tam, 4)]
    return final

def color_promedio(matriz:list)->list:
    final = []
    tam = len(final)
    i1 = 0
    while i1 < tam:
        fila = []
        j1 = 0
        while j1 < tam:
            cel_y_vec = []
            i2 = i1 - 1
            while i2 < i1 + 2:
                j2 = j1 - 1
                while j2 < j1 + 2:
                    if (-1 < i2 < tam) and (-1 < j2 < tam):
                        cel_y_vec.append(matriz[i2][j2])
                    j2 += 1
                i2 += 1
            fila.append(color_prom_celda(cel_y_vec))
            print(fila)
            j1 += 1
        final.append(fila)
        i1 += 1
    return final

imagen = [[[0, 0, 0], [0, 0.2, 0.3], [0.6, 0.4, 0.5]], 
          [[0.8, 0.9, 0.7], [1, 0, 0.5], [0.5, 0.7, 0.2]], 
          [[0.3, 0.9, 0.7], [0.4, 0.3, 0.1], [1, 1, 1]]]
#print(pintar_imagen(imagen))
proceso = color_promedio(imagen)
print(proceso)
#print(pintar_imagen(proceso))