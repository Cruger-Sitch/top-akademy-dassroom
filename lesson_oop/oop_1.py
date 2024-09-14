

# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска,
# производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.

# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ (со статически созданными экземплярами)

# class Car:
#     def __init__(self, name = '', year = 0, volume = '', color = '', price = ''):
#         self._name = name
#         self._year = year
#         self._volume = volume
#         self._color = color
#         self._price = price
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_year(self, year):
#         self._year = year
#         if year >= 0:
#             self._year = year
#         else:
#             print('Введено некорретное число.')
#
#     def set_volume(self, volume):
#         self._volume = volume
#
#     def set_color(self, color):
#         self._color = color
#
#     def set_price(self, price):
#         self._price = price
#
#     def get_name(self):
#         return self._name
#
#     def get_year(self):
#         return self._year
#
#     def get_volume(self):
#         return self._volume
#
#     def get_color(self):
#         return self._color
#
#     def get_price(self):
#         return self._price
#
# car1 = Car()
# car1.set_name('Hyundai')
# car1.set_year(2019)
# car1.set_volume('1.6')
# car1.set_color('Бежевый')
# car1.set_price('1 200 000')
#
# car2 = Car()
# car2.set_name('Renault')
# car2.set_year(2020)
# car2.set_volume('1.5')
# car2.set_color('Красный')
# car2.set_price('1 100 000')
#
#
# car3 = Car()
# car3.set_name('BMW')
# car3.set_year(2021)
# car3.set_volume('2.0')
# car3.set_color('Черный')
# car3.set_price('3 000 000')
#
#
# car4 = Car()
# car4.set_name('Skoda')
# car4.set_year(2018)
# car4.set_volume('1.4')
# car4.set_color('Синий')
# car4.set_price('800 000')
#
# # Проитерируем все объекты и выведем кждый экземпляр класса:
# for carr in [car1, car4, car3, car4]:
#     print('Марка модели:', carr.get_name())
#     print('год выпуска', carr.get_year())
#     print('Объем двигателя:', carr.get_volume())
#     print('Цвет автомобиля:', carr.get_color())
#     print('Цена автомобиля:', carr.get_price())
#     print('\n')
#
# # Если обращаться к отдельно взятому экземпляру, то так:
# print('Информация о car1:')
# print('Марка модели:', car1.get_name())
# print('год выпууска:', car1.get_year())
# print('Объем двигателя:', car1.get_volume())
# print('Цвет автомобиля:', car1.get_color())
# print('Цена автомобиля:', car1.get_price())
#
# # Если надо внести изменение в экземпляр класса, то так:
# car1.set_color('Серебристый')
# car1.set_price('1 250 000')
#
# # Проверяем внесенные изменения
# print("\nОбновленная информация о car1:")
# print('Марка модели:', car1.get_name())
# print('Год выпуска:', car1.get_year())
# print('Объем двигателя:', car1.get_volume())
# print('Цвет автомобиля:', car1.get_color())
# print('Цена автомобиля:', car1.get_price())
#
#

# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ (с динамически добавленными экземплярами), так, для практики...

# class Car:
#     def __init__(self, name='', year=0, volume='', color='', price=''):
#         self._name = name
#         self._year = year
#         self._volume = volume
#         self._color = color
#         self._price = price
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_year(self, year):
#         if year >= 0:
#             self._year = year
#         else:
#             print('Введено некорректное число.')
#
#     def set_volume(self, volume):
#         self._volume = volume
#
#     def set_color(self, color):
#         self._color = color
#
#     def set_price(self, price):
#         self._price = price
#
#     def get_name(self):
#         return self._name
#
#     def get_year(self):
#         return self._year
#
#     def get_volume(self):
#         return self._volume
#
#     def get_color(self):
#         return self._color
#
#     def get_price(self):
#         return self._price
#
#
# def create_car():
#     add_car = input("Хотите добавить новый автомобиль? (да/нет): ").strip().lower()
#     if add_car != 'да':
#         return None
#
#     name = input("Введите марку автомобиля: ")
#     year = int(input("Введите год выпуска: "))
#     volume = input("Введите объем двигателя: ")
#     color = input("Введите цвет автомобиля: ")
#     price = input("Введите цену автомобиля: ")
#
#     return Car(name, year, volume, color, price)
#
#
#
# cars = []
#
#
# while True:
#     car = create_car()
#     if car is None:
#         break
#     cars.append(car)
#
#
# car1 = Car()
# car1.set_name('Hyundai')
# car1.set_year(2019)
# car1.set_volume('1.6')
# car1.set_color('Бежевый')
# car1.set_price('1 200 000')
# cars.append(car1)
#
# car2 = Car()
# car2.set_name('Renault')
# car2.set_year(2020)
# car2.set_volume('1.5')
# car2.set_color('Красный')
# car2.set_price('1 100 000')
# cars.append(car2)
#
# car3 = Car()
# car3.set_name('BMW')
# car3.set_year(2021)
# car3.set_volume('2.0')
# car3.set_color('Черный')
# car3.set_price('3 000 000')
# cars.append(car3)
#
# car4 = Car()
# car4.set_name('Skoda')
# car4.set_year(2018)
# car4.set_volume('1.4')
# car4.set_color('Синий')
# car4.set_price('800 000')
# cars.append(car4)
#
#
# for i, car in enumerate(cars, start=1):
#     print(f"\nИнформация о car{i}:")
#     print('Марка модели:', car.get_name())
#     print('Год выпуска:', car.get_year())
#     print('Объем двигателя:', car.get_volume())
#     print('Цвет автомобиля:', car.get_color())
#     print('Цена автомобиля:', car.get_price())



# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.


# class Book:
#     def __init__(self, title='', year_of_publication=0, publisher='', genre='', author='', price=''):
#         self._title = title
#         self._year_of_publication = year_of_publication
#         self._publisher = publisher
#         self._genre = genre
#         self._author = author
#         self._price = price
#
#     def set_title(self, title):
#         self._title = title
#     def set_year_of_publication(self, year_of_publication):
#         if year_of_publication >= 0:
#             self._year_of_publication = year_of_publication
#         else:
#             print('Введено некорректное число.')
#
#     def set_publisher(self, publisher):
#         self._publisher = publisher
#
#     def set_genre(self, genre):
#         self._genre = genre
#
#     def set_author(self, author):
#         self._author = author
#     def set_price(self, price):
#         self._price = price
#
#     def get_title(self):
#         return self._title
#
#     def get_year_of_publication(self):
#         return self._year_of_publication
#
#     def get_publisher(self):
#         return self._publisher
#
#     def get_genre(self):
#         return self._genre
#
#     def get_author(self):
#         return self._author
#
#     def get_price(self):
#         return self._price
#
#
# def create_book():
#     add_book = input("Хотите добавить новую книгу? (да/нет): ").strip().lower()
#     if add_book != 'да':
#         return None
#
#     title = input("Введите название книги: ")
#     year_of_publication = int(input("Введите год издания: "))
#     publisher = input("Введите издателя: ")
#     genre = input("Введите жанр: ")
#     author= input("Введите автора книги: ")
#     price = input("Введите цену книги: ")
#
#     return Book(title, year_of_publication, publisher, genre, author, price)
#
# books = []
#
#
# while True:
#     book = create_book()
#     if book is None:
#         break
#     books.append(book)
#
#
# book1 = Book()
# book1.set_title('Шантарам')
# book1.set_year_of_publication(2003)
# book1.set_publisher('Азбука-2023')
# book1.set_genre('Роман')
# book1.set_author('Грегори Дэвида Роберт')
# book1.set_price('1 500 руб')
# books.append(book1)
#
# book2 = Book()
# book2.set_title('Тысяча сиюющих солн')
# book2.set_year_of_publication(2018)
# book2.set_publisher('Фантом-Пресс')
# book2.set_genre('Повесть')
# book2.set_author('Халед Хосейни')
# book2.set_price('800 руб')
# books.append(book2)
#
# book3 = Book()
# book3.set_title('Жук в муравеййнике')
# book3.set_year_of_publication(1979)
# book3.set_publisher('Знание')
# book3.set_genre('Научная фантастика')
# book3.set_author('Стругацкий А.Н, Стугацкий Б.Н.')
# book3.set_price('750 руб')
# books.append(book3)
#
# book4 = Book()
# book4.set_title('451 градус по фаренгейту')
# book4.set_year_of_publication(1953)
# book4.set_publisher('Ballantine Books')
# book4.set_genre('Научная фантастика')
# book4.set_author('Рэй Бредбери')
# book4.set_price('750 руб')
# books.append(book4)
#
#
# for i, book in enumerate(books, start=1):
#     print(f"\nИнформация о book{i}:")
#     print('Название книги:', book.get_title())
#     print('Год издания:', book.get_year_of_publication())
#     print('Издательство:', book.get_publisher())
#     print('Жанр книги:', book.get_genre())
#     print('Автор книги:', book.get_author())
#     print('Цена книги:', book.get_price())
#



# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату
# открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных, вывода
# данных, реализуйте доступ к отдельным # полям через методы класса.


# class Stadium:
#     def __init__(self, name='', opening_date=0, country='', city='', capacity=0):
#         self._name = name
#         self._opening_date = opening_date
#         self._country = country
#         self._city = city
#         self._capacity = capacity
#
#     def set_name(self, name):
#         self._name = name
#     def set_opening_date(self, opening_date):
#         if opening_date >=0:
#             self._opening_date = opening_date
#         else:
#             print('Введено некорректное число')
#     def set_country(self, country):
#         self._country = country
#     def set_city(self, city):
#         self._city = city
#     def set_capacity(self, capacity):
#         if capacity >=0:
#             self._capacity = capacity
#         else:
#             print('Введено некорректное число')
#
#     def get_name(self):
#         return  self._name
#     def get_opening_date(self):
#         return  self._opening_date
#     def get_country(self):
#         return  self._country
#     def get_city(self):
#         return  self._city
#     def get_capacity(self):
#         return  self._capacity
#
# def create_stadium():
#     add_stadium = input('Хотите дабавить стадион? (да/нет): ').strip().lower()
#     if add_stadium != 'да':
#         return None
#
#     name = input('Введите название стадиона: ')
#     opening_date = int(input('Введите год его открытия: '))
#     country = input('Введите страну: ')
#     city = input('Введите город: ')
#     capacity = int(input('Введите мвестимость стадиона'))
#
#     return  Stadium(name, opening_date, country, city, capacity)
#
# stadiums = []
#
# while True:
#     stadium = create_stadium()
#     if stadium is None:
#         break
#     stadiums.append(stadium)
#
# stadium1 = Stadium()
# stadium1.set_name('Камп Ноу')
# stadium1.set_opening_date(1957)
# stadium1.set_country("Испанния")
# stadium1.set_city('Барселона')
# stadium1.set_capacity(100000)
# stadiums.append(stadium1)
#
# stadium2 = Stadium()
# stadium2.set_name('Melbourne Cricket Ground')
# stadium2.set_opening_date(1986)
# stadium2.set_country("Австралия")
# stadium2.set_city('Мельбурн')
# stadium2.set_capacity(100024)
# stadiums.append(stadium2)
#
# stadium3 = Stadium()
# stadium3.set_name('First National Bank Stadium')
# stadium3.set_opening_date(2023)
# stadium3.set_country("ЮАР")
# stadium3.set_city('Йоханнесбург')
# stadium3.set_capacity(94736)
# stadiums.append(stadium3)
#
# stadium4 = Stadium()
# stadium4.set_name('Коттон Боул')
# stadium4.set_opening_date(1994)
# stadium4.set_country("США")
# stadium4.set_city('Даллас')
# stadium4.set_capacity(92100)
# stadiums.append(stadium4)
#
# for i, stadium in enumerate(stadiums, start=1):
#     print(f"\nИнформация о stadium{i}:")
#     print('Название стадиона:', stadium.get_name())
#     print('Год открытия стадиона:',stadium.get_opening_date())
#     print('Страна расположения стадиона:', stadium.get_country())
#     print('Город расположения стадиона:', stadium.get_city())
#     print('Вместимость стадтона:', stadium.get_capacity())
#
#
















