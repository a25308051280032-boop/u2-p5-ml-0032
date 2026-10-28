import numpy as np
import pandas as pd
# Iris Chavez NC 0032
# datos matriz 
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnasw
# y almacenar la tabla en la variable df dataframe
df=pd.DataFrame(datos_alumno,columns=["ci", "marcas", "paquete"])
print(df)
# datos a partir de un diccionario
alumno_diccionario={ 
    "nombre":["Yahir", "Caleb", "Daniel", "Farfan", "Alexia", "Yeikob"],
   "califa":[90,60,100,60,100,70],
  "edad":[16,15,16,16,17,16]
 }

# convertir el diccionario en Dataframe
estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Iris Chavez NC 0032")