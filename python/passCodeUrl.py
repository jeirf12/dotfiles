#! python
import qrcode, sys, cv2, pyshorteners,numpy as np

params = sys.argv
nameFile = "codigoQR"

if len(params) > 1:
    data = params[1]

    if '-s' in params:
        shortener = pyshorteners.Shortener()
        short_url = shortener.dagd.short(data)
        data = short_url

    img = qrcode.make(data)

    if '-g' in params:
        print(f"foto guardada como: {nameFile}.png")
        img.save(f'{nameFile}.png')
    else:
        imgprocess = np.array(img.convert('RGB'), dtype = np.uint8)
        cv2.imshow(nameFile, imgprocess)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("ERROR: Se introdujo (0) o mas de un (1) argumento\nEjemplo de uso: \n\t\tpython passCodeUrl.py www.google.com\n\t\t python passCodeUrl.py www.google.com -g\n\t\tpython passCodeUrl.py www.google.com -g -s")
