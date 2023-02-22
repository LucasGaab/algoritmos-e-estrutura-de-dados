#Classe que representa um nó da lista duplamente encadeada
class Node:
    def __init__(self, dado):
      self.dado = dado
      self.anterior = None
      self.proximo = None

    
#Classe que representa a lista duplamente encadeada    
class Lista_duplamente_encadeada:
    def __init__(self):
      self.inicio = None
      self.fim = None   
      
    #Função que adiciona um novo elemento na lista 
    def adicionar(self, dado):
        nodo = Node(dado)
        #Se a lista tiver vazia
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            nodo.anterior = self.fim
            self.fim.proximo = nodo
            self.fim = nodo
            
    
    #Função que remove um elemento da lista
    def remover(self, dado):
      elemento_atual = self.inicio
      #Percorre a lista até o final
      while elemento_atual is not None:
          if elemento_atual.dado == dado:
              #Se o elemento a ser removido é o primeiro da lista
              if elemento_atual == self.inicio:
                  self.inicio = elemento_atual.proximo
              else:
                  elemento_atual.anterior.proximo = elemento_atual.proximo
                    
              #Se o elemento a ser removido é o último da lista    
              if elemento_atual == self.fim:
                  self.fim = elemento_atual.anterior
              else:
                elemento_atual.proximo.anterior = elemento_atual.anterior
              return True
          elemento_atual = elemento_atual.proximo
      return False
                      
    #Função que exibe os dados da lista
    def exibir(self):
      elemento_atual = self.fim
      while elemento_atual is not None:
          print(elemento_atual.dado)
          elemento_atual = elemento_atual.anterior  
            
    #Função que move um elemento da lista para o início        
    def encontrar(self, dado):
      # remove o elemento se ele já existir na lista
      if self.remover(dado):
        # adiciona o elemento no início da lista
        self.adicionar(dado)
        return True
      else:
        return False

#Recebendo entradas e executando as funções
lista = Lista_duplamente_encadeada()

while True:
    comando = input().split()
    if comando[0] == "ADD":
        lista.adicionar(comando[1])
    elif comando[0] == "REM":
        lista.remover(comando[1])
    elif comando[0] == "FIND":
        lista.encontrar(comando[1])
    elif comando[0] == "EXIB":
        lista.exibir()
    elif comando[0] == "END":
        break        