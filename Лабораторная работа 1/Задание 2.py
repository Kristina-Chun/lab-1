# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 #Мб
pages = 100
lines = 50
symbols_per_line = 25
symbol_weight = 4 #байт
book_size = pages * lines * symbols_per_line * symbol_weight #байт
mb_book_size = book_size / 1024**2 #Мб
number_of_books = disk_size//mb_book_size
print("Количество книг, помещающихся на дискету:", round(number_of_books))
