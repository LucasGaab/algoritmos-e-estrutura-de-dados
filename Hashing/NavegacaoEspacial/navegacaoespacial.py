# Recebe o numeroúmero de espaços disponíveis no centro de dados da nave
numero = int(input())

# Cria uma lista vazia com numero posições
memoria = [None] * numero

# Recebe o numeroúmero de comandos que serão executados
qtd_comandos = int(input())

# Para cada comando, executa a operação correspondente
for i in range(qtd_comandos):
    comando = input().split()
    
    # Operação ADD - adiciona o dado na posição correspondente da memória
    if comando[0] == 'ADD':
        x = int(comando[1])
        posicao = x % numero
        adicionado = False

        while not adicionado:
            if memoria[posicao] is None:
                memoria[posicao] = x
                adicionado = True
                print(f"E: {posicao}")
            posicao = (posicao + 1) 
            
    # Operação SEARCH - busca o dado na memória
    elif comando[0] == 'SCH':
        dado = int(comando[1])
        posicao_dado = dado % numero
        encontrado = False
    
        while not encontrado:
            if memoria[posicao_dado] == dado:
                print(f"E: {posicao_dado}")
                encontrado = True
            elif memoria[posicao_dado] is None:
                print("NE")
                encontrado = True
    
            posicao_dado = (posicao_dado + 1) % numero
    
            # Se a lista estiver completamente percorrida e o dado não for encontrado, imprime NE
            if posicao_dado == dado % numero:
                print("NE")
                encontrado = True
    
    # Operação CAP - consulta a disponibilidade de armazenamento em um endereço de memória
    elif comando[0] == 'CAP':
        endereco = int(comando[1])
        if memoria[endereco] is None:
            print("D")
        else:
            print(f"A: {memoria[endereco]}")