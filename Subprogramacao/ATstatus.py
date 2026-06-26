def verificar_media(media):
    if media >= 6 :
        return "Aprovado"
    elif media >= 4:
        return "Verificaçao Suplementar"
    else:
        return "Reprovado"
    
nota = float(input("Digite a media do aluno: "))

print(f"Status do aluno: {verificar_media(nota)}")






#
