myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("Whats your name? ")
print(name)

color = input("What is your favourite color? ")
animal = input("What is your favourite animal? ")
print("{}, you like a {} {}!" .format(name, color, animal))


# Ejercicios adicionales
# 1) Escribir un programa que pregunte el nombre completo del usuario en la consola y luego muestre por pantalla el nombre completo del usuario tres veces, una con todas letras minúsculas,
# otra con todas letras mayusculas y otra solo con la primera letra del nombre y de los apellidos en mayuscula. El usuario puede introducir su nombre combinando mayusculas y minusculas como quiera

nombreCompleto = input("Ingrese su nombre completo: ")
nombreMinuscula = nombreCompleto.lower()
nombreMayuscula = nombreCompleto.upper()
nombreMinYMayus = nombreCompleto.title()
print("Su nombre en minusculas: ", nombreMinuscula)
print("Su nombre en mayusculas: ", nombreMayuscula)
print("Su nombre con las mayusculas y minusculas correspondientes: ", nombreMinYMayus)

# 2) Escribir un programa que pregunte el nombre del usuario en la consola y despues de que el usuario lo introduzca muestre por pantalla NOMBRE tiene N letras donde NOMBRE es el nombre de usuario
# en mayusculas y N es el numero de letras que tiene el nombre

nombre = input("Ingrese su nombre: ")
nombreMayuscula = nombre.upper()
N = int(len(nombre))
print(nombreMayuscula, " tiene ", N, " letras")

# 3) Los telefonos de una empresa tienen el siguiente formato prefijo-numer-extension donde el prefijo es el codigo del pais mas 34, la extension tiene 2 digitos ej: +34-913724710-56.
# escribir un programa que pregunte por un numero de telefono con este formato y muestre por pantalla el numero de telefono sin el prefijo y la extension

telefono = input("Ingrese un numero de telefono en el formato prefijo-numero-extension: ")
arrayTelefono = telefono.split("-")
print("Numero sin prefijo ni extension: ", arrayTelefono[1])