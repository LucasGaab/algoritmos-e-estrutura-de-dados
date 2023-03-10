# Classe nó que armazena propriedades da árvore
class Node:
    def __init__(self, valor, pai=None):
        self.valor = valor
        self.pai = pai
        self.filho_direito = None
        self.filho_esquerdo = None
        self.altura = 0

# Classe que representa a árvore AVL em si 
class ArvoreAVL:
    def __init__(self):
        self.raiz = None
    
    # Funções que coletam a altura da árvore    
    def altura(self):
        if self.raiz:
            return self.calcular_altura(self.raiz)

    def calcular_altura(self, no):
        # A altura do nó  é o valor máximo entre a altura a sua direita e esquerda + 1
        if not no:
            return -1
        return no.altura
    
    # Funções que fazem a inserção de um novo nó
    def inserir(self, valor):
        # se a raiz não existe
        if not self.raiz:
            self.raiz = Node(valor)
            print(f'{valor} INSERIDO')
        else:
            self.inserir_valor(valor, self.raiz)
            print(f'{valor} INSERIDO')
            
    def inserir_valor(self, valor, no):
        if valor < no.valor:
            if no.filho_esquerdo:
                self.inserir_valor(valor, no.filho_esquerdo)
            else:
                no.filho_esquerdo = Node(valor, no)
                self.check_balanceamento(no.filho_esquerdo)
        if valor > no.valor:
            if no.filho_direito:
                self.inserir_valor(valor, no.filho_direito)
            else:
                no.filho_direito = Node(valor, no)
                self.check_balanceamento(no.filho_direito)        
                
    # Funções que fazem a remoção de um nó
    def remover(self, valor):
      self.remover_valor(valor, self.raiz)
            
    def remover_valor(self, valor, no):
      
      # Condicionais para cada tipo de nó a ser removido
        if valor < no.valor:
            if no.filho_esquerdo:
                self.remover_valor(valor, no.filho_esquerdo)
        elif valor > no.valor:
            if no.filho_direito:
                self.remover_valor(valor, no.filho_direito)
        elif valor == no.valor:
            # se for uma folha
            if not no.filho_esquerdo and not no.filho_direito:
                no_pai = no.pai
                if no_pai:
                    if no_pai.filho_esquerdo == no:
                        no_pai.filho_esquerdo = None
                    elif no_pai.filho_direito == no:
                        no_pai.filho_direito = None
                # se for raiz
                else:
                    self.raiz = None
                del no
                print(f'{valor} DELETADO')
                self.check_balanceamento(no_pai)
            # se o filho a esquerda existir
            elif no.filho_esquerdo and not no.filho_direito:
                no_pai = no.pai
                
                if no_pai:
                    if no_pai.filho_esquerdo == no:
                        no_pai.filho_esquerdo = no.filho_esquerdo
                    elif no_pai.filho_direito == no:
                        no_pai.filho_direito = no.filho_esquerdo
                else:
                    self.raiz = no.filho_esquerdo
                    
                no.filho_esquerdo.pai = no_pai
                del no
                print(f'{valor} DELETADO')
                self.check_balanceamento(no_pai)
            # se o filho a direita existir
            elif no.filho_direito and not no.filho_esquerdo:
                no_pai = no.pai
                
                if no_pai:
                    if no_pai.filho_esquerdo == no:
                        no_pai.filho_esquerdo = no.filho_direito
                    elif no_pai.filho_direito == no:
                        no_pai.filho_direito = no.filho_direito
                else:
                    self.raiz = no.filho_direito
                    
                no.filho_direito.pai = no_pai
                del no
                print(f'{valor} DELETADO')
                self.check_balanceamento(no_pai)
            # se o nó tiver os dois filhos
            elif no.filho_esquerdo and no.filho_direito:
                no_sucessor = self.sucessor(no.filho_direito)
                no_sucessor.valor, no.valor = no.valor, no_sucessor.valor
                self.remover_valor(no_sucessor.valor, no.filho_direito)
    
    # Função auxiliar que encontra o sucessor do nó            
    def sucessor(self, no):
        if no.filho_esquerdo:
            return self.sucessor(no.filho_esquerdo)
        return no
        
    # Função que calcula o fato de balanceamento        
    def balanceamento(self, no):
        if not no:
            return 0
        return self.calcular_altura(no.filho_esquerdo) - self.calcular_altura(no.filho_direito)
    
    # Função que realiza uma rotação a direita
    def rotacao_direita(self, no):
        temp_filho_esquerdo = no.filho_esquerdo
        t = no.filho_esquerdo.filho_direito
        
        temp_filho_esquerdo.filho_direito = no
        no.filho_esquerdo = t
        
        temp_parent = no.pai
        temp_filho_esquerdo.pai = temp_parent
        no.pai = temp_filho_esquerdo
        if t:
            t.pai = no
            
        if temp_filho_esquerdo.pai:
            if temp_filho_esquerdo.pai.filho_esquerdo == no:
                temp_filho_esquerdo.pai.filho_esquerdo = temp_filho_esquerdo
            elif temp_filho_esquerdo.pai.filho_direito == no:
                temp_filho_esquerdo.pai.filho_direito = temp_filho_esquerdo
        else:
            self.raiz = temp_filho_esquerdo
            
        # atualizar altura
        no.altura = max(self.calcular_altura(no.filho_esquerdo), self.calcular_altura(no.filho_direito)) + 1
        temp_filho_esquerdo.altura = max(self.calcular_altura(temp_filho_esquerdo.filho_esquerdo),
                                    self.calcular_altura(temp_filho_esquerdo.filho_direito)) + 1
    
    # Função que realiza uma rotação a esquerda                                
    def rotacao_esquerda(self, no):
        temp_filho_direito = no.filho_direito
        t = no.filho_direito.filho_esquerdo
        
        temp_filho_direito.filho_esquerdo = no
        no.filho_direito = t
        
        temp_parent = no.pai
        temp_filho_direito.pai = temp_parent
        no.pai = temp_filho_direito
        if t:
            t.pai = no
            
        if temp_filho_direito.pai:   # se não for a raiz
            if temp_filho_direito.pai.filho_esquerdo == no:
                temp_filho_direito.pai.filho_esquerdo = temp_filho_direito
            elif temp_filho_direito.pai.filho_direito == no:
                temp_filho_direito.pai.filho_direito = temp_filho_direito
        # se for a raiz
        else:
            self.raiz = temp_filho_direito
            
        # atualizar altura
        no.altura = max(self.calcular_altura(no.filho_esquerdo), self.calcular_altura(no.filho_direito)) + 1
        temp_filho_direito.altura = max(self.calcular_altura(temp_filho_direito.filho_esquerdo),
                                    self.calcular_altura(temp_filho_direito.filho_direito)) + 1   
                                    
    #Função responsável por realizar as rotações necessárias
    def rotacao(self, no):
        if self.balanceamento(no) > 1:
            if self.balanceamento(no.filho_esquerdo) < 0:
                self.rotacao_esquerda(no.filho_esquerdo)
            self.rotacao_direita(no)

        if self.balanceamento(no) < 0:
            if self.balanceamento(no.filho_direito) > 0:
                self.rotacao_direita(no.filho_direito)
            self.rotacao_esquerda(no)
                                    
    # Função que verifica se a árvore AVL viola o balanceamento após inserir ou remover um nó.                                
    def check_balanceamento(self, no):
        while no:
            no.altura = max(self.calcular_altura(no.filho_esquerdo), self.calcular_altura(no.filho_direito)) + 1
            self.rotacao(no)
            no = no.pai
    
    # Função responsável por percorrer a árvore e imprimir seus nós em uma determinada ordem.
    def percorrer(self):
        if self.raiz:
            self.em_ordem_(self.raiz)
            return True
        else:
            print('ARVORE VAZIA')
            return False
    # Função responsável por percorrer a árvore em ordem simétrica
    def em_ordem_(self, no):
        if no.filho_esquerdo:
            self.em_ordem_(no.filho_esquerdo)

        elementos_emordem.append(no.valor)

        if no.filho_direito:
            self.em_ordem_(no.filho_direito)

    # Funções responsáveis por buscar um valor na árvore e retornar o nó que contém esse valor
    def buscar(self, valor):
        if self.raiz:
            return self.buscar_valor(valor, self.raiz)

    def buscar_valor(self, valor, no):
        if valor < no.valor:
            if no.filho_esquerdo:
                return self.buscar_valor(valor, no.filho_esquerdo)
        elif valor > no.valor:
            if no.filho_direito:
                return self.buscar_valor(valor, no.filho_direito)
        elif valor == no.valor:
            return True
        return False

    # Funções que buscam o menor valor lexicografico
    def minimo(self):
        if self.raiz:
            return self.buscar_minimo(self.raiz)
        else:
            return 'ARVORE VAZIA'

    def buscar_minimo(self, no):
        if no.filho_esquerdo:
            return self.buscar_minimo(no.filho_esquerdo)
        return f'MENOR: {no.valor}'
    
    # Funções que buscam o maior valor lexicografico
    def maximo(self):
        if self.raiz:
            return self.buscar_maximo(self.raiz)
        else:
            return 'ARVORE VAZIA'

    def buscar_maximo(self, no):
        if no.filho_direito:
            return self.buscar_maximo(no.filho_direito)
        return f'MAIOR: {no.valor}'
        
        
# cria a árvore vazia
arvore = ArvoreAVL()

elementos_emordem = []  # variavel para imprimir os elementos

funcionando = True

# Recebendo entradas e realizando as operações
while funcionando:
    entrada = input().split()

    if entrada[0] == 'INSERIR':
        if arvore.buscar(entrada[1]):
            print(f'{entrada[1]} JA EXISTE')
        else:
            arvore.inserir(entrada[1])

    elif entrada[0] == 'DELETAR':
        if arvore.buscar(entrada[1]):
            arvore.remover(entrada[1])
        else:
            print(f'{entrada[1]} NAO ENCONTRADO')

    elif entrada[0] == 'MINIMO':
        print(arvore.minimo())

    elif entrada[0] == 'MAXIMO':
        print(arvore.maximo())

    elif entrada[0] == 'ALTURA':
        print(f'ALTURA: {arvore.altura() + 1}')

    elif entrada[0] == 'FIM':
        if arvore.percorrer():
            em_ordem = ' '.join(map(str, elementos_emordem))
            print(em_ordem)
            
        funcionando = False    