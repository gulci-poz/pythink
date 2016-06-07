# denote, assemble, observe - math, engineer, science
# 1 formulate a problem
# 2 think creatively about solutions
# 3 express a solution clearly and accurately

# nie możemy zapisać liczby za pomocą separatorów
# python utworzy tuple, zera będą obcięte do jednego zera
nums = 1, 000, 000
print(nums)
print(type(nums))

# statement - kawałek kodu, który daje jakiś efekt; nie ma wartości

a = 1
b = 2
a += b / 2
# najpierw zostanie wykonana część wyrażenia po prawej stronie
# potem nastąpi inkrementacja
print(a)

# PEMDAS - nawiasy, potęgi, mnożenie, dzielenie, dodawanie, odejmowanie
# ten sam priorytet - od lewej do prawej, z wyjątkiem potęgowania

strmult = 'str' * 3
print(strmult)

# Syntax Error
# Runtime Error (exceptions)
# Semantic error

x = y = 1
print(x, y)
