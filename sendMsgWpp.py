#importamos el modulo 
import pywhatkit

try:
    
    pywhatkit.sendwhatmsg("+573145192759","fea",22,59)
    pywhatkit.help()
    print("mensaje enviado")

except:
    
    print("ocurrio un error")

