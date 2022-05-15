creator = "Karen"
PI = 3.1415926
_year = 2022


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def area(radius):
    return PI * radius * radius

# this code will only run if this file is being run directly
# if it is being executed from the top as the main program.
# if this file is being used anywhere as an import a module, it will not run
if __name__ == "__main__":
    print("Thios will only run when calculator is being executed as a script")
    print(subtract(3, 5))
