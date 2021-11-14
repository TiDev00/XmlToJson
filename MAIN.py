import os
import xmltodict
import json


# Function to add the root tag to all files in a directory
def root_tag(my_file_path):
    directory = my_file_path

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with open(filepath, "r+") as file:
                old = file.read()
                file.seek(0)
                file.write("<Collection>\n" + old)
                file.close()

            with open(filepath, "a") as file:
                file.write("</Collection>\n")
                file.close()


# Function to create json file from xml file
def converter(my_file):
    with open(my_file, 'r') as file:
        obj = xmltodict.parse(file.read())
        file.close()
        json_object = json.dumps(obj, indent=2)

    with open(my_file.replace(".xml", ".json"), "w") as json_file:
        json_file.write(json_object)
        json_file.close()


converter("test0.xml")
