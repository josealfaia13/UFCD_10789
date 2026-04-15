num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Insira um número: "))
num2 = int(input("Insira um outro número: "))
num3 = int(input("Insira so mais um outro número: "))

if num1 > num2 and num2 > num3:
    print(f"{num1} Maior \n {num3} Menor")
elif num1 > num3 and num3 > num2:
    print(f"{num1} Maior \n {num2} Menor")
elif num2 > num3 and num3 > num1:
    print(f"{num2} Maior \n {num1} Menor")
elif num2 > num1 and num1 > num3:
    print(f"{num2} Maior \n {num3} Menor")
elif num3 > num1 and num1 > num2:
    print(f"{num3} Maior \n {num2} Menor")
elif num3 > num2 and num2 > num1:
    print(f"{num3} Maior \n {num1} Menor")
else:
    print("erro!!")
