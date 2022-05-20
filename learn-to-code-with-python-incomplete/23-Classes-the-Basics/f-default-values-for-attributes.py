from asyncio import gather


class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "Georage Orwell")
gatsby = Book("The Great Gatsby","F.Scott Fitzgerald", 29.10)

print(animal_farm.price)
print(gatsby.price)

atlas = Book(title = "Atlas Shrugged", author = "Ayn Rand")


