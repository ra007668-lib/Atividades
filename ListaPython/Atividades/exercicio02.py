def soma_impares():
    a = int(input("Digite o valor de 'a': "))
    b = int(input("Digite o valor de 'b': "))
    

    if a >= b:
        print("Erro: 'a' deve ser menor que 'b'.")
        return
    
    soma = 0
    impares = []
    

    for i in range(a + 1, b):
        if i % 2 != 0:  
            soma += i
            impares.append(str(i))
            
    # Exibe o resultado formatado
    expressao = " + ".join(impares)
    print(f"Saída: {expressao} = {soma}")

soma_impares()
