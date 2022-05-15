# using * to import all of the module's public attributes into the current namespace
from a_calculator import *

print(creator)
print(PI)
print(add(3, 5))
print(subtract(3, 10))

# cannot invoke any attributes with _XX from that module