import os
import re
import xmltodict
import json
import codecs



# Function to add the root tag to all files in a directory
def root_tag(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with codecs.open(filepath, "r+", encoding='ISO-8859-1') as file:
                old = file.read()
                file.seek(0)
                file.write("<add>\n" + old)
                file.close()
            with codecs.open(filepath, "r+", encoding="ISO-8859-1") as file:
                old2 = file.read()
                file.seek(0)
                file.write("<?xml version = \"1.0\" encoding = \"ISO-8859-1\"?>\n" + old2)
                file.close()
            with codecs.open(filepath, "a") as file:
                file.write("\n</add>")
                file.close()


# Function to create json file for all file of a directory
def converter(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with codecs.open(filepath, 'r+', encoding='ISO-8859-1') as file:
                obj = xmltodict.parse(file.read())
                file.close()
                json_object = json.dumps(obj, indent=4)
            with codecs.open(filepath.replace(".xml", ".json"), "w+") as json_file:
                json_file.write(json_object)
                json_file.close()


# Function to replace tag properly for all files in a directory
def replacer(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with codecs.open(filepath, 'r+') as file:
                f = file.read()
                f = re.sub('<DOC>', '<doc>', f)
                f = re.sub('</DOC>', '</doc>', f)
                f = re.sub('<DOCNO>', '<field name=\"docno\">', f)
                f = re.sub('</DOCNO>', '</field>', f)
                f = re.sub('<FILEID>', '<field name=\"fileId\">', f)
                f = re.sub('</FILEID>', '</field>', f)
                f = re.sub('<FIRST>', '<field name=\"first\">', f)
                f = re.sub('</FIRST>', '</field>', f)
                f = re.sub('<SECOND>', '<field name=\"second\">', f)
                f = re.sub('</SECOND>', '</field>', f)
                f = re.sub('<HEAD>', '<field name=\"head\">', f)
                f = re.sub('</HEAD>', '</field>', f)
                f = re.sub('<DATELINE>', '<field name=\"dateline\">', f)
                f = re.sub('</DATELINE>', '</field>', f)
                f = re.sub('<TEXT>', '<field name=\"text\">', f)
                f = re.sub('</TEXT>', '</field>', f)
                f = re.sub('<BYLINE>', '<field name=\"byline\">', f)
                f = re.sub('</BYLINE>', '</field>', f)
                f = re.sub('<NOTE>', '<field name=\"note\">', f)
                f = re.sub('</NOTE>', '</field>', f)
                f = re.sub('<UNK>', '<field name=\"unk\">', f)
                f = re.sub('</UNK>', '</field>', f)
                f = re.sub('&', '&amp;', f)
                file.seek(0)
                file.write(f)
                file.truncate()