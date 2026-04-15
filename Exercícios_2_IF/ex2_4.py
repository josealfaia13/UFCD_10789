saldo = 0
cheque = 0

saldo = int(input("Insira o seu saldo: "))
cheque = int(input("Insira o valor do seu cheque: "))

if saldo > cheque:
    desconto = saldo - cheque
    print(f"Cheque descontado, saldo: {desconto}")
else:
    print("Não tem saldo sufeciente para descontar o cheque")