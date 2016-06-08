import time

print(type(True))
print(type(False))

# python traktuje każdy niezerowy element jako prawdziwy
print(42 and True)

# place keeper
if True:
    pass

x = 9

if 0 < x < 10:
    print('positive single-digit')


def countdown(n):
    if n <= 0:
        print('START')
        # pusty return powoduje wyjście z pętli i powrót do miejsca wywołania
        # nie zwraca żadnej wartości, nawet none
    else:
        print(n)
        time.sleep(0.25)
        countdown(n - 1)

# countdown(10)

# nieskończona rekursja, python dopuszcza 1000 ramek na stosie

# login = input('Login: ')
# print('User:', login)

# komunikaty błędu pokazują, gdzie błąd został wykryty
# błąd mógł wystąpić wcześniej


def retnote():
    pass

noneval = 0
print(noneval)
# funkcja nic nie zwraca, ale dostaniemy wartość None
noneval = retnote()
print(noneval)

# ilość sekund od 01.01.1970 (UNIX epoch, Greenwich)
timenow = time.time()
hours = timenow / 60 / 60
print('full days:', hours // 24)
print(int(int(int(timenow) / 60) / 60) % 60, ':', sep='', end='')
print(int(int(timenow) / 60) % 60, ':', sep='', end='')
print(int(timenow) % 60, 'GMT')
