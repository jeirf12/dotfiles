# Ejercicio Python:
# Una
# PyME, tiene la siguiente estructura de pagos para sus 10 empleados: 

# Un sueldo
# base

# Una bonificación del 1% del sueldo base, por
# cada mes trabajado

# Una asignación familiar del 5% del sueldo base,
# por cada hijo


# La suma de los tres valores anteriores, conforman
# la “base imponible”.
# Todos los empleados están en FONASA, así que
# deben cotizar el 7% de la base imponible en salud. Los empleados están en una de dos: AFPs, la
# primera cobra (entre imposición y otros gastos) el 12 % de la base imponible, mientras que la
# segunda cobra el 11.4%

# Construyan un programa Python que:

# a) Pida el ingreso de datos de los 10 empleados
# y los almacene. Debe pedir: nombre, apellido, sueldo base, afap, fecha de ingreso
# y cantidad de hijos.

# b) El programa debe calcular la base imponible,
# según lo indicado arriba y luego descontar según corresponda.

# c) El programa debe calcular lo que se debe
# pagar a FONASA y el monto de cada AFAP.

# d) El programa debe calcular los promedios de
# pago a los empleados

# e) El programa debe implementar control de
# excepciones en cada ingreso de información.

# El mensaje debe ser claro al usuario, indicando
# que debe corregir en cada intento de ingresar los datos.E
# Se entiende por:

# FONASA: El Fondo Nacional de Salud, FONASA, es el organismo público encargado de otorgar cobertura de atención, tanto a las personas que cotizan el 7% de sus ingresos mensuales en FONASA, como a aquellas que, por carecer de recursos propios, financia el Estado a través de un aporte fiscal directo.

# AFAP: AFAP significa “Administradora de Fondos de Ahorro Previsional”. Son empresas que administran parte del aporte de los trabajadores afiliados para que en el futuro tengan una mejor jubilación.

import sqlite3

connection = sqlite3.connect('prueba')
cursor = connection.cursor()
print("La base de datos se abrió correctamente")

def executeQuery(query):
    try:
        cursor.execute(query)
        connection.commit()
        query = query.split(" ")
        nameTable = query[2].strip().lower()
        action = query[0].strip().lower()
        if action == "create":
            action = "creada"
        elif action == "insert":
            action = "se ingreso el registro"
        elif action == "update":
            action = "actualizada"
        elif action == "delete":
            action = "borró los registros"
        elif action == "drop":
            action = "eliminada"
        elif action == "select":
            nameTable = query[3].strip().lower()
            action = "seleccionada"
        else:
            action = ""
        print(f"Tabla {nameTable} {action} correctamente")
        return cursor
    except Exception as ex:
        print(f"Ocurrió un error: {ex}")

def deleteTable(nameTable):
    query = f"DROP TABLE {nameTable.upper()}"
    executeQuery(query)

def deleteDataTable(nameTable):
    query = f"DELETE FROM {nameTable.upper()}"
    executeQuery(query)

def createTableEmployee():
    query = '''CREATE TABLE EMPLOYEE
          (ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
          NAME            TEXT    NOT NULL,
          LASTNAME        TEXT    NOT NULL,
          SALARY          REAL    NOT NULL,
          AFAP            INT     NOT NULL,
          STARTDATE       DATE    NOT NULL,
          COUNTERCHILDRENS INT    NOT NULL
          )'''
    executeQuery(query)

def showTable():
    aux = executeQuery("SELECT * FROM EMPLOYEE")
    rows = aux.fetchall()
    for row in rows:
        print(row)

def validateInputData(chain, option="string"):
    value = ""
    while len(str(value)) == 0:
        value = input(chain)
        if option == "numeric":
            if value.isnumeric():
                value = int(value)
            else:
                value = ""
        elif option == "string":
            if not value.isalpha():
                value = ""
    return value

def insertEmployee():
    name = validateInputData("Digite el nombre: ")
    lastName = validateInputData("Digite el apellido: ")
    salary = validateInputData("Digite el salario: ", "numeric")
    afap = validateInputData("Digite el afap: ", "numeric")
    print("Digite la fecha de ingreso a la empresa")
    day = validateInputData("Digite el dia: ", "numeric")
    month = validateInputData("Digite el mes: ", "numeric")
    year = validateInputData("Digite el año: ", "numeric")
    dateStart = f"{day}/{month}/{year}"
    countChildrens = validateInputData("Digite la cantidad de hijos: ", "numeric")
    executeQuery(f'''INSERT INTO EMPLOYEE (NAME, LASTNAME, SALARY, AFAP, STARTDATE, COUNTERCHILDRENS) VALUES ("{name}", "{lastName}", {salary}, {afap}, "{dateStart}", {countChildrens})''')

def main():
    insertEmployee()
    showTable()

main()
# deleteTable('employee')
# createTableEmployee()
