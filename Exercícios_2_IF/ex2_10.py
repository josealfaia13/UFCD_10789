nums = []

for i in range(10):
    num = int(input(f"Insira um número {i+1}: "))
    nums.append(num)

contador_par = 0
contador_impar = 0

for num in nums:
    if num % 2 == 0:
       contador_par +=1
    else:
        contador_impar +=1

print(f"Pares: {contador_par}")
print(f"ímpares: {contador_impar}")
