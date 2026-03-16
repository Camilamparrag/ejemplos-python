

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

"""personas = ["cristian", "esteban"]

for i in personas: #i lee cada indice
    print(i)

alumnos = []

while True:
    nombre = input("ingresa un nombre de un alumno :")

    if nombre == "salir":
        break
    alumnos.append(nombre)
    print(alumnos)"""

"""alumnos = ["carlos", "manuel"]

print(alumnos)"""




##diccionarios

#print(len(alumnos))


"""for i in range(1,20,5):
    print(i)"""


#rango si le paso 4 me genera = 0,1,2,3,4
#rango se lo paso 10 = 0,1,2,3,4,5,6,7,8,9


numeros = [1,2,3,4,5,2,3,7,8,4,2,7,9,4,8,1,4,9,7,]
ordenados = sorted(numeros , reverse=True)
print(ordenados)

numero = complex(2,3)
x = 2 + 3j


#splices

print(ordenados[0])

texto = "esto es un texto"

print(texto[::-1])

print(ordenados.count(7))

#diccionarios








