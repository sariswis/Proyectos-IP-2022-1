# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:59:24 2022

@author: Sarita
"""

from math import radians, cos, sin, asin, sqrt

def distancia_entre_dos_puntos(lat1:float, lon1:float, lat2:float, lon2:float)->float:
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dif_lon = lon2 - lon1
    dif_lat = lat2 - lat1
    a = sin(dif_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(dif_lon / 2)**2
    c = 2 * asin(sqrt(a))
    return c * 6371

def fecha_a_lista(fecha:str)->list:
    año = int(fecha[0:4])
    mes = int(fecha[5:7])
    dia = int(fecha[8:10])
    l = [año, mes, dia]
    return l

def fecha_en_rango(f_in:list, f_fin:list, fecha:list)->bool:
    esta = False
    if f_in[0] < fecha[0] < f_fin[0]:
        esta = True
    elif f_in[0] == fecha[0]:
        if f_in[1] < fecha[1]:
            esta = True
        elif f_in[1] == fecha[1]:
            if f_in[2] <= fecha[2]:
                esta = True
    elif f_fin[0] == fecha[0]:
        if f_fin[1] > fecha[1]:
            esta = True
        elif f_fin[1] == fecha[1]:
            if f_fin[2] >= fecha[2]:
                esta = True
    return esta

def carga_de_datos(n_archivo:str)->dict:
    avistamientos = {}
    archivo = open(n_archivo, "r", encoding="utf8")
    titulos = archivo.readline()
    
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        name_country = datos[3]
        avistamiento = {}
        avistamiento["datetime"] = datos[0]
        avistamiento["city"] = datos[1]
        avistamiento["state"] = datos[2]
        avistamiento["shape"] = datos[4]
        avistamiento["duration"] = float(datos[5])
        avistamiento["comments"] = datos[6]
        avistamiento["date posted"] = datos[7]
        avistamiento["latitude"] = float(datos[8])
        avistamiento["longitude"] = float(datos[9].strip())
        
        if name_country not in avistamientos.keys():
            avistamientos[name_country] = [avistamiento]
        else:
            avistamientos[name_country].append(avistamiento)
        linea = archivo.readline()
    archivo.close()
    return avistamientos

def avistamientos_en_fecha(avistamientos:dict, fecha:str)->list:
    avist_en_fecha = []
    for l_pais in avistamientos.values():
        for avistamiento in l_pais:
            if fecha == avistamiento["datetime"][0:10]:
                avist_en_fecha.append(avistamiento)
    return avist_en_fecha

def avistamientos_por_ciudad(avistamientos:dict)->dict:
    ciudades = {}
    for l_pais in avistamientos.values():
        for avistamiento in l_pais:
            if avistamiento["city"] not in ciudades.keys():  
                ciudades[avistamiento["city"]] = [avistamiento]
            else:
                ciudades[avistamiento["city"]].append(avistamiento)
    return ciudades

def avistamientos_mas_de_x_segundos(avistamientos:dict, limite:float)->dict:
    avist_con_lim = {}
    for pais in avistamientos.keys():
        avist_con_lim[pais] = []
        for avistamiento in avistamientos[pais]:
            if avistamiento["duration"] > limite:
                avist_con_lim[pais].append(avistamiento)
    return avist_con_lim

def avistamientos_por_rango_de_fechas(avistamientos:dict, fecha_in:str, fecha_fin:str)->list:
    f_in = fecha_a_lista(fecha_in)
    f_fin = fecha_a_lista(fecha_fin)
    avist_en_rango = []
    for l_pais in avistamientos.values():
        for avistamiento in l_pais:
            fecha = fecha_a_lista(avistamiento["datetime"][0:10])
            if fecha_en_rango(f_in, f_fin, fecha):
                avist_en_rango.append(avistamiento)
    return avist_en_rango

def avistamientos_en_radio_determinado(avistamientos:dict, lat:float, long:float, radio:float)->list:
    avist_en_radio = []
    for l_pais in avistamientos.values():
        for avistamiento in l_pais:        
            distancia = distancia_entre_dos_puntos(lat, long, avistamiento["latitude"], avistamiento["longitude"])
            if distancia < radio:
                avist_en_radio.append(avistamiento)
    return avist_en_radio

def minimo_x_avistamientos_en_mes(avistamientos:dict, cantidad_minima:int, fecha:str)->bool:
    hubo_minimo = False
    cant_actual = 0
    for l_pais in avistamientos.values():
        if not(hubo_minimo):
            i = 0
            tam = len(l_pais)
            while i < tam and not(hubo_minimo):
                if l_pais[i]["datetime"][0:7] == fecha:
                    cant_actual += 1
                if cant_actual == cantidad_minima:
                    hubo_minimo = True
                i += 1
    return hubo_minimo

def dar_avistamiento_mas_corto_y_largo_por_pais(avistamientos:dict, pais:str)->dict:
    menor_d = avistamientos[pais][0]["duration"]
    mayor_d = 0
    for avistamiento in avistamientos[pais]:
        duracion = avistamiento["duration"]
        if duracion <= menor_d:
            menor_d = duracion
            corto = avistamiento
        if duracion >= mayor_d:
            mayor_d = duracion
            largo = avistamiento
    avist_pais = {"corto":corto, "largo":largo}
    return avist_pais

def contar_avistamientos_por_forma(avistamientos:dict)->dict:
    avist_forma ={}
    for l_pais in avistamientos.values():
        for avistamiento in l_pais:
            if avistamiento["shape"] not in avist_forma:
                avist_forma[avistamiento["shape"]] = 1
            else:
                avist_forma[avistamiento["shape"]] += 1
    return avist_forma

def pais_con_mas_avistamientos_de_x_segundos(avistamientos:dict, limite:float)->dict:
    avist_superan_lim = avistamientos_mas_de_x_segundos(avistamientos, limite)
    mayor_pais = ""
    mayor_avist = 0
    for pais in avist_superan_lim.keys():
        cant_avist = 0
        for avistamiento in avist_superan_lim[pais]:
            cant_avist += 1
        if cant_avist >= mayor_avist:
            mayor_avist = cant_avist
            mayor_pais = pais
    mayor_num = {"pais":mayor_pais, "avistamientos": mayor_avist}
    return mayor_num

def avistamientos_que_contengan_cadena_en_comentarios(avistamientos:dict, cadena:str)->list:
    contienen_cad = []
    for l_pais in avistamientos.values():
        for avistamiento in l_pais:
            if cadena in avistamiento["comments"]:
                contienen_cad.append(avistamiento)
    return contienen_cad