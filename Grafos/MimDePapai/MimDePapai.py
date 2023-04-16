# Função busca em profundidade para calcular o número de usuários que saberiam a notícia
def BuscaProfundidade(vertice, lista_adjacencia, visitados):
    visitados[vertice] = True
    contador = 1
    for vizinho in lista_adjacencia[vertice]:
        if not visitados[vizinho]:
            contador += BuscaProfundidade(vizinho, lista_adjacencia, visitados)
    return contador

# Função que retorna uma lista com o número de usuários que receberiam a notícia a partir de cada usuário da rede social
def distribuicaoNoticas(num_usuarios, num_conexoes, conexoes):
    lista_adjacencia = [[] for i in range(num_usuarios)]
    for u, v in conexoes: # percorre as conexões
        lista_adjacencia[u-1].append(v-1)
        lista_adjacencia[v-1].append(u-1)
    resultado = []
    
    for i in range(num_usuarios): # para cada usuário
        visitados = [False] * num_usuarios
        resultado.append(BuscaProfundidade(i, lista_adjacencia, visitados))
    return resultado

# Recebendo entradas
num_usuarios, num_conexoes = map(int, input().split())
conexoes = []
for i in range(num_conexoes):
    u, v = map(int, input().split())
    conexoes.append((u, v))

# Rodando as funções e imprimindo resultado
resultado = distribuicaoNoticas(num_usuarios, num_conexoes, conexoes)
print(' '.join(map(str, resultado)))
