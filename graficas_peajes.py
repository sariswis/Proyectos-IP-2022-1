# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:53:45 2022

@author: Sarita
"""

import matplotlib.pyplot as plt
import pandas as pd

def cargar_archivo(dataF:str)->pd.DataFrame:
    datos = pd.read_csv(dataF)
    return datos

peajes = cargar_archivo("peajes.csv")
plt.figure()

def graficas(peajes:pd.DataFrame)->None:
    numerico = peajes.iloc[0:5, 4:10]
    print(numerico)
    barras = numerico.plot(kind="bar", figsize=(15, 10))
    apiladas = numerico.plot(kind="bar", stacked=True, figsize=(10, 5))
    horizont = numerico.plot(kind="barh", stacked=True, figsize=(10, 7))
    histograma = numerico.plot(kind="hist", bins=20, figsize=(10, 5))
    hist_x_colum = numerico.hist(figsize=(10, 10), bins=3)
    plt.show()
print(graficas(peajes))
def graficas2(peajes:pd.DataFrame)->None:
    color = {"boxes":"Green", "whiskers":"Orange", "medians":"Red", "caps":"Blue"}
    box_plot = peajes.loc[:, ["TAR_PLENA_I"]].boxplot(color=color, figsize=(12, 8))
    box_plot2 = peajes.loc[:, ["TAR_PLENA_I", "TAR_PLENA_II", "TAR_PLENA_III", "TAR_PLENA_IV", "TAR_PLENA_V"]].plot.box(figsize=(12, 8))
    box_plot3 = peajes.loc[:, ["Departamento", "TAR_PLENA_I"]].boxplot(by="Departamento", rot=90, figsize=(10,6))
    plt.show()
    
def graficas3(peajes:pd.DataFrame)->None:
    solo_cinco = peajes.head()
    box_plot = solo_cinco.boxplot(rot=90, figsize=(10, 6))
    box_plot2 = peajes.loc[:, ["Departamento", "TAR_PLENA_I", "TAR_PLENA_II", "TAR_PLENA_III", "TAR_PLENA_IV", "TAR_PLENA_V"]].boxplot(by="Departamento", rot=90, figsize=(9, 5))
    plt.show()
    
def graficas4(peajes:pd.DataFrame)->None:
    primera = peajes.iloc[:, 4:10].plot(kind="scatter", x="TAR_PLENA_I",  y="TAR_PLENA_II", color="Blue", label="1 vs 2", figsize=(10, 5))
    segunda = peajes.iloc[:, 4:10].plot(kind="scatter", x="TAR_PLENA_I",  y="TAR_PLENA_III", color="Green", label="1 vs 3", ax=primera, figsize=(10, 5))
    tercera = peajes.iloc[:, 4:10].plot(kind="scatter", x="TAR_PLENA_I",  y="TAR_PLENA_IV", color="Red", label="1 vs 4", ax=segunda, figsize=(10, 5))
    matiz = peajes.iloc[:, 4:10].plot(kind="scatter", x="TAR_PLENA_I",  y="TAR_PLENA_II", c="TAR_PLENA_III", s=peajes["TAR_PLENA_IV"]/110, figsize=(10, 5))
    matriz_graficas = pd.plotting.scatter_matrix(peajes.iloc[:, 4:8], figsize=(12, 7), diagonal="hist", s=150)


