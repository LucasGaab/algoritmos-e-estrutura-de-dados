class AnalisadorEspacos:
    def __init__(self, x):
        self.x = x
        self.combinacoes = []
    
    # Método público para analisar todas as combinações possíveis
    def analisar(self):
        self._backtrack([], 1, 0)
        self._imprimir_resultados()
    
    # Método privado que realiza o backtracking para encontrar todas as combinações possíveis
    def _backtrack(self, combinacao_principal, partida, soma_atual):
        if soma_atual == self.x:
            combinacao_ordenada = sorted(combinacao_principal)
            if combinacao_ordenada not in self.combinacoes:
                self.combinacoes.append(combinacao_ordenada)
        elif soma_atual < self.x:
            for i in range(partida, self.x + 1):
                nova_soma = soma_atual + i
                if nova_soma <= self.x:
                    combinacao_principal.append(i)
                    self._backtrack(combinacao_principal, i, nova_soma)
                    combinacao_principal.pop()
    
    # Método privado que exibe os resultados encontrados
    def _imprimir_resultados(self):
        print(f"Uma sessão com {self.x} pessoas pode ter sua audiência nos seguintes subgrupos:")
        for combinacao in sorted(self.combinacoes):
            print(combinacao)

# Recebendo entradas para realizar operações
x = int(input())
analisador = AnalisadorEspacos(x)
analisador.analisar()
