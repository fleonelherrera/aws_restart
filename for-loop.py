print("Count to 10!")

for x in range(0,11):
    print(x)
    
    
# Ejercicios adicionales:
# 1) Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminará

palabra = input("Ingrese una palabra: ")

while palabra != "salir":
    print(palabra)
    palabra = input("Ingrese una palabra: ")
    
    
# 2) Escribir un programa en el que se pregunte al usuario por una frase y una letra y muestre por pantalla el numero de veces que aparece la letra en la frase

frase = input("ingrese una frase: ")
letra = input("ingrese una letra: ")
contLetras = 0
for x in frase:
    if x == letra:
        contLetras+=1
print("La frase ", frase, " tiene ", contLetras, " letras")