for i in range(0, 256):
    print(f"{i} -> {chr(i)}", end="  ")
    
    if (i + 1) % 20 == 0:
        continuar = input("\nContinuar? (s/n): ")
        if continuar.lower() != 's':
            break