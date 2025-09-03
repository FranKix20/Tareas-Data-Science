import pandas as pd

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Carlos", "notas": [4.5, 5.0, 6.2]},
    {"nombre": "Beatriz", "notas": [6.8, 6.9, 6.7]},
    {"nombre": "Diego", "notas": [3.2, 4.5, 5.1]},
    {"nombre": "Elena", "notas": [7.0, 6.5, 6.9]},
    {"nombre": "Fernando", "notas": [2.5, 3.0, 4.2]},
    {"nombre": "Gabriela", "notas": [5.6, 6.0, 5.9]},
    {"nombre": "Héctor", "notas": [4.8, 5.2, 4.9]},
    {"nombre": "Isabel", "notas": [6.3, 6.7, 6.0]},
    {"nombre": "Javier", "notas": [3.5, 4.0, 3.8]},
    {"nombre": "Karla", "notas": [5.7, 6.1, 5.5]},
    {"nombre": "Luis", "notas": [2.8, 3.6, 4.0]},
    {"nombre": "María", "notas": [7.0, 6.8, 6.9]},
    {"nombre": "Nicolás", "notas": [3.9, 4.2, 4.5]},
    {"nombre": "Olga", "notas": [5.2, 5.4, 5.6]},
    {"nombre": "Pedro", "notas": [4.4, 4.8, 5.0]},
    {"nombre": "Quintín", "notas": [6.0, 5.8, 6.3]},
    {"nombre": "Raquel", "notas": [4.7, 4.9, 5.1]},
    {"nombre": "Sofía", "notas": [6.6, 6.7, 6.5]},
    {"nombre": "Tomás", "notas": [3.0, 3.5, 4.0]},
    {"nombre": "Úrsula", "notas": [5.9, 6.2, 6.4]},
    {"nombre": "Víctor", "notas": [4.3, 4.6, 4.8]},
    {"nombre": "Wendy", "notas": [6.1, 6.0, 6.3]},
    {"nombre": "Ximena", "notas": [3.7, 3.9, 4.1]},
    {"nombre": "Yahir", "notas": [5.3, 5.5, 5.7]},
    {"nombre": "Zulema", "notas": [6.9, 6.8, 6.7]},
    {"nombre": "Andrés", "notas": [2.0, 3.0, 3.5]},
    {"nombre": "Brenda", "notas": [4.6, 5.1, 4.9]},
    {"nombre": "Cristóbal", "notas": [6.5, 6.3, 6.2]},
    {"nombre": "Daniela", "notas": [5.0, 5.2, 5.4]}
]

df_estudiantes = pd.DataFrame(estudiantes)
df_Notas = df_estudiantes.explode("notas")

#Desafio 1

df_estudiantes["PROMEDIO"] = df_estudiantes["notas"].apply(lambda x: sum(x) / len(x))

mejor_promedio = df_estudiantes.loc[df_estudiantes["PROMEDIO"].idxmax()]
peor_promedio = df_estudiantes.loc[df_estudiantes["PROMEDIO"].idxmin()]

print(df_estudiantes)

print(f"\n\n El mejor promedio entre los estudiantes es\n {mejor_promedio}")
print(f"\n\n El peor promedio entre los estudiantes es\n {peor_promedio}")

#Desafio 2

aprobados = (df_Notas.groupby("nombre")["notas"].min() >= 4.0).sum()
print(f"\n\n la cantidad de aprobados es : {aprobados}")


#Desafio 3
moda = df_Notas.mode()

print(f"\n\n La nota mas frecuente (Moda) es:\n {moda}")

#Desafio 4

mascara_Notas = df_Notas["notas"] < 4.0
estudiantes_Bajo_4 = df_Notas.loc[mascara_Notas, "nombre"].unique

Porcentaje = (len(estudiantes_Bajo_4) / len(df_estudiantes)) * 100

print(f"\n\n El porcentaje de estudiantes con almenos una nota < 4,0 es un:\n {Porcentaje:.2f}%")

#Desafio 5

#Desafio Extra (Calcular el promedio con .mean directamente)