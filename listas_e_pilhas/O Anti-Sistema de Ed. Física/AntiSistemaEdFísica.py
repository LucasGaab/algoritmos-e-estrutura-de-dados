def checkar_ordem_pilha(pilha_local):
    #Verifica se a pilha está em ordem crescente (pilha imaculada)
    for i in range(1, len(pilha_local)):
        if pilha_local[i] < pilha_local[i-1]:
            return False
    #Retorna True se a pilha está em ordem crescente
    return True

def adicionar_locacao(pilha_local, codigo_local):
    #Verifica se a pilha está em ordem crescente
    if not checkar_ordem_pilha(pilha_local):
        #Se não está em ordem, está um caos:
        print("A pilha está um caos.")
        return
    #Percorre a pilha
    for i in range(len(pilha_local)):
        if codigo_local < pilha_local[i]:
            #Insere a nova locação na posição atual da pilha
            pilha_local.insert(i, codigo_local)
            break
    else:
        #Se a nova locação não foi adicionada, adiciona no final da pilha
        pilha_local.append(codigo_local)
    print(pilha_local)

#Recebendo e tratando as entradas
pilha = input().split(',')
codigo = input()

#Executando a função
adicionar_locacao(pilha, codigo)