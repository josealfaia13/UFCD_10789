hor = 0 
min = 0
sec = 0

sec = int(input("Insira os segundos que deseja: "))

hor = sec // 3600
resto = sec % 3600

min = resto // 60
sec = resto % 60

print(f"{hor} Horas, {min} Minutos, {sec} Segundos")