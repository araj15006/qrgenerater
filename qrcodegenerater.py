import pyqrcode
from PIL import Image
import sys

def qrgenerater(name,link):
    
    pLink = pyqrcode.create(link)
    pLink.png(f"{name}.png", scale=50)
    print("Code generated and saved.")
    print("Opening your code...")

    # opening file
    image = Image.open(f"{name}.png")
    image.show()
    print("file opend")
    sys.exit()


name = str(input("Enter file name: "))
link = input("Enter your link here: ")  
qrgenerater(name,link)