"""
Ejercicio nivel 2: Cupibook: La nueva red social
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""

def crear_amigo( nombre: str, fecha_de_nacimiento: int,
                 genero: str, genero_musical_favorito: str,
                 genero_literario_favorito: str,
                 numero_de_likes: int,
                 numero_de_publicaciones: int, cantidad_de_amigos: int,
                 bloqueado: bool) -> dict:
    amigo = {"nombre":nombre, 
             "fecha_de_nacimiento":fecha_de_nacimiento, 
             "signo_zodiacal": asignar_signo_zodiacal(fecha_de_nacimiento),
             "genero":genero, 
             "genero_musical_favorito":genero_musical_favorito, 
             "genero_literario_favorito":genero_literario_favorito, 
             "numero_de_likes":numero_de_likes, 
             "numero_de_publicaciones":numero_de_publicaciones, 
             "cantidad_de_amigos":cantidad_de_amigos, 
             "bloqueado":bloqueado}
    return amigo

def buscar_amigo_por_nombre( nombre:str, a1: dict, a2: dict, a3: dict, 
                            a4: dict ) -> dict:
    if nombre == a1["nombre"]:
        busqueda = a1
    elif nombre == a2["nombre"]:
        busqueda = a2
    elif nombre == a3["nombre"]:
        busqueda = a3
    elif nombre == a4["nombre"]:
        busqueda = a4
    else:
        busqueda = None
    return busqueda

def buscar_amigo_con_mas_likes( a1: dict, a2: dict, a3: dict,
                               a4: dict ) -> dict:
    amigo_mas_likes = a1
    max_likes = a1["numero_de_likes"]
    if a2["numero_de_likes"] > max_likes:
        amigo_mas_likes = a2
        max_likes = a2["numero_de_likes"]
    if a3["numero_de_likes"] > max_likes:
        amigo_mas_likes = a3
        max_likes = a3["numero_de_likes"]
    if a4["numero_de_likes"] > max_likes:
        amigo_mas_likes = a4
        max_likes = a4["numero_de_likes"]
    return amigo_mas_likes

def buscar_amigo_con_menos_publicaciones( a1: dict, a2: dict, a3: dict,
                                         a4: dict ) -> dict:
    amigo_menos_pub = a1
    min_pub = a1["numero_de_publicaciones"]
    if a2["numero_de_publicaciones"] < min_pub:
        amigo_menos_pub = a2
        min_pub = a2["numero_de_publicaciones"]
    if a3["numero_de_publicaciones"] < min_pub:
        amigo_menos_pub = a3
        min_pub = a3["numero_de_publicaciones"]
    if a4["numero_de_publicaciones"] < min_pub:
        amigo_menos_pub = a4
        min_pub = a4["numero_de_publicaciones"]
    return amigo_menos_pub

def asignar_signo_zodiacal( fecha: int ) -> str:
    mes = (fecha % 10000) // 100
    dia = fecha % 100
    
    if (mes == 3 and dia >= 21) or (mes == 4 and dia < 21):
        signo = "Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia < 22):
        signo = "Tauro"
    elif (mes == 5 and dia >= 22) or (mes == 6 and dia < 22):
        signo = "Géminis"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia < 23):
         signo = "Cáncer"       
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia < 23):
         signo = "Leo"       
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia < 23):
         signo = "Virgo"       
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia < 23):
        signo = "Libra"        
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia < 23):
         signo = "Escorpio"       
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia < 22):
          signo = "Sagitario"      
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia < 21):
          signo = "Capricornio"      
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia < 20):
        signo = "Acuario"       
    elif (mes == 2 and dia >= 20) or (mes == 3 and dia < 21):
        signo = "Piscis"      
        
    return signo

def es_cupiamigo( amigo1: dict , amigo2: dict) -> bool:
    c1 = amigo1["cantidad_de_amigos"] >= 3 and amigo2["cantidad_de_amigos"] >= 3
    c2 = amigo1["bloqueado"] == False and amigo2["bloqueado"] == False
    c3 = (amigo1["genero_musical_favorito"] == amigo2["genero_musical_favorito"]) and (amigo1["genero_literario_favorito"] == amigo2["genero_literario_favorito"])
    c4 = signo_es_compatible(amigo1, amigo2)
    return c1 and c2 and c3 and c4

def es_cupienemigo( amigo:dict ) -> bool:
    return (amigo["bloqueado"] == True) or (amigo["numero_de_likes"] < 5 and amigo["cantidad_de_amigos"] == 0) 

def signo_es_compatible( amigo1: dict, amigo2: dict ) -> bool:
    c1 = (amigo1["signo_zodiacal"] == "Aries") and (amigo2["signo_zodiacal"] == ("Géminis" or "Leo" or "Libra" or "Sagitario"))
    c2 = (amigo1["signo_zodiacal"] == "Tauro") and (amigo2["signo_zodiacal"] == ("Tauro" or "Cáncer" or "Virgo" or "Libra" or "Escorpio" or "Capricornio" or "Piscis"))
    c3 = (amigo1["signo_zodiacal"] == "Géminis") and (amigo2["signo_zodiacal"] == ("Aries" or "Leo" or "Libra" or "Acuario"))
    c4 = (amigo1["signo_zodiacal"] == "Cáncer") and (amigo2["signo_zodiacal"] == ("Tauro" or "Virgo" or "Escorpio" or "Piscis"))
    c5 = (amigo1["signo_zodiacal"] == "Leo") and (amigo2["signo_zodiacal"] == ("Aries" or "Géminis" or "Leo" or "Virgo" or "Libra"))
    c6 = (amigo1["signo_zodiacal"] == "Virgo") and (amigo2["signo_zodiacal"] == ("Tauro" or "Cáncer" or "Leo" or "Virgo" or "Escorpio" or "Capricornio" or "Piscis"))
    c7 = (amigo1["signo_zodiacal"] == "Libra") and (amigo2["signo_zodiacal"] == ("Aries" or "Tauro" or "Géminis" or "Leo" or "Libra" or "Acuario"))
    c8 = (amigo1["signo_zodiacal"] == "Escorpio") and (amigo2["signo_zodiacal"] == ("Tauro" or "Cáncer" or "Virgo" or "Piscis"))
    c9 = (amigo1["signo_zodiacal"] == "Sagitario") and (amigo2["signo_zodiacal"] == ("Aries" or "Sagitario" or "Acuario"))
    c10 = (amigo1["signo_zodiacal"] == "Capricornio") and (amigo2["signo_zodiacal"] == ("Tauro" or "Virgo" or "Piscis"))
    c11 = (amigo1["signo_zodiacal"] == "Acuario") and (amigo2["signo_zodiacal"] == ("Géminis" or "Libra" or "Sagitario" or "Acuario"))
    c12 = (amigo1["signo_zodiacal"] == "Piscis") and (amigo2["signo_zodiacal"] == ("Tauro" or "Cáncer" or "Virgo" or "Escorpio" or "Capricornio"))
    
    return c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8 or c9 or c10 or c11 or c12

def amigo_mas_compatibilidad( a1: dict, a2: dict,
                               a3: dict, a4: dict ) -> dict:
    p_a1 = aux_puntaje_compatibilidad(a1)
    p_a2 = aux_puntaje_compatibilidad(a2)
    p_a3 = aux_puntaje_compatibilidad(a3)
    p_a4 = aux_puntaje_compatibilidad(a4)
    puntaje = {"p_a1":p_a1, "p_a2":p_a2, "p_a3":p_a3, "p_a4":p_a4}
    
    amigo_mas_com = a1
    max_pun = puntaje["p_a1"]
    
    if puntaje["p_a2"] > max_pun:
        amigo_mas_com = a2
        max_pun = puntaje["p_a2"]
    if puntaje["p_a3"] > max_pun:
        amigo_mas_com = a3
        max_pun = puntaje["p_a3"]
    if puntaje["p_a4"] > max_pun:
        amigo_mas_com = a4
        max_pun = puntaje["p_a4"]
        
    return amigo_mas_com

def aux_puntaje_compatibilidad(a:dict)->int:
    puntos = 0
    if a["cantidad_de_amigos"] > 5:
        puntos += 3
    if a["bloqueado"] == True:
        puntos -= 10
    if a["genero_musical_favorito"] == ("pop" or "rap" or "salsa"):
        puntos += 2
    else:
        puntos += 1
    if a["genero_literario_favorito"] == ("drama" or "ciencia ficción"):
        puntos += 1
    elif a["genero_literario_favorito"] == "lírico":
        puntos -= 1
    return puntos

def contar_amigos_con_generos(a1: dict, a2: dict,
                                a3: dict, a4: dict, genero_musical:str,
                                genero_literario: str) -> int:
    conteo = 0
    if (a1["genero_musical_favorito"] == genero_musical) and (a1["genero_literario_favorito"] == genero_literario):
        conteo += 1
    if (a2["genero_musical_favorito"] == genero_musical) and (a2["genero_literario_favorito"] == genero_literario):
        conteo += 1
    if (a3["genero_musical_favorito"] == genero_musical) and (a3["genero_literario_favorito"] == genero_literario):
        conteo += 1
    if (a4["genero_musical_favorito"] == genero_musical) and (a4["genero_literario_favorito"] == genero_literario):
        conteo += 1
    return conteo
