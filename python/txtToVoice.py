from gtts import gTTS
from deep_translator import GoogleTranslator
import os

#texto que se ingresa por consola
text = input("Insert text for convert to audio: ")
language = input("Insert the language of translator: ")

#Traducir documentos
#language = 'es'
#pathTexto = os.getcwd()
#textTranslator = GoogleTranslator(source='en', target=language).translate_file(f'{pathTexto}/textIngles.txt')

#Traduce el texto ingresado
textTranslator = GoogleTranslator(source='auto', target=str(language)).translate(text)

#Se puede definir en text el texto que se va a leer
#lang se puede definir el lenguaje del audio lo mas usado es
#es = español y en = english
tts = gTTS(text=textTranslator, lang=language)

#Ruta donde se guarda del audio
tts.save("audioConverted.mp3")

#OPCIONAL: sirve para abrir el archivo
#si no desea abrirlo puede comentar la linea
os.system("gio open audioConverted.mp3")
