import datetime
import random
from faker import Faker
fake = Faker('en_Us')


class MovieLibrary:
    def __init__(self, number, title, sub_title, publication_date, type_mov, movie_flag):
        self.next = number
        self.title = title
        self.subtitle = sub_title
        self.publication_date = publication_date
        self.type_mov = type_mov
        self.movie_flag = movie_flag

        # VariablesClass
        self.numbers_ofreplays = 0

    def __repr__(self):
        return f'\n{self.next} / {self.title.capitalize()} {self.subtitle} / {self.publication_date} / {self.type_mov} / {self.numbers_ofreplays} \n'

    def play_movie(self, step=random.randrange(2, 100)):
        self.numbers_ofreplays += step

# klasa ktora dziedziczy


class SeriesLibrary(MovieLibrary):
    def __init__(self, episod_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episod_number = episod_number
        self.season_number = season_number

    def __repr__(self):
        return f'\n{self.next} / {self.title.capitalize()} {self.subtitle} / {self.publication_date} / {self.type_mov}  / E{self.episod_number}S{self.season_number} / {self.numbers_ofreplays}\n'

    def play_movie(self, step=random.randrange(2, 100)):
        self.numbers_ofreplays += step
# Funkcje do konstrukcji listy filmow i seriali


def create_movies():
    library.append(MovieLibrary(title=fake.word(), sub_title=fake.word(), publication_date=fake.date_between(
        '-50y'), type_mov=random.choice(['Documentary', 'Thriller', 'Horror', 'Action', 'Comedy', 'Family', 'Romantic']), number=number_, movie_flag=1))


def create_series():
    library.append(SeriesLibrary(title=fake.word(), sub_title=fake.word(), publication_date=fake.date_between(
        '-10y'), type_mov=random.choice(['Documentary', 'Thriller', 'Horror', 'Action', 'Comedy', 'Family', 'Romantic']), number=number_, movie_flag=2, episod_number=str(random.randrange(1, 10)).zfill(2), season_number=str(random.randrange(1, 10)).zfill(2)))

# funkcje do pobierania wylacznie filmow albo wylacznie seriali


def get_movies():
    for movie in library:
        if movie.movie_flag == 1:
            only_movie_ = only_movie.append(movie)
    return only_movie_


def get_series():
    for series in library:
        if series.movie_flag == 2:
            only_series_ = only_series.append(series)
    return only_series_

# funkcja do szukania filmow badz seriali


def search():
    searching_title = input(
        "Podaj pierwszy człon tytułu \n").lower()
    searching_subtitle = input("Podaj drugi człon tytułu\n")
    for x in library:
        x.title
        if x.title == searching_title and x.subtitle == searching_subtitle:
            return f'Film/Serial {searching_title.capitalize()} {searching_subtitle} znajduje sie w bibliotece'
    raise ValueError(
        f"Niestety {searching_title.capitalize()} {searching_subtitle} nie ma w naszej Bibliotece")
# Generator oddworzeń


def generate_views(y, x):
    for z in range(y):
        z = library[random.randrange(x)]
        z.play_movie()

# Top Titles


def top_titles():
    by_top = sorted(
        library, key=lambda top: top.numbers_ofreplays)
    by_top.reverse()
    return by_top


# menu


def menu():
    return ' Menu Programu:\n [1] Uzycie Funkcji która zwraca jedynie filmy\n [2] Uzucie funkcji która zwraca jedynie seriale\n [3] Uzycie funkcji która daje mozliwosc wyszukania filmu bądz serialu po tytule\n [4] Funkcja zwrcajaca top Titles z najwieksza liczba wyswietleń\n [5] Wyswietl cała listę filmow oraz seriali [0] Zakonczenie programu'


# Content Menager.
# Viarlabeles
library = []
number_ = 0
only_movie = []
only_series = []
numbers_of_viev = []
sorted_numbers_of_viev = []
sorted_end = []
loops = 3
date = datetime.datetime.today()

print("Biblioteka Filmów")
numbers_of_movie = int(input("Podaj liczbe filmów do wygenerowania\n"))
numbers_of_series = int(input("Podaj liczbe seriali do wygenerowania\n"))

for i in range(int(numbers_of_movie)):
    create_movies()
    number_ += 1


for i in range(int(numbers_of_series)):
    create_series()
    number_ += 1

generate_views(10, (numbers_of_movie+numbers_of_series))
get_movies()
get_series()


numbers_of_viev.append(top_titles())
for i in numbers_of_viev:
    for x in i:
        sorted_numbers_of_viev.append(x)

for z in sorted_numbers_of_viev:
    sorted_end.append(z)
    loops -= 1
    if loops == 0:
        break


print(menu())
option = int(input("Wpisz swoj wybor: "))
while option != 0:
    if option == 1:
        print("Lista Zawiera Jedynie Filmy")
        for i in only_movie:
            print(i)
        print(menu())
        option = int(input("Wpisz swoj wybor: "))

    elif option == 2:
        print("Lista zawiera jedynie Seriale")
        for i in only_series:
            print(i)
        print(menu())
        option = int(input("Wpisz swoj wybor: "))

    elif option == 3:
        print(search())
        print(menu())
        option = int(input("Wpisz swoj wybor: "))

    elif option == 4:
        print(
            f'Ponizej wyswitlam liste 3 Filmow / Seriali z najwieksza liczba oddworzen na dzień {date.strftime("%d-%m-%Y %H:%M")}')
        for i in sorted_end:
            print(i)
        print(menu())
        option = int(input("Wpisz swoj wybor: "))
    elif option == 5:
        print(library)
        print(menu())
        option = int(input("Wpisz swoj wybor: "))
print("Dziękuje za skorzystanie z programu")
