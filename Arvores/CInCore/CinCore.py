# Classe que representa um nó da árvore, contendo o valor, ponteiros e nível
class Node:
    def __init__(self, valor=None, nivel=0):
        self.valor = valor
        self.nivel = nivel
        self.esquerda = None
        self.direita = None
        self.pai = None

# Classe que representa a árvore de busca binária
class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None  # inicializa a raiz da árvore como nula
    
    # Adiciona um novo nó na árvore
    def adicionar(self, valor):
        if self.raiz is None:  # se o nó atual for nulo, cria um novo nó com o valor
            self.raiz = Node(valor)
            return 0
            
        no_atual = self.raiz
        nivel = 0
        no = Node(valor)  # cria um novo nó para ser adicionado
        
        # realiza a busca do local adequado para o novo nó na árvore
        while True:
            nivel += 1
            if valor < no_atual.valor:
                if no_atual.esquerda:
                    no_atual = no_atual.esquerda
                else:
                    no_atual.esquerda = no
                    no.pai = no_atual
                    no.nivel = nivel
                    return nivel
            elif valor > no_atual.valor:
                if no_atual.direita:
                    no_atual = no_atual.direita
                else:
                    no_atual.direita = no
                    no.pai = no_atual
                    no.nivel = nivel
                    return nivel
            else:
                return no_atual.nivel
    
    # Função que realiza a rotação para a esquerda na árvore
    def _rotacionar_esquerda(self, no):
        nova_raiz = no.direita
        no.direita = nova_raiz.esquerda
        if nova_raiz.esquerda is not None:
            nova_raiz.esquerda.pai = no
        nova_raiz.pai = no.pai
        if no.pai is None:
            self.raiz = nova_raiz
        elif no == no.pai.esquerda:
            no.pai.esquerda = nova_raiz
        else:
            no.pai.direita = nova_raiz
        nova_raiz.esquerda = no
        no.pai = nova_raiz
    
    # Função que realiza a rotação para a direita na árvore
    def _rotacionar_direita(self, no):
        nova_raiz = no.esquerda
        no.esquerda = nova_raiz.direita
        if nova_raiz.direita is not None:
            nova_raiz.direita.pai = no
        nova_raiz.pai = no.pai
        if no.pai is None:
            self.raiz = nova_raiz
        elif no == no.pai.direita:
            no.pai.direita = nova_raiz
        else:
            no.pai.esquerda = nova_raiz
        nova_raiz.direita = no
        no.pai = nova_raiz
    
    
    #Função que procura um determinado valor na estrutura
    def procurar(self, valor):
      if not self.raiz:
          return None
        
      no_atual = self.raiz
      nivel = -1
      
      while no_atual:
          nivel += 1
          if valor < no_atual.valor:
              no_atual = no_atual.esquerda
          elif valor > no_atual.valor:
              no_atual = no_atual.direita
          else:
              self.balanceamento(no_atual)
              return nivel   
              
    # Função que equilibra a ávore após a exclusão de um nó
    def balanceamento(self, no):
        pilha = []
        while no.pai is not None:
            pilha.append(no)
            no = no.pai
    
        while pilha:
            no = pilha.pop()
            if no == no.pai.esquerda:
                self._rotacionar_direita(no.pai)
            else:
                self._rotacionar_esquerda(no.pai)
    
        self.raiz = no

arvore = ArvoreBuscaBinaria()

 
# Recebendo as entradas e executando as operações 
while True:
    try:
        entrada = input().split()
        operacao = entrada[0]
        numero = entrada[1]
    except EOFError:
        break
    
    if operacao == 'ADD':
        valor_adicionado = arvore.adicionar(int(numero))
        print(valor_adicionado)
    
    elif operacao == 'SCH':
        valor_encontrado = arvore.procurar(int(numero))
    
        if valor_encontrado is None:
            print('-1')
        else:
            print(valor_encontrado)
    
    else:
        pass