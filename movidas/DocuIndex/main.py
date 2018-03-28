#!/usr/bin/python
import os
from Doc import Doc

pathDoc = r"C:\Users\miguel\Documents\Trabajo\GMV\Proyectos\GSCINF\Doc"
indexer = {'Contract': [],
           'ENG': [],
           'Interfaces': [],
           'Others': [],
           'Plan': [],
           'RAMS': [],
           'Requirement': [],
           'SOC': []}

def addToIndexer(object):
    indexer[object.type].append(object)

def generateHtml():
    htmlFile = open("index.html", "w")
    htmlFile.writelines("<!DOCTYPE html>")
    htmlFile.writelines("<html>")
    htmlFile.writelines("<body>")

    for type, listDoc in indexer.items():
        for doc in listDoc:
            str = "<br><a href=\"{0}/{1}\">{1}</a>\n".format(type, doc.name)
            htmlFile.write(str)
    htmlFile.writelines("</html>")
    htmlFile.writelines("</body>")
    htmlFile.close()


def main():
    for root, dir, files in os.walk(pathDoc):
        for file in files:
            filename = os.path.join(root, file)
            doc = Doc(filename)
            addToIndexer(doc)

    generateHtml()


if __name__ == "__main__":
    main()

