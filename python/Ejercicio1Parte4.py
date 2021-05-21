#Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
import random

def calculateAmount(amount):
    number = random.choice([0, 10, 20, 25, 50])
    balls = {0:"Bola Blanca", 10:"Bola Roja", 20:"Bola Azul", 25:"Bola Verde", 50:"Bola Amarilla"}
    print(f"Aleatoriamente usted obtuvo una {balls[number]}")
    if number == 0:
        print("\n\nlo siento no ha ganado un descuento")
    else:
        amount = amount - ((amount*number)/100)
        print(f"\n\nFelicidades, ha ganado un {number} por ciento de descuento")
    print(f"\n\nSu nuevo total a pagar es: ${amount}")

def main():
    flag = True
    while flag:
        try:
            amount = int(input('\nIntroduzca la cantidad total de la compra: '))
            if amount >=100:
                print("""\nSu gasto iguala o supera los $100.00 y por tanto participa en la promoción.\n
\t  Color           \t  Descuento\n
\tBola Blanca       \t   No tiene\n
\tBola Roja         \t10 por ciento\n
\tBola Azul         \t20 por ciento\n
\tBola Verde        \t25 por ciento\n
\tBola Amarilla     \t50 por ciento\n
""")
                calculateAmount(amount)
            else:
                print("\nNo aplica a la promoción")
            flagNumber = int(input('\nSi desea salir presione 1 o de lo contrario presione otro número: '))
            if flagNumber == 1:
                print("\nGracias por utilizar el programa!")
                flag = False
        except Exception:
            pass
main()
