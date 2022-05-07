# item() invoked on a dict object and returns and iterable view object
# which is a special object that yields one key-value pair at a time
# for each iteration, it's actually going to provide us a 2 element tuple (key, value)
# the tuple can be unpacked and stored in 2 vairables right in the declaration of the formal

courses = {
    "History": "Mr.Washington",
    "Math": "Mr.Newton",
    "Science": "Mr.Einstein"
}

for course, professor in courses.items():
    print(f"The cours {course} is being taught by {professor}.")

# _ is a comminoty convention to indicate that
# whatever this _ variable presents is not going to be used in the block
for _, professor in courses.items():
    print(f"The next professor is {professor}")



