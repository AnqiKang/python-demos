# if the file already exists, it will be deleted. all contents will be deleted
# eveytime, create a new file
file_name = "my_file.txt"

with open(file_name, "w") as file_obj:
    file_obj.write("Hello file!!!!\n")
    file_obj.write("This is the second line!!!!\n")
