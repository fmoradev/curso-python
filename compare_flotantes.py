x = 3.3
y = 1.1 + 2.2
print(x)
print(y)
print(x == y)

#strings
y_str = format(y, ".2g") # dos digitos
print(y_str)
print(str(x) == y_str)

#matematica
print("*" * 10)
print(x, y)
tolerance = 0.00001
print(abs(x - y) < tolerance)