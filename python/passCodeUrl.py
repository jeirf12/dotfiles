import pyshorteners
import qrcode
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    shortener = pyshorteners.Shortener()
    short_url = shortener.dagd.short(url)

    img = qrcode.make(short_url)
    img.save('urlQR.png')
    # img.show()
else:
    print("ERROR: Se introdujo (0) o mas de un (1) argumento\nEjemplo: python passCodeUrl.py www.google.com")
