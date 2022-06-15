from PIL import Image
import os

downloadsFolder = "/Users/nicolasschurmann/Downloads/"
picturesFolder = "/Users/nicolasschurmann/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/nicolasschurmann/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)



