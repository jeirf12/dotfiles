import random
import time

def introduccion():
    print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")

def cheqcueva(CambiarCueva):
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)

    FriendlyCueva = random.randint (1, 2)

    global puntaje
    global bandera
    if CambiarCueva == str(FriendlyCueva):
        puntaje +=100
        print ("Te entrega el tesoro...")
    else:
        bandera = True
        print ("El dragon te come de un bocado....")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("¿A que cueva quieres entrar? 1 o 2?")
        cueva = input()

    return cueva

puntaje = 0
bandera = False

EmpezarNuevo = ("si")

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):

    introduccion()

    NumCaverna = CambiarCueva()

    cheqcueva(NumCaverna)

    if puntaje !=0 and bandera:
        print(f'Tu puntaje total es de: {puntaje}')

    print ("Quieres jugar de nuevo? (si o no)")
    EmpezarNuevo = input()


