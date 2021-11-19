# Смена значений двух переменных

a = 3
b = 5
print("a = ", a, "; b = ", b, "\n")

b = b - a
a = b + a
b = a - b
print("a = ", a, "; b = ", b)