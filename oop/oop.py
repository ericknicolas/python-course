from book import Book

b = Book("Game of Thrones", "Martin", 350, "tapa dura")
a = Book("Harry Potter", "JK Rowling", 700, "tapa blanda")

print(b.get_title())
print(a.num_pages())
print(a)
print(len(b))
print(b.num_pages())