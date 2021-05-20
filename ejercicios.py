#Ejercicios Primera Parte

#1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(number1, number2):
    #Primera Version

    # top = number2
    # if number1>number2:
    #     top = number1
    # return top

    #Segunda Version
    return number1 if number1>number2 else number2

#2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def maxThree(number1, number2, number3):
    #Primera Version

    # if number1>number2 and number1>number3:
    #     top = number1
    # elif number2>number1 and number2>number3:
    #     top = number2
    # elif number3>number1 and number3>number2:
    #     top = number3
    # elif number1==number2 or number1==number3:
    #     top = number1

    # return top

    #Segunda Version
    top = max(number1, number2)
    return max(top, number3)

#3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def len(list:list):
    acum = 0
    for i in list:
        acum += 1
    return acum

#4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
import re

def valueCharacter(chain):
    #Primera Version

    value = re.search('[^aeiouAEIOU]', chain)
    if value:
        return False
    return True

    #Segunda Version
    # vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    # return chain in vowels

#5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(list: list, position, answer=0):
    if position>0:
        answer += list[position-1]
        position -= 1
        return sum(list,position,answer)
    return answer

def mult(list: list, position, answer=1):
    if position>0:
        answer *= list[position-1]
        position -=1
        return mult(list,position,answer)
    else:
        return 0

#6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def reverseChain(chain):
    #Primera Version

    # reverse = ""
    # for value in chain:
    #     reverse = value + reverse
    # return reverse

    #Segunda Version
    return chain[::-1]

#7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def isPalindrome(chain):
    #Primera Version

    # chain = chain.lower()
    # reverse = reverseChain(chain)
    # if chain == reverse:
    #     return True
    # return False

    #Segunda Version
    chain = chain.lower()
    return chain == reverseChain(chain)

#8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(list1: list, list2: list):
    flag = False
    for value in list1:
        if value in list2:
            flag = True
    return flag

#9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generateCharacteres(repetitions: int, value: str):
    return value*repetitions

#10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

def histogram(list: list):
    for value in list:
        print(f'\n{generateCharacteres(value, "*")}')

#Ejercicios Segunda Parte

#Ejercicio 1: La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def maxList(list: list, size=None, top=0):
    if size is None:
        size = len(list)
    if size > 0:
        top = max(top, list[size-1])
        top = maxList(list, size-1, top)
    return top

#Ejercicio 2: Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def chainLarge(list: list):
    equals = []
    topChain = ""
    sizeNow = len(topChain)
    for value in list:
        sizeNew = len(value)
        if sizeNow <= sizeNew:
            if sizeNow>0:
                equals.append(value)
                if sizeNow < sizeNew:
                    equals.remove(topChain)
            topChain = value
            sizeNow = sizeNew
    return equals

#Ejercicio 3: Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def chainLargeN(list: list, number: int):
    compare = []
    for value in list:
        size = len(value)
        if number < size:
            compare.append(value)
    return compare

#Ejercicio 4: Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
import re
def evaluateNCapital(chain: str):
    number = 0
    for value in chain:
        number += len(re.findall("[A-Z]+", value))
    return number

#Ejercicio 5: Construir un pequeño programa que convierta números binarios en enteros.

def binaryEntire(binary: int):
    decimal = 0
    for position, digit in enumerate(binary[::-1]):
        decimal += 2**position*int(digit)
    return decimal

#Ejercicio 6
# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

def calculateBirthday(year: int, persons: list):
    for value in persons:
        comply = year - value[1]
        print(f'The person {value[0]} will be {comply} years old')

def insertDate():
    persons = []
    year = int(input('Insert the current year: '))
    for i in range(3):
        name = input('Insert the name: ')
        yearBirthday = int(input('Insert the birth year: '))
        persons.append([name, yearBirthday])

    calculateBirthday(year, persons)

#Ejercicio 7: Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def impressAgeTop(ages):
    return len(filter(lambda x: x>20, ages))

def insertAges():
    ages = []
    for i in range(10):
        age = int(input('Insert a age: '))
        ages.append(age)
    print(f'The number of people over 20 years of age are: {impressAgeTop(tuple(ages))}')

#Ejercicio 8: Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def searchWord(characterSearch: str):
    quantity = 0
    words = ['hola', 'aja', 'como', 'estas', 'aqui', 'sutil']
    for char in words:
        if characterSearch in char[0]:
            quantity +=1
    return quantity

def insertCharacter():
    character = input('Insert a character: ')
    print(f'The number of words whats begin with the letter {character} is: {searchWord(character)}')

#Ejercicio 9: Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def quantityVowels(chain):
    quantityA = 0
    quantityE = 0
    quantityI = 0
    quantityO = 0
    quantityU = 0
    for char in chain:
        if 'a' in char or 'A' in char:
            quantityA +=1
        if 'e' in char or 'E' in char:
            quantityE +=1
        if 'i' in char or 'I' in char:
            quantityI +=1
        if 'o' in char or 'O' in char:
            quantityO +=1
        if 'u' in char or 'U' in char:
            quantityU +=1

    print(f'A tiene {quantityA}\nE tiene {quantityE}\nI tiene {quantityI}\nO tiene {quantityO}\nU tiene {quantityU}\n')

#Ejercicio 10: Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def esBisiesto(year: int):
    if year%4 == 0 or year%400 ==0:
        if year%100 !=0:
            return True
    return False

#Ejercicios Tercera Parte

#Ejercicio 1: Diseñar un sistema de puntos para el juego El reino del dragón:Dejo el enlace por si alguien no lo vio.
#La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos. 
#Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo y la opción de empezar de nuevo.

#from reinoDragon import *

#Ejercicio 2: Escribe un programa que te permita jugar a una versión simplificada del juego Master Mind. El juego consistirá en adivinar una cadena de números distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la cadena de números. En cada intento, el programa informará de cuántos números han sido acertados (el programa considerará que se ha acertado un número si coincide el valor y la posición).

import random

def numberRandom(longitude: int):
    word = ""
    for value in range(longitude):
        word += str(random.randint(int(value), longitude))
    return word

def evaluateNumber(numRandom, numUser):
    size = len(numRandom)
    counter = 0

    for i in range(size):
        if numRandom[i] == numUser[i]:
            counter += 1
    return counter

def masterMind():
    number = ""
    while len(number) == 0:
        number = input('Digite la longitud de la cadena: ')
    numRandom = numberRandom(int(number))
    chainUser = ""
    while len(chainUser)==0:
        chainUser = input("Intenta adivinar la cadena: ")

    while len(chainUser)>0:
        flag = evaluateNumber(numRandom, chainUser)
        if flag == int(number):
            print(f'con {chainUser} has adivinado {flag} valores\nFelicidades')
            chainUser = ""
        else:
            chainUser = input(f'con {chainUser} has adivinado {flag} valores, intenta adivinar la cadena: ')

#Ejercicio 3: Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

def evaluateRhyme():
    chainFirst = input("Digite la primera palabra: ")
    chainSecond = input("Digite la segunda palabra: ")
    if len(chainFirst) < 3 or len(chainSecond) < 3:
        print("Una de las dos palabras tienen menos de 3 letras")
    elif chainFirst[-3:] == chainSecond[-3:]:
        print("Las dos palabras riman")
    elif chainFirst[-2:] == chainSecond[-2:]:
        print("Las dos palabras riman un poco")
    else:
        print("Las dos palabras no riman")

#Ejercicio 4: Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida. Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.

def rateInterest(capital, interest, years):
    return capital * ((1 + interest/100)**years)

def mainInterest():
    capital = int(input("Cuanto dinero (Dolares): "))
    interest = float(input("Cuanto interés: "))
    years = int(input("Cantidad de años: "))

    print(f"Sabiendo que una cantidad de {capital} dolares al {interest}% de interes anual se convierte en {rateInterest(capital, interest, years)} dolares al cabo de {years} años")

mainInterest()
