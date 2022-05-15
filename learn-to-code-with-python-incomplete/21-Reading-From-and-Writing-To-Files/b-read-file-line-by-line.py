with open("cupcakes.txt") as file_obj:
    for line in file_obj:
        print(line.rstrip())