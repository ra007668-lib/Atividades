def verificar_idade(media):
    if media >= 18 :
        return "Acesso Permitido"
    else:
        return "Acesso Negado"
    
nota = float(input("Digite a sua idade: "))

print(f"Sistema: {verificar_idade(nota)}")