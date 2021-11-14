import os


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

root_tag("DossierTest")