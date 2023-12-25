import random
pessoas = ['Petrianne','M.Eduarda', 'Shirlene','Marilene','Alberta','Patricia', 'Lenilza', 'Ana']
import random

# Lista de pessoas
#pessoas = ["Pessoa1", "Pessoa2", "Pessoa3", "Pessoa4", "Pessoa5", "Pessoa6", "Pessoa7", "Pessoa8"]

# Lista de funções numeradas
funcoes = [2, 8, 9, 12, 13, 20]

# Dicionário para armazenar as funções atribuídas a cada pessoa
funcoes_pessoas = {}

# Funções consideradas pesadas
funcoes_pesadas = [8, 13, 20]

# Funções predefinidas para cada pessoa
funcoes_predefinidas = [8, 8, 9, 12, 13, 20, 9, 2]

# Distribuir funções adicionais para cada pessoa
for i, pessoa in enumerate(pessoas):
    funcoes_disponiveis = funcoes.copy()
    funcoes_atribuidas = [funcoes_predefinidas[i]]
    while len(funcoes_atribuidas) < 4:
        funcao = random.choice(funcoes_disponiveis)
        if (funcao not in funcoes_atribuidas and
            (len(funcoes_atribuidas) == 1 or funcoes_atribuidas[-1] not in funcoes_pesadas or funcao not in funcoes_pesadas)):
            funcoes_atribuidas.append(funcao)
        funcoes_disponiveis.remove(funcao)
    funcoes_pessoas[pessoa] = funcoes_atribuidas

# Exibir as funções atribuídas a cada pessoa
for pessoa, funcoes in funcoes_pessoas.items():
    print(f"{pessoa}: {funcoes}")
