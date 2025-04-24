def e_vogais(lista):

    vogais = "aeiouAEIOU" 
    contador = 0

    for achar in lista:
        if achar in vogais:
            contador +=1

    return contador

lista = input("Digite a palavra: ")
num_de_vogais = e_vogais(lista)
print(F"O número de vogais no seu texto é: {num_de_vogais}")