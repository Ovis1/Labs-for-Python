# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = int(1.44 * 1024 * 1024) # размер дискеты в байтах
book_pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

book_size = book_pages * lines_per_page * chars_per_line * bytes_per_char  # размер одной книги в байтах
num_books = disk_size // book_size  # количество книг

print("Количество книг, помещающихся на дискету:", num_books)
