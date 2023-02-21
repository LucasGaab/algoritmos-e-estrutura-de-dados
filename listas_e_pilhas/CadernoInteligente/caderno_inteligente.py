#Função para verificação das pilhas
def verificar_pilha(pilha):
    #Variável que mantém o controle das capas
    pilha_temporaria = []
    
    #Laço que percorre a pilha de capas e seus índices
    for i, capa in enumerate(pilha):
        if capa == "F":
            pilha_temporaria.append(i)
            
        elif not pilha_temporaria:
          return f"Incorreto, devido a capa na posição {i+1}."
          
        else:
          pilha_temporaria.pop(0)
          
    #Se a lista não estiver vazia, o caderno está incorreto
    if pilha_temporaria:
        return f"Incorreto, devido a capa na posição {pilha_temporaria[0] + 1}."
    else:
      return "Correto."

#Recebendo a pilha de capas e chamando a função
pilha = input().strip()
print(verificar_pilha(pilha))
