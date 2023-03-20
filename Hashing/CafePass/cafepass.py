def calculadora_array(cpf):
    # Converte o CPF em uma lista de dígitos multiplicados por 10
    array = [int(digito) * 10 for digito in cpf]
    
    # Cria a tabela hash com um vetor de 100 posições
    tabela_hash = [None] * 100
    
    # Remove os dígitos repetidos, somando seus valores
    for digito in array:
        indice = digito % 100
        if tabela_hash[indice] == None:
            tabela_hash[indice] = digito
        else:
            tabela_hash[indice] += digito
    
    return tabela_hash


# Função que recebe um CPF e o magic number e retonar as saídas
def autorizar(cpf, mn):
    lista_cpf = calculadora_array(cpf)
    achou = False
    aprovados = []
    
    for v in lista_cpf:
        if v is None:
            continue
        else:
            calculo = mn - v
            if calculo in lista_cpf:
                if calculo != v or lista_cpf.count(calculo) > 1:
                    achou = True
                    break
                else:
                    if calculo not in aprovados:
                        aprovados.append(calculo)
    
    if achou:
        return "UP Permission"
    else:
        return "NOT Permission"


# Recebendo as entradas e chamando a função
n = int(input())
for i in range(n):
    cpf, mn = input().split()
    mn = int(mn)
    print(autorizar(cpf, mn))