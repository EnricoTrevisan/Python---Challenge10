def validar_senha(senha):

    if len(senha) < 8:
        return False

    e_numero = False
    e_maiscula = False
    
    for letra in senha:
        if letra >= "0" and letra <= "9":
            e_numero = True
        if letra >= "A" and letra <= "Z":
            e_maiscula = True

    if e_numero and e_maiscula:
        return True
    else:
        return False

senha_usuario = input("Digite sua senha, de acordo aos nossos termos (1° Tenha oitos letras, 2° Tenha uma letra maiscúla, 3° Tenha um número): ")

if validar_senha(senha_usuario):
    print("Sua senha está correta de acordo com nossos termos. Obrigado.")
else:
    print("A sua senha não está correta de acordo com nossos termos. Tente novamente.")