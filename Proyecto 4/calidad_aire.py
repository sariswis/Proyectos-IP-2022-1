import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.patches as mpatches

def cargar_datos(ruta:str) -> pd.DataFrame:
    datos = pd.read_csv(ruta)
    return datos

def diagrama_de_torta_segun_tipo_de_estacion(datos: pd.DataFrame) -> None:
    estaciones = datos[["Nombre de la estación","Tipo de estación"]].drop_duplicates().sort_values(by="Tipo de estación")
    conteo = estaciones["Tipo de estación"].value_counts(sort=False)
    tipos = np.unique(estaciones["Tipo de estación"])
    resultados = pd.DataFrame({"Tipo de estación":tipos, "Conteo":conteo})
    torta = resultados.plot(kind="pie", y="Conteo", autopct="%1.1f%%", title="Distribución porcentual según tipo de estación", legend=False, ylabel="")
    plt.show()

def tendencia_medidas_por_rango_de_anios(datos: pd.DataFrame, anio_inf: int, anio_sup: int) -> None:
    medidas = datos[["Anio"]][datos.Anio >= anio_inf][datos.Anio <= anio_sup].sort_values(by="Anio")
    anios = list(medidas["Anio"].drop_duplicates())
    c_medidas = list(medidas.groupby("Anio")["Anio"].count())
    resultados = pd.DataFrame({"Anio":anios, "Cantidad":c_medidas})
    resultados.plot.line(x="Anio", y="Cantidad", marker="o", xlabel="Año", ylabel="Número de medidas", xticks=anios, legend=False)
    plt.title("Tendencia de número de medidas de " + str(anio_inf) + " a " + str(anio_sup))
    plt.show()

def diagrama_de_barras_mediciones_o3_mayores_a(datos: pd.DataFrame, cota:float) -> None:
    medidas = datos[datos.Variable == "O3"][datos.Concentración > cota].sort_values(by="Departamento")
    final = medidas["Departamento"].value_counts().head()
    final.plot(kind="barh")
    plt.gca().invert_yaxis()
    plt.title("Top departamentos con mediciones de O^3 mayores a " + str(cota) +" µg/m^3")
    plt.ylabel("Departamento")
    plt.xlabel("Número de medidas superiores a " + str(cota) +" µg/m^3")
    plt.show()
    
def caja_y_bigotes_distribucion_concentraciones_CO_por_año(datos: pd.DataFrame, anio:int) -> None:
    medidas = datos[["Concentración"]][datos.Anio == anio][datos["Tiempo de exposición"] == 8][datos.Variable == "CO"]
    medidas.plot.box(grid=True)
    plt.title("Distribución de medidas de CO por año")
    plt.xlabel(str(anio))
    plt.ylabel("Concentración")
    plt.show()
   
def concentraciones_anuales_PM10_por_departamento(datos: pd.DataFrame, dpto:str) -> None:
    medidas = datos[["Anio", "Concentración"]][datos.Departamento == dpto.upper()][datos.Variable == "PM10"].sort_values(by="Anio")
    anios = list(medidas["Anio"].drop_duplicates())
    concent = list(medidas.groupby("Anio")["Concentración"].mean())
    resultados = pd.DataFrame({"Anio":anios, "Concentración":concent})
    resultados.plot(kind="bar", x="Anio", y="Concentración", legend=False, xlabel="Año", ylabel="Concentración")
    plt.title("Concentración promedio de material particulado menor a 10 micras por años en " + dpto)
    plt.show()
  
def crear_matriz(datos:pd.DataFrame) -> tuple:
    ICAs =sorted(datos["ICA"].unique())
    ICAs_dict = dict(list(enumerate(ICAs)))
    deptos = sorted(datos["Departamento"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    medidas = datos[["Departamento", "ICA"]].sort_values(by="Departamento")
    matriz = []
    tam = len(dept_dict)
    for i in range(tam):
        med_depto = medidas[medidas.Departamento == dept_dict[i]]
        aceptable = med_depto[med_depto.ICA == "Aceptable"]["ICA"].count()
        buena = med_depto[med_depto.ICA == "Buena"]["ICA"].count()
        dañsalud = med_depto[med_depto.ICA == "Dañina a la salud"]["ICA"].count()
        dañsensib = med_depto[med_depto.ICA == "Dañina a la salud de grupos sensibles"]["ICA"].count()
        muydañ = med_depto[med_depto.ICA == "Muy dañina a la salud"]["ICA"].count()
        pelig = med_depto[med_depto.ICA == "Peligrosa"]["ICA"].count()
        fila = [aceptable, buena, dañsalud, dañsensib, muydañ, pelig]
        matriz.append(fila)
    return (matriz, dept_dict, ICAs_dict)

def dar_departamento_con_mas_mediciones(info_matriz: tuple) -> str:
    mayor_cantidad = 0
    depto_mas = ""
    tam = len(info_matriz[0])
    for i in range(tam):
        if sum(info_matriz[0][i]) > mayor_cantidad:
            mayor_cantidad = sum(info_matriz[0][i])
            depto_mas = info_matriz[1][i]
    return depto_mas
   
def contar_numero_de_mediciones_por_ica_dado(info_matriz: tuple, ica_a_buscar:str) -> int:
    j = 0
    tam = len(info_matriz[2])
    encontrado = False
    while j < tam and not(encontrado):
        if info_matriz[2][j] == ica_a_buscar:
            encontrado = True
            j -= 1
        j += 1
    medidas = 0
    for i in info_matriz[0]:
        medidas += i[j]
    return medidas

def mayores_mediciones_ica_y_departamento(info_matriz: tuple) -> tuple:
    tami = len(info_matriz[0])
    tamc = len(info_matriz[0][0])
    mayor_med = 0
    for i in range(tami):
        for j in range(tamc):
            if info_matriz[0][i][j] > mayor_med:
                mayor_med = info_matriz[0][i][j]
                mayor_depto = info_matriz[1][i]
                mayor_ICA = info_matriz[2][j]
    return (mayor_depto, mayor_ICA)

def cargar_coordenadas(nombre_archivo:str)->dict:
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0].upper()] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos

def departamentos_mapa(info_matriz: tuple) -> None:
    coord = cargar_coordenadas("coordenadas.txt")
    mapa = mpimg.imread("mapa.png").tolist()
    
    mayores_ICAs = {}
    tami = len(info_matriz[0])
    tamc = len(info_matriz[0][0])
    for i in range(tami):
        mayor_med = 0
        mayor_ICA = ""
        for j in range(tamc):
            if info_matriz[0][i][j] > mayor_med:
                mayor_med = info_matriz[0][i][j]
                mayor_ICA = info_matriz[2][j]
        mayores_ICAs[info_matriz[1][i]] = mayor_ICA
        
    colores = {"Buena":[36/255,226/255,41/255], "Aceptable":[254/255,253/255,56/255], "Dañina a la salud de grupos sensibles":[252/255,102/255,33/255],"Dañina a la salud":[252/255,20/255,27/255], "Muy dañina a la salud":[127/255,15/255,126/255], "Peligrosa":[101/255, 51/255, 8/255]}    
    for d in mayores_ICAs:
        c_central = coord[d]
        color = colores[mayores_ICAs[d]]
        for i in range(c_central[0] - 6, c_central[0] + 7):
            for j in range(c_central[1] - 6, c_central[1] + 7):
                mapa[i][j] = color
        
    legends = []
    for i in range(len(info_matriz[2])):
        legends.append(mpatches.Patch(color = colores[info_matriz[2][i]], label= info_matriz[2][i]))
    plt.legend(handles = legends, loc = 3, fontsize='x-small')
    plt.imshow(mapa)
    plt.show()