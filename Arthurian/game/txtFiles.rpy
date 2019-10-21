init python:
    def getPage(filename):
        yourData = filename
        yourData = renpy.file(yourData).read().decode("utf-8")
        yourData = yourData.replace("\r", "")
        yourData = yourData.replace("\t", "        ")
        return yourData