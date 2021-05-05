#1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(number1, number2):
    top = number2
    if number1>number2:
        top = number1
    return top

#2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def maxThree(number1, number2, number3):
    if number1>number2 and number1>number3:
        top = number1
    elif number2>number1 and number2>number3:
        top = number2
    elif number3>number1 and number3>number2:
        top = number3
    elif number1==number2 or number1==number3:
        top = number1

    return top

#3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def len(list:list):
    acum = 0
    for i in list:
        acum += 1
    return acum

#4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
import re

def valueCharacter(chain):
    value = re.search('[^aeiouAEIOU]', chain)
    if value:
        return False
    return True

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
    reverse = ""
    for value in chain:
        reverse = value + reverse
    return reverse

#7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def isPalindrome(chain):
    chain = chain.lower()
    reverse = reverseChain(chain)
    if chain == reverse:
        return True
    return False

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

