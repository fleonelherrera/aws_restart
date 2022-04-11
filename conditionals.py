userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply=="yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    
# Ejercicios adicionales
# 1) Realizar un programa que solicite al usuario el nombre de un pais y luego muestre en consola cual es la capital. si el pais empieza con A le debe mostrar el mensaje
# "el pais digitado esta seleccionado para donaciones" CREAR DICCIONARIO

paises = {
    "Argentina": "Buenos Aires",
    "Bolivia": "Sucre",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Ecuador": "Quito",
    "Paraguay": "Asuncion",
    "Peru": "Lima",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas",
}

pais = input("Ingrese un pais de Latinoamerica: ")
if pais=="Argentina" or pais[0]=="A":
    print("Su capital es: ", paises["Argentina"])
elif pais=="Bolivia":
    print("Su capital es: ", paises["Bolivia"])
elif pais=="Chile":
    print("Su capital es: ", paises["Chile"])
elif pais=="Ecuador":
    print("Su capital es: ", paises["Ecuador"])
elif pais=="Paraguay":
    print("Su capital es: ", paises["Paraguay"])
elif pais=="Peru":
    print("Su capital es: ", paises["Peru"])
elif pais=="Uruguay":
    print("Su capital es: ", paises["Uruguay"])
elif pais=="Venezuela":
    print("Su capital es: ", paises["Venezuela"])
elif pais=="Brasil":
    print("Su capital es: ", paises["Brasil"])
else:
    print("El pais ingresado no pertenece a Latinoamerica :(")

