
from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/home/naren/Descargas/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)
            
