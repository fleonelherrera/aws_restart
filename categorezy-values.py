myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    
# Ejercicios adicionales
# 1) Escribir un programa que pida al usuario una palabra y la muestre por pantalla 3 veces en minuscula, 3 en mayus y 3 en la primera letra en mayus

palabra = input("Ingrese una palabra: ")
for val in range(3):
    print (palabra.lower())
for val in range(3):
    print (palabra.upper())
for val in range(3):
    print (palabra.title())
    
# 2) Escribir un programa que pida al usuario una palabra y almacene en una lista la palabra como la ingreso el usuario, la palabra en minuscula, la palabra en mayus,
# la palabra con la primer letra en mayus y el tamaño de la palabra. luego imprima cada uno de los valores de la lista

listaPalabras=[]
palabra = input("ingrese una palabra: ")
listaPalabras.append(palabra)
listaPalabras.append(palabra.lower())
listaPalabras.append(palabra.upper())
listaPalabras.append(palabra.title())
listaPalabras.append(len(palabra))
for item in listaPalabras:
    print(item)
    
# 3) Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares desde 1 hasta ese numero separados por comas

num = int(input("Ingrese un numero entero positivo: "))
for val in range(1,num+1,2):
    print(val, end=', ')