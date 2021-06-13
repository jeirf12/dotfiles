import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

def numberScanner(number):
    number = phonenumbers.parse(number)
    description = geocoder.description_for_number(number, 'en')
    supplier = carrier.name_for_number(number, 'en')
    info = [['Country', 'Supplier'], [description, supplier]]
    data = str(tabulate(info, headers="firstrow", tablefmt="github"))
    return data

num = input("Enter number: ")
print(numberScanner(num))
