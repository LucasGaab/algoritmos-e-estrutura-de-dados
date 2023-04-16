# Definição da função bfs que recebe um grafo, um nó de início e um valor máximo de investimento
def bfs(grafo, inicio, investimento):
    conexoes_gratuitas = grafo[inicio] 
    numeros_abaixo_do_limite = [] # lista de usuários abaixo do limite de investimento
    no_atual = [int(conexao) for conexao in conexoes_gratuitas]
    
    for conexao_gratuita in conexoes_gratuitas:
        numeros_abaixo_do_limite.append(conexao_gratuita) # Guardando as conexoes gratuitas

    # continuar enquanto houver nós a serem explorados e ainda houver investimento
    while no_atual and investimento >= 5.25: 
        proximo_no = []
        
        for conexoes_gratuitas in no_atual:
            for conexao_paga in grafo[conexoes_gratuitas]:
                if investimento >= 5.25:
                    # se a conexão paga ainda não foi explorada e não é o usuário inicial
                    if conexao_paga not in numeros_abaixo_do_limite and int(conexao_paga) != inicio:
                        numeros_abaixo_do_limite.append(conexao_paga)
                        proximo_no.append(int(conexao_paga))
                        investimento -= 5.25 # subtrai o valor do investimento atual
        no_atual = proximo_no

    return numeros_abaixo_do_limite


# Recebendo entradas do usuário
N = int(input())
U = int(input())
B = float(input())

grafo = []

for i in range(N):
    usuario = input().split()
    seguidores = usuario[2:]
    grafo.insert(i, seguidores)

# Rodando a função para retornar o resultado e printando
resultados = bfs(grafo, U, B)
print(resultados)
