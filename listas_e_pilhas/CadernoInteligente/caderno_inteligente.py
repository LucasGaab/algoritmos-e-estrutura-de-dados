#Função para verificação das pilhas
def verificar_pilha(pilha):
    #Variável que mantém o controle das capas
    pilha_temporaria = []
    for i, capa in enumerate(pilha):
        if capa == "F":
            pilha_temporaria.append(i)
        else:
            if not pilha_temporaria:
                return f"Incorreto, devido a capa na posição {i + 1}."
            pilha_temporaria.pop()
    if pilha_temporaria:
        return f"Incorreto, devido a capa na posição {pilha_temporaria[-1] + 1}."
    return "Correto."

#Recebendo a pilha de capas e chamando a função
pilha = input().strip()
print(verificar_pilha(pilha))