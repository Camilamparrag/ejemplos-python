

"""print("holaaaaaaaaaaaa")

#VARIABLES

nombre = "Camila"
edad = 33
altura = 1.64
es_profesor = False
ciudad = "Arica"



#TIPOS DE DATOS

str #esto es un texto
int #esto es un entero
float #esto es un flotante o decimal
bool #esto es verdadero o falso

#INPUT
#INPUT()

texto = input()
print(texto)



##Listas
lista = [] ##corchetes son importantes
##
diccionario = {"key":"value"}
##Sets
sets={}
##tuplas
tuplas = ()"""

##Listas
##index
frutas = ["manzana", "uva", "kiwi", "sandia", [1,2,3,4,[5,6,7]]]
    #index    0        1       2       3              4        = posicion

frutas[3] = "pera" #modificar indice
frutas[0] = "melon" #modificar indice
frutas[4] = [] #modificar por una lista vacia 

"""print(frutas[2]) #imprimir lista
print(frutas[1])
print(frutas[0])
print(frutas[4][4][0])"""


#print(dir(frutas))

#print(dir(diccionario))

#append
frutas.append("naranaja")

#remove
frutas.remove("kiwi")

#print(frutas)

personas = ["cristian", "esteban"]

for i in personas: #i lee cada indice
    print(i)

alumnos = []

while True:
    nombre = input("ingresa un nombre de un alumno :")

    if nombre == "salir":
        break
    alumnos.append(nombre)
    print(alumnos)






##diccionarios














