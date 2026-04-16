num = int(input("Quantos números deseja usar: "))

contador = 0

for i in range(1, num):
    print(f"{num} + {i} = {num + i}")
    print(f"{num} - {i} = {num - i}")
    print(f"{num} * {i} = {num * i}")
    
    if i != 0:
        print(f"{num} / {i} = {num / i}")
    
    contador += 4  

print("Total de operações:", contador)