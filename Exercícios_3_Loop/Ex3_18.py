limite = int(input("Até que número deseja verificar: "))

for num in range(1, limite + 1):
    soma = 0
    
    for i in range(1, num):
        if num % i == 0:
            soma += i
    
    if soma == num:
        print(f"{num} é perfeito")