# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 08:16:35 2022

@author: ss.cardenas
"""

def factorial(n:int)->int:
    total = 1
    indice = 1
    while indice <= n:
        total = indice * total
        indice += 1
    return total

def es_primo(n:int)->bool:
    if n <= 1:
        rta = False
    elif n == 2:
        rta = True
    else:
        i = 2
        rta = True
        while (n/2) >= i:
            if n % i == 0:
                rta = False
            i += 1
    return rta

def aux_es_primo_adapt(n:int)->bool:
    if n == 2:
        rta = True
    else:
        i = 2
        rta = True
        while (n/2) >= i:
            if n % i == 0:
                rta = False
            i += 1
    return rta
        
def suma_primeros_n_primos(x:int)->int:
    suma = 0
    c_primos = 0
    num = 2
    while c_primos < x and x > 0:
        if aux_es_primo_adapt(num):
            suma += num
            c_primos += 1
        num += 1
    return suma

def fibonacci(n:int)->int:
    indice = 0
    a = 0
    b = 1
    numero = 0
    while indice < n:
        if n == 0:
           numero = 0        
        elif n == 1:
           numero = 1
        else:
            numero = a + b
            a = b
            b = numero
        indice += 1
    return numero

def elevar_e(x:int, n:int)->float:
    suma = 0
    den = 1
    if x > 0 and n > 0:
        suma += 1
        for i in range(1, n):
            num = x ** i
            den = den * i
            suma += num / den
    return suma
