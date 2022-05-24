# a special kind of tuple that allows the develper to access its values by both index position and by key or name
# namedtuple are used to create new classes.
# objects instantiated from namedtuples hold attributes but no instance methods
# bascially, objects with attributes but no methods
# build objects only for the purposes of storing data with no actual behavior related that data
import collections

Book = collections.namedtuple("Book", ["title", "author"])
# collections.namedtuple("Book", "title author")

# every Book object created from it will have 2 attributes, title and author
animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title= "The Great Gatsby", author = "F. Scott Fitzgerable")

print(animal_farm[0]) # Animal Farm
print(gatsby[1]) # F. Scott Fitzgerable


