import os

class Doc:

    def __init__(self, filename):
        self.name = os.path.basename(filename)
        self.filepath = filename
        self.alias = ""
        self.id = 0
        self.size = 0
        self.format = ""
        self.date = ""
        self.version = ""
        self.type = os.path.basename(os.path.dirname(filename))

    def toPrint(self):
        print("name: \t" + self.name)
        print("filepath: \t" + self.filepath)
        print("alias: \t" + self.alias)
        print("id: \t" + str(self.name))
        print("size: \t" + str(self.size))
        print("format: \t" + self.format)
        print("date: \t" + self.date)
        print("version: \t" + self.version)
        print("type: \t" + self.type)



