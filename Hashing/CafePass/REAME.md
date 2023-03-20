# Café Pass

O Centro de Informática estava enfrentando um problema sério com a cafeteira de sua sala de convivência. Alguns alunos estavam consumindo quantidades excessivas de café, deixando pouco para os demais. Para resolver o problema, o time de desenvolvimento do Helpdesk CIn-UFPE, liderado por Charles do Helpdesk, decidiu criar um sistema de autorização experimental chamado "CaféPass" para validar se uma aluna(o) pode acessar a cafeteira da sala de convivência na semana.

## Funcionamento:

Toda Segunda o sistema carrega CPFs dos alunos e forma um array a partir de seus dígitos multiplicado por 10 :

ex.: 72290379050 => [70, 20, 20, 90, 0, 30, 70, 90, 0, 50, 0]

Caso o CPF tenha dígitos repetidos, então deve-se reduzir esse array somando os valores duplicados:

ex.: [70, 20, 20, 90, 0, 30, 70, 90, 0, 50, 0] => [140, 40, 180, 0, 30, 50]

Por último, é gerado um número aleatório (Magic Number) entre 30 e 990 para cada CPF. Dessa forma, se a soma de dois elementos distintos do array final for igual ao número aleatório, então a aluna(o) ganha permissão de acessar a sala de convivência para usar a cafeteira na semana.

Pode usar lista (Python List)
Não pode usar dicionário (Python dict)
Atenção com o uso excessivo de trechos com O(nˆ2)
Obrigatório usar Tabela Hash

## Input

N - Onde N é o número de operações da entrada

Várias linhas com a seguinte informação:

CPF MN - Calcula autorização considerando um CPF e um (magic number) MN.

Limites de Input

len(CPF) = 11
30 <= MN <= 990

## Output

RESPONSE - Onde pode ser UP Permission se o usuário receber a permissão ou NOT Permission, caso não esteja autorizado na semana.