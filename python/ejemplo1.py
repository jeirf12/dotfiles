

numberList = [1,2,3,4,5,6,7,8,9]
print(numberList)
for index,iterator in enumerate(numberList):
    numberList[index] *=10
print(numberList)

number1 = 20
number2 = 30
print(f"""Elige tu propio camino
    no se puede vivir solo todo el dia
    ok vivo inutil
    El resultado es {number1*number2} """)
#las tuplas no se pueden agregar datos en caliente o cuando esta corriendo el programa
#actua como una lista constante

t = (12, 'hello', 'python', [10, 5, 7], 'h')
#t.append(3) #no funciona porque las tuplas son inmutables
# pero se puede utilizar otros metodos como las listas
print(len(t))
print(len(t[4]))

#los conjuntos ordenan sin importar como los ingrese
body = {2, 1, 3}
print(body)

#para buscar en un conjunto un dato o info
collection = {'there are', 'many', 'values'}
print('values' in collection)

#simplificar repetidos de listas con conjuntos
listen = [7, 7, 7, 5, 5, 5, 6, 6, 6]
print(listen)
body = set(listen)
print(body)

#imprimiendo caracteres de una cadena
character = 'this is an example to demonstrate the effectiveness of python'
print(set(character))

#manejo de colas en python
from collections import deque

colas = deque()
print(colas)

print(type(colas))

colas = deque(['example', 'jhon', 'student', 'genius', 'example1'])
print(colas)
#para sacar los datos como pilas
colas.pop()
print(colas)

#para sacar los datos como colas
colas.popleft()
print(colas)

#para imprimir en pantalla
v1 = 'jhon'
v2 = 'student genius'
forma = 'El profesor {} y sus {}'.format(v1, v2)
print(forma)

#Otra utilidad de format para el lado izquierdo
print('{:50}'.format('hola bb'))

#Otra utilidad de format para el lado derecho
print('{:>50}'.format('hola bb'))
