myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)

myFinalAnswerTuple= ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavouriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}

print(myFavouriteFruitDictionary)
print(type(myFavouriteFruitDictionary))

print(myFavouriteFruitDictionary["Akua"])
print(myFavouriteFruitDictionary["Saanvi"])
print(myFavouriteFruitDictionary["Paulo"])

# Ejercicio adicional 1: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

Asignaturas = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
print(Asignaturas)

# 2) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura>
# es cada una de las asignaturas de la lista.

Asignaturas = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
print("Yo estudio ", Asignaturas[0])
print("Yo estudio ", Asignaturas[1])
print("Yo estudio ", Asignaturas[2])
print("Yo estudio ", Asignaturas[3])
print("Yo estudio ", Asignaturas[4])

# 3) Se requiere solicitar al usuario las ultimas diez notas de su curso de aws. luego es necesario mostrar la media de todas las calificaciones.
# Si la media de las notas es mayor que 70 puntos mostrar el msj FELICIDADES ! APROBASTE. Si la media es inferior a 70 entonces mostrar: recuerda encender la camara :()

Notas = []

for x in range (0,10):
    nota= input("Agregue la nota ", x)
    Notas.append(int(nota))
    
promedio = sum(Notas)/len(Notas)

if promedio>=70:
    print("FELICIDADES ! APROBASTE")
else:
    print("recuerda encender la camara :(")