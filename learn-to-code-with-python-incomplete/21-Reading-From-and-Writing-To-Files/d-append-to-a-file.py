file_name = "my_file.txt"

with open(file_name, "a") as file_obj:
    file_obj.write("appending the file!!!!\n")
    file_obj.write("Next line!!!!\n")