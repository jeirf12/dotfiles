#! python
import re

def asciiBinary(chain):
    binary = ""
    for date in chain:
        value = wheelToBinary(date)
        binary +=value
    return binary

def wheelToBinary(character):
    dictionaryAscii = {' ': ' 00100000', '!': ' 00100001', '"': ' 00100010', '#':' 00100011', '$':' 00100100', '%':' 00100101', '&':' 00100110', '\'':' 00100111', '(':' 00101000', ')':' 00101001', '*':' 00101010', '+':' 00101011', ',':' 00101100', '-':' 00101101', '.':' 00101110', '/':' 00101111', '0':' 00110000', '1':' 00110001', '2':' 00110010', '3':' 00110011', '4':' 00110100', '5':' 00110101', '6':' 00110110', '7':' 00110111', '8':' 00111000', '9':' 00111001', ':':' 00111010', ';':' 00111011', '<':' 00111100', '=':' 00111101', '>':' 00111110', '?':' 00111111', '@':' 01000000', 'A':' 01000001', 'B':' 01000010', 'C':' 01000011', 'D':' 01000100', 'E':' 01000101', 'F':' 01000110', 'G':' 01000111', 'H':' 01001000', 'I':' 01001001', 'J':' 01001010', 'K':' 01001011', 'L':' 01001100', 'M':' 01001101', 'N':' 01001110', 'O':' 01001111', 'P':' 01010000', 'Q':' 01010001', 'R':' 01010010', 'S':' 01010011', 'T':' 01010100', 'U':' 01010101', 'V':' 01010110', 'W':' 01010111', 'X':' 01011000', 'Y':' 01011001', 'Z':' 01011010', '[':' 01011011', '\\':' 01011100', ']':' 01011101', '^':'	01011110', '_':' 01011111', '`':' 01100000', 'a':' 01100001', 'b':' 01100010', 'c':' 01100011', 'd':' 01100100', 'e':' 01100101', 'f':' 01100110', 'g':' 01100111', 'h':' 01101000', 'i':' 01101001', 'j':' 01101010', 'k':' 01101011', 'l':' 01101100', 'm':' 01101101', 'n':' 01101110', 'o':' 01101111', 'p':' 01110000', 'q':' 01110001', 'r':' 01110010', 's':' 01110011', 't':' 01110100', 'u':' 01110101', 'v':' 01110110','w':' 01110111', 'x':' 01111000', 'y':' 01111001', 'z':' 01111010', '{':' 01111011', '|':' 01111100', '}':' 01111101', '~':' 01111110'}
    if character in dictionaryAscii:
        return dictionaryAscii[character]
    return character

def binDecimal(numberBinary):
    numberDecimal = 0
    for position, digitBinary in enumerate(numberBinary[::-1]):
        numberDecimal += 2**position*int(digitBinary)
    return numberDecimal

def decimalBin(numberDecimal):
    binary = ""
    decimal = int(numberDecimal)
    while decimal // 2 !=0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return str(decimal) + binary

def decHexa(numberDecimal):
    hexadecimal = ""
    decimal = int(numberDecimal)
    while decimal >= 16:
        quotient = decimal % 16
        quotient = wheelToHexa(quotient)
        hexadecimal = quotient + hexadecimal
        decimal = int(decimal // 16)
    return str(decimal) + hexadecimal

def hexaDec(numberHexadecimal):
    decimal = 0
    for position,date in enumerate(numberHexadecimal[::-1]):
        value = wheelToDecimal(date)
        high = 16 ** position
        equivalence = high * value
        decimal += equivalence
    return decimal


def wheelToHexa(number:int):
    dictionaryHexadecimal = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    number = str(number)
    if number in dictionaryHexadecimal:
        return dictionaryHexadecimal[number]
    return number

def wheelToDecimal2(character:str):
    dictionaryDecimal = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    if character in dictionaryDecimal:
        return dictionaryDecimal[character]
    return int(character)



def validateNumberInput(numberFlag = 1):
    num = -1
    flag = False
    if numberFlag == 1:
        name1 = 'binary'
        name2 = 'decimal'
    elif numberFlag == 2:
        name1 = 'decimal'
        name2 = 'binary'

    while not flag:
        number = input(f"Enter the {name1} number:\n")
        if len(number)==1:
            if number.find('1')!=-1 or number.find('0')!=-1:
                num=number
                break
        if numberFlag == 1:
            flag = re.match('[01][10]', number)
        else:
            break

    if numberFlag == 1 and num ==-1:
        num = binDecimal(number)
    elif numberFlag == 2 and num ==-1:
        num = decimalBin(number)

    print(f'the number {name2} is {num}')

def test(numberFlag = 1):
    validateNumberInput(numberFlag)

#test(2)
#print(decHexa('7000'))
#print(hexaDec('1B58'))
#print(asciiBinary('RFJ'))
print(decimalBin('35'))
