import os
import xmltodict
import json
import codecs


# Function to add the root tag to all files in a directory
def root_tag(my_filepath):
    directory = my_filepath

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with codecs.open(filepath, "r+", encoding='ISO-8859-1') as file:
                old = file.read()
                file.seek(0)
                file.write("<Collection>\n" + old)
                file.close()

            with codecs.open(filepath, "a", encoding='ISO-8859-1') as file:
                file.write("</Collection>\n")
                file.close()


# Function to create json file from all file of a directory
def converter(my_filepath):
    directory = my_filepath

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with codecs.open(filepath, 'r', encoding='ISO-8859-1') as file:
                obj = xmltodict.parse(file.read())
                file.close()
                json_object = json.dumps(obj, indent=2)

            with codecs.open(filepath.replace(".xml", ".json"), "w", encoding='ISO-8859-1') as json_file:
                json_file.write(json_object)
                json_file.close()

root_tag("docs")
