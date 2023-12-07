# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

def cargar_archivo(dataF:str)->pd.DataFrame:
    datos = pd.read_csv(dataF)
    return datos

def atributos(peajes:pd.DataFrame)->dict:
    atributos = {
            "type peajes": type(peajes),
            "peajes": peajes,
            "dtypes colum": peajes.dtypes,
            "columns": peajes.columns,
            "axes": peajes.axes,
            "ndim": peajes.ndim,
            "size": peajes.size,
            "shape": peajes.shape, 
            "values numpy": peajes.values
            }
    return atributos

def recorrer(peajes:pd.DataFrame)->tuple:
    columnas = []
    valores_colum = []
    for c in peajes.columns:
        columnas.append(c)
    for d in peajes.Departamento:
        valores_colum.append(d)
    return (columnas, valores_colum)

def metodos(peajes:pd.DataFrame)->dict:
    metodos = {
            "head": peajes.head(),
            "tail": peajes.tail(10),
            "describe": peajes.describe(),
            "max": peajes.max(),
            "min": peajes.min(),
            "mean": peajes.mean(),
            "median": peajes.median(),
            "std desv estand": peajes.std(),
            "sample": peajes.sample(n=3, random_state=1),
            "dropna": peajes.dropna(),
            "unique": peajes["NombreProyecto"].unique()
            }
    return metodos

def seleccion_columna(peajes:pd.DataFrame)->dict:
    selecc = {
            "nombre_atributo": peajes.Departamento,
            "corchetes_comillas": peajes[["Departamento", "NombreProyecto"]]
            }
    return selecc

def seleccion_filas(peajes:pd.DataFrame)->dict:
    selecc = {
            "rango : ": peajes[0:1],
            "1 fila": peajes.iloc[0],
            "ultima fila": peajes.iloc[-1],
            "todas filas": peajes.iloc[:],
            "10 filas de 3 en 3": peajes.iloc[0:10:3],
            "5 filas solo colum 3": peajes.iloc[0:5, 3],
            "5 filas colum 2-4": peajes.iloc[0:5, 2:5],
            "5 filas, colum 2,1,3,5": peajes.iloc[0:5, [2, 1, 3, 5]],
            "todas filas, colum 4-11": peajes.iloc[:, 4:12]
            }
    return selecc

def sorting(peajes:pd.DataFrame)->dict:
    extracto = peajes[0:100:10]
    tarifa = peajes.sort_values(by="TAR_PLENA_I", ascending=False)
    ordenado = {
            "subconjunto": extracto,
            "ord nombre": extracto.sort_values(by="NombreProyecto"),
            "mas caros": tarifa[0:5]
            }
    return ordenado

def filtering(peajes:pd.DataFrame)->dict:
    filtrado = {
                "Filas Cundin": peajes[peajes.Departamento == "CUNDINAMARCA"],
                "Peajes caros Cundin": peajes[peajes.TAR_PLENA_I > 10000][peajes.Departamento == "CUNDINAMARCA"]
                }
    return filtrado

ejecutando = True
while ejecutando:
    peajes = cargar_archivo("peajes.csv")
    print("\nMenú\n1. Cargar\n2. Atributos\n3. Recorrer\n4. Métodos\n5. Selecc Colum\n6. Selecc Filas\n7. Sorting\n8. Filtering\n0. Salir")
    opcion = int(input("Seleccione una opción: "))
    print()
    if opcion == 1:
        print(peajes)
    elif opcion == 2:
        print("ATRIBUTOS\n\n", atributos(peajes))
    elif opcion == 3:
        print("RECORRER\n\n", recorrer(peajes))
    elif opcion == 4:
        print("METODOS\n\n", metodos(peajes))
    elif opcion == 5:
        print("SELECCIÓN\n\n", seleccion_columna(peajes))
    elif opcion == 6:
        print("SELECCIÓN\n\n", seleccion_filas(peajes))
    elif opcion == 7:
        print("SORTING\n\n", sorting(peajes))
    elif opcion == 8:
        print("FILTERING\n\n", filtering(peajes))
    elif opcion == 0:
        ejecutando = False
    else:
        print("No existe")