#!/usr/bin/python
import os
import PIL.Image

"""
printStats():   funcion que imprime todos los datos que se han ido almancenando, i.e.
                numero de carpetas, ficheros, tamaño, etc.

braimstorming:
- colecionar metadatos

"""
inFolder="/home/miguel/Imágenes"
image = "/home/miguel/Imágenes/IMG_20160807_060703.jpg"

TAG_DATE=36868

def playWithPIL():
    img = PIL.Image.open(image)
    exif_data = img._getexif()
    print(exif_data)

def formatDate(date):
    """
    Resultado: 2016:08:07 06:07:03 --> 20160807060703
    Quitar los dos puntos
    Quitar espacio
    """
    return date


def main():
    separator = "------------------------------------------"
    folderId = 0
    print(separator)
    for root,dir,files in os.walk(inFolder):
        folderId += 1
        print("folder: " + root)
        print("folderId: %d" % folderId)
        print("dir: " + str(dir))
        print("files: " + str(files))
        print()
        for filename in files:
            print(filename)
            if filename.endswith(".jpg"):
                # Rename jpg files
                file = os.path.join(root, filename)
                img = PIL.Image.open(file)
                exif_data = img._getexif()
                if exif_data and TAG_DATE in exif_data:
                    date = formatDate(exif_data[TAG_DATE])
                    print("\t-- " + date)
                else:
                    pass
            elif filename.endswith(".png"):
                # Rename png files
                """
                Por aquí se define cómo extraer metadatos con ficheros png:
                https://motherboard.vice.com/en_us/article/aekn58/hack-this-extra-image-metadata-using-python
                """
                pass
            else:
                # Rename other format files
                pass

        print(separator)


if __name__ == "__main__":
    main()
    #playWithPIL()
