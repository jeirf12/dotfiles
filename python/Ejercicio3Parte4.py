#Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película y posterior a ello pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.

import os, time

def main():
    flag = True
    while flag:
        try:
            print("""\n\tCategoria\t\tPrecio\t\tCódigo\tRecargo/Día de atraso\n
\tFavoritos\t\t$2.50\t\t  1\t\t$0.50
\tNuevos\t\t\t$3.00\t\t  2\t\t$0.75
\tEstrenos\t\t$3.50\t\t  3\t\t$1.00
\tSuper Estrenos\t\t$4.00\t\t  4\t\t$1.50
""")
            code = 0
            while code < 1 or code > 4:
                code = int(input('Introduzca el código de la categoria de la pelicula: '))
            numberDelay = int(input('Introduzca el número de días de atraso en la devolución: '))
            priceMovies = {1: 2.50, 2: 3.00, 3: 3.50, 4: 4.00}
            priceDelays = {1: 0.50, 2: 0.75, 3: 1.00, 4: 1.50}
            price = priceMovies[code] + (numberDelay * priceDelays[code])
            print(f'\nEl total a pagar es: {price} dolares')
            flagNumber = int(input('Si desea salir presione 1 o de lo contrario presione otro número: '))
            if flagNumber == 1:
                print('Gracias por utilizar el programa!')
                flag = False
        except Exception:
            time.sleep(2)
            os.system('clear')

main()
