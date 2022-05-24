# invoked when an instance is no longer being referenced or used in the program
# invoked when the object is being garbage collected

class Garbage():
    def __del__(self):
        print("This is my last breath!")


g = Garbage()

g = [1, 2, 3]

import time
# sleep: pause the execution of the program
time.sleep(5)
print("Program done!")