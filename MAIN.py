
myFile = "test.xml"

with open(myFile, "r+") as file:
    old = file.read()
    file.seek(0)
    file.write("<Collection>\n" + old)
    file.close()

with open(myFile, "a") as file:
    file.write("</Collection>\n")
    file.close()