nota1 = 0
nota2 = 0
nota3 = 0

nota1 = int(input("Insira uma nota: "))
nota2 = int(input("Insira uma outra nota: "))
nota3 = int(input("Insira so mais uma nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"{media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")