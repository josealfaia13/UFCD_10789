num1 = int(input("Insira um número: "))

num2 = int(input("Insira outro número: "))

num3 = int(input("Insira so mais um númeor: "))

print(f"1º número-{num1}, 2º número-{num2}, 3º número-{num3}\n")

if num1 > num2 and num2 > num3:
    print(f"{num1} é o maior e o menor é o {num3}") 
elif num1 > num3 and num3 > num2:
    print(f"{num1} é o maior e o menor é o {num2}") 
elif num2 > num3 and num3 > num1:
    print(f"{num2} é o maoir e o menor é o {num1}")
elif num2 > num1 and  num1 > num3 :
    print(f"{num2} é o maoir e o menor é o {num3}")
elif num3 > num2 and num2 > num1:
    print(f"{num3} é o maoir e o menor é o {num1}")    
elif num3 > num1 and num1 > num2:
    print(f"{num3} é o maior e o menor é  o {num2}")
   