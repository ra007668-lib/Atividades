x = int(input("Digite o valor de x (dividendo): "))
y = int(input("Digite o valor de y (divisor): "))

if y == 0:
    print("Erro: Divisão por zero não é permitida.")
else:
    quociente = 0
    resto = x

    # Subtrai o y de x até que x seja menor que y
    while resto >= y:
        resto -= y
        quociente += 1

    print(f"\nResultado de {x} dividido por {y}: {quociente}")
    print(f"Resto da divisão: {resto}")