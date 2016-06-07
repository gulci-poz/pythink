import math

# function - a named sequence of statements that performs a computation

# funkcja int obcina część ułamkową
print(int('32'))
print(int(3.9999))

print(float('32.9999'))
print(float(4))

print(str(32))
print(str(32.9999))

# moduł - kolekcja funkcji i zmiennych - plik
# pakiet - zbiór modułów - folder

# python tworzy obiekt modułu
print(math)
print(math.log10(10))
# podstawą jest liczba e
print(math.log(10))
# kąt w radianach
print(math.sin(0.5))

# pi = 180
deg = 180
rad = deg * math.pi / 180
print(rad)

rad = 1
deg = rad * 180 / math.pi
print(deg)

print(math.sin(45 * math.pi / 180))
print(math.sin(math.radians(45)))
# ewaluacja wartości dla sinusa daje nam trochę inny wynik niż funkcja sin
print(math.sqrt(2) / 2)

x = math.sin(math.radians(45))
# e ** (log(x)) = x
print(math.exp(math.log(x)))
# e ** x
print(math.exp(x))
print(math.e ** x)
print(math.pow(math.e, x))


# py tworzy obiekt typu function
# definicja zostaje wykonana, ale nie generuje nic na wyjściu
# ewaluacja argumentów następuje przed wywołaniem funkcji
# wewnątrz funkcji argumentu zostają przypisane do parametrów
# parametry i zmienne zadeklarowane wewnątrz funkcji są lokalne
def printsth():
    print('sth')
    # możemy oznakować zmienną jako globalną
    # txt = 'hello'
    # global txt

# wywołanie musi nastąpić po definicji
# inaczej python nie rozpozna identyfikatora
print(printsth)
print(type(printsth))
printsth()
# print(txt)

# stack diagram, oprócz state diagram (wartości zmiennych)
# pokazuje też funkcję, do której należą zmienne
# __main__ - główna funkcja wykonywanego skryptu (nie modułu)
# moduł może być wykonany jako skrypt
# lista funkcji ze stosu to traceback

# void functions; "fruitful functions" - zwracają wartość

# zostanie przypisana wartość None, funkcja nic nie zwraca
# sth = printsth()
# print(sth)
# specjalny typ NoneType
print(type(None))

# programowanie ~ stopniowe debugowanie, aż do poprawnego działania


def right_justify(txt):
    return (70 - len(txt)) * ' ' + txt

print(right_justify('hello'))
print(right_justify('world'))
print(right_justify('the zen of python'))


def rjust_twice(f, txt):
    print(f(txt))
    print(f(txt))

rjust_twice(right_justify, 'guido')


def draw_edge(dimx):
    return ('+ ' + '- ' * 4) * dimx + '+' + '\n'


def draw_internal(dimx):
    return ('|' + ' ' * 9) * dimx + '|' + '\n'


def draw_square(dimx):
    return draw_edge(dimx) + draw_internal(dimx) * 4


def draw_grid(dimx, dimy):
    print(draw_square(dimx) * dimy + draw_edge(dimx))

draw_grid(10, 2)
