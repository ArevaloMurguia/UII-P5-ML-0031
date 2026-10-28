import numpy as np
import pandas as pd
# ---- Arevalo Rafael NC:0031 Fecha:28/10/26 ----
## Datos Matrtiz 4 x 3
Datos_Alumnos = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# Poner nombre a las columnas
# Y almacenar la tabla en la variable df DataFrame
print("---- Datos a partir de una matriz de 4 x 3 ---- ")
df=pd.DataFrame(Datos_Alumnos,columns=['ci','Marcas','Paquete'])
print(df)
# Datos a partir de un diccionario 
print("---- Datos a partir de un diccionario ---- ")
Alumno_Diccionario = {
    "Nombre":["Eliseo","Joel","Pedro","Nicole","Dylan","Jesse"],
    "Califa":[60,90,100,80,70,50],
    "Edad":[64,15,16,16,18,14]
}

Estudiantes = pd.DataFrame(Alumno_Diccionario)
print(Estudiantes)

print("---- Arevalo Rafael NC:0031 ----")