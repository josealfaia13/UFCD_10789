soma = 0
contador = 0

while contador < 30:
    num = int(input("Digite um número par entre 1 e 50: "))
    
    if 1 <= num <= 50 and num % 2 == 0:
        soma += num
        contador += 1
    else:
        print("Número inválido!")

media = soma / 30
print("Média:", media)