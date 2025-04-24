def e_maior_valor(lista):
    maior_valor = lista[0]
    for numero in lista:
        if numero > maior_valor:
            maior_valor = numero
    return maior_valor

lista = [10, 56, 89, 105, 96, 25, 36, 54]
maior = e_maior_valor(lista)
print(f"O maior valor da lista é {maior}")