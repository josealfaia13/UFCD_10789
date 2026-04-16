a = 1
b = 1

print(a, b, end=" ")

for _ in range(6):  # próximos 6 números
    c = a + b
    print(c, end=" ")
    a = b
    b = c