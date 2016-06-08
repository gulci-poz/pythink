import turtle
import math

# funkcja Turtle() tworzy obiekt typu Turtle
bob = turtle.Turtle()
print(bob)

# grot strzałki
# bob.pu()
# bob.fd(100)
# bob.pd()
# bob.lt(135)
# bob.fd(50)
# bob.bk(50)
# bob.rt(270)
# bob.fd(50)


# w py2 w dzieleniu powinniśmy mieć przynajmniej jedną wartość float
# żeby otrzymać nieobciętą wartość float
def polygon(t, length, n, angle):
    # docstring - dokumentacja interfejsu
    """
    rysuje wielokąt równoboczny
    parametr n określa ile boków ma wielokąt
    parametr angle określa za pomocą wartości kąta,
    ile boków będzie wyrysowanych
    angle powinien mieć wartość [1, n]
    """
    for i in range(angle):
        t.fd(length)
        t.lt(360 / n)


def square(t, length):
    polygon(t, length, 4, 4)


# ustawienie żółwika na punkcie początkowym okręgu - godzina 3, kierunek N
def set_turtle_arc(t, radius):
    t.pu()
    t.fd(radius)
    t.lt(90)
    t.pd()


def circumference(radius):
    return 2 * math.pi * radius


# przyjmujemy, że obracamy się o jeden stopień, czyli rysujemy wielokąt
# o 360 bokach
# dla małych promieni będziemy rysowali bardzo krókie boki
def arc(t, radius, angle):
    set_turtle_arc(t, radius)
    polygon(t, circumference(radius) / 360, 360, angle)


def circle(t, radius):
    arc(t, radius, 360)

# możemy używać keyword arguments
# square(bob, length=100)
# polygon(bob, length=100, n=6, angle=6)
# polygon(bob, 100, 6, 4)
# circle(bob, 200)
arc(bob, radius=150, angle=45)

# czy tak naprawdę rysowane są punkty? linia jako kolejno rysowane punkty
# co z bardzo krótkimi liniami?

# poniższe pojęcia dotyczą projektowania interfejsu funkcji, a nie OOP

# opakowanie kodu operującego na przekazanych danych w funkcję to enkapsulacja
# klasyczne w OOP to zastrzeżenie dostępu do wybranych danych

# dodanie parametru do funkcji (zamiast twardego kodowania liczb)
# to generalizacja

# interfejs funkcji - podsumowanie użycia: parametry, co robi funkcja, co zwraca
# czysty interfejs umożliwia użytkownikowi wykonanie zadania bez zagłębiania
# się w nieistotne szczegóły
# np. dla łuku częścią interfejsu jest r, ale nie n
# n to lokalna zmienna, która określa dokładność rysowania łuku - ilość
# boków, które przybliżają łuk, to nie musi być istotne dla użytkownika
# r - what, n - how

# refactoring - rearanżacja programu, ulepszenie interfejsów i zapewnienie
# możliwości ponownego wykorzystania kodu

# preconditions - argumenty; postconditions - intended effect, side effects

# okno będzie oczekiwało na akcję użytkownika (np. zamknięcie okna)
turtle.mainloop()
