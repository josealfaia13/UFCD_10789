num = 0 
num = int(input("Insira um número: "))

match num:
    case 0:
        if num == 0:
            print("O número é 0")
    case _ if num > 0:
        if num %2==0:
            print("O número é par")
        else:
            print("O número é impar")

        if num %3==0 and num%5==0:
            print("O número é divisível por 3 e 5")
        else:
            print("O número não é divisível por 3 nem por 5")    

    case _ if num < 0:
        print("O número é  negativo")


