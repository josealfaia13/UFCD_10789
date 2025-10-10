sec = 0
min = 0
hor = 0

sec = int(input("Insira os segundos: "))
print(sec)

min = int(sec / 60)
hor = int(min / 60)
secrest = int(sec%60)
minrest = int(min%60)

print(f"{hor} horas, {minrest} minutos, {secrest} segundos")