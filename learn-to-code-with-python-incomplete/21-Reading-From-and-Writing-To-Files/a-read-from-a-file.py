# how to use Python to create an pass text files on your computer
# r: read only

# cupcakes_file = open("cupcakes.txt", "r")
# cupcakes_file.close()

# this sytax will auto close file whenever we are done working with them. no close() method needed
# perform auto cleanup when the blokc is done executing
with open("cupcakes.txt", "r") as cupcakes_files:
    print("The files has beedn opened")
    content = cupcakes_files.read()
    print(content)
    
print("The file has been closed")



