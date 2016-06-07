import turtle

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


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

# square(bob, 100)
polygon(bob, 100, 6)

# rysowane są punkty?

# okno będzie oczekiwało na akcję użytkownika (np. zamknięcie okna)
turtle.mainloop()
