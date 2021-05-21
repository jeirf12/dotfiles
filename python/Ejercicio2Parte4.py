# De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. El programa determinará el total a pagar, como una factura. Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades, y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??
class Product():
    def __init__(self, name, code, price, amount=0):
        self.__name = name
        self.__code = code
        self.__price = price
        self.__amount = amount

    def setName(self, name): self.__name = name
    def setCode(self, code): self.__code = code
    def setPrice(self, price): self.__price = price
    def setAmount(self, amount): self.__amount = amount
    def getName(self): return self.__name
    def getCode(self): return self.__code
    def getPrice(self): return self.__price
    def getAmount(self): return self.__amount

def getProduct(code):
    listProducts = {1:Product('Camisa', 1, 35.0), 2:Product('Cinturon', 2, 7.0), 3:Product('Zapatos', 3, 75.0), 4:Product('Pantalón', 4, 80.0), 5:Product('Calcetines', 5, 6.0), 6:Product('Faldas', 6, 25.0), 7:Product('Gorras', 7, 10.0), 8:Product('Sueter', 8, 45.0), 9:Product('Corbata', 9, 15.0), 10:Product('Chaqueta', 10, 55.0)}
    return listProducts[code]

def searchRepeated(products, product):
    for value in products:
        if product.getName() == value.getName():
            value.setAmount(value.getAmount() + product.getAmount())
            value.setPrice(value.getPrice() + product.getPrice())
            return True
    return False


def getInvoice(products):
    priceOverall = 0
    print("""\n\t\t\t\t\tFactura\n\n
    \t\tProducto\t\t Unidades\t\tValor""")
    for product in products:
        print(f"""\n\t\t{product.getName()}\t\t\t{product.getAmount()}\t\t\t{product.getPrice()}""")
        priceOverall += product.getPrice()

    print(f"\n\t\tEl total neto a pagar es: {priceOverall}")

def main():
    products = []
    flag = True
    while flag:
        try:
            print("""\n\t\tElija el producto deseado: \n\n
\t\tProducto                \tCódigo\n
\t\tCamisa........................... 1\n
\t\tCinturon......................... 2\n
\t\tZapatos.......................... 3\n
\t\tPantalón......................... 4\n
\t\tCalcetines....................... 5\n
\t\tFaldas........................... 6\n
\t\tGorras........................... 7\n
\t\tSueter........................... 8\n
\t\tCorbata.......................... 9\n
\t\tChaqueta......................... 10\n
""")
            code = 0
            while code < 1 or code > 10:
                code = int(input('\t\tIntroduzca código: '))
            product = getProduct(code)
            print(f'\n\t\tEl precios es: ${product.getPrice()}')
            units = int(input('\n\t\tIntroduzca número de unidades: '))
            price = product.getPrice() * units
            product.setPrice(price)
            product.setAmount(units)
            if searchRepeated(products, product) == False:
                products.append(product)
            print(f'\n\t\tEl total a pagar es: ${price}')
            flagNumber = int(input('Si desea salir presione 1 o de lo contrario presione otro número: '))
            if flagNumber == 1:
                getInvoice(products)
                flag = False
        except Exception:
            pass

main()
