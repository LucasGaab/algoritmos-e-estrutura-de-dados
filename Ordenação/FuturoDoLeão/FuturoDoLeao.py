# Função responsável por calcular a mediana entre os salários
def mediana(salario_sport, futuro_salario):
    lista_ordenada = []
    i = j = 0
    
    # Mergesort das duas listas ordenando-as em uma nova lista
    while i < len(salario_sport) and j < len(futuro_salario):
        if salario_sport[i] < futuro_salario[j]:
            lista_ordenada.append(salario_sport[i])
            i += 1
        else:
            lista_ordenada.append(futuro_salario[j])
            j += 1
    lista_ordenada += salario_sport[i:]
    lista_ordenada += futuro_salario[j:]
    n = len(lista_ordenada)
    
    # Retirando a mediana
    if n % 2 == 0:
        return '{:.2f}'.format((lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2)
    else:
        return '{:.2f}'.format(lista_ordenada[n//2])


# Recebendo salários, rodando a função e printando saída
salario_sport = list(map(int, input().split()))
futuro_salario = list(map(int, input().split()))

print('O salário sugerido por Juba na primeira negociação será de', mediana(salario_sport, futuro_salario), 'mil reais.')
