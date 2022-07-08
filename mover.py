
from PIL import Image
import os
from subprocess import  getoutput


downloadsFolder = getoutput(r"cd ~/Descargas && pwd")
picturesFolder =  getoutput(r"cd ~/Imágenes && pwd")

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name,": ",extension)

        if extension in [".mp3"]:
            
            musicFolder = getoutput(r"cd ~/Música && pwd")
            os.rename(downloadsFolder, filename, musicFolder, filename)








