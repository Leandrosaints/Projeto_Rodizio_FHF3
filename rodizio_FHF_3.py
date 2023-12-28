
import random

from colorama import Fore
class Logic():
    def __init__(self):
        ...
    def logic(self):

        pessoas = ['Petrianne', 'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia', 'Lenilza', 'Ana']

        # Lista de funções numeradas
        funcoes = [2, 8, 9, 10, 12, 13, 20]

        # Dicionário para armazenar as funções atribuídas a cada pessoa
        funcoes_pessoas = {}

        # Funções consideradas pesadas
        funcoes_pesadas = [8, 13, 20]

        # Funções predefinidas para cada pessoa
        funcoes_predefinidas = [8, 8, 9, 12, 13, 20, 9, 2]

        # Distribuir funções adicionais para cada pessoa
        for i, pessoa in enumerate(pessoas):
            funcoes_disponiveis = funcoes.copy()
            funcoes_atribuidas = [funcoes_predefinidas[i]]#Recebe as fucoes que ja foram pre-definidas respectivamente

            while len(funcoes_atribuidas) < 4:
                funcao = random.choice(funcoes_disponiveis)



                if (funcao not in funcoes_atribuidas and
                    (len(funcoes_atribuidas) == 1 or funcoes_atribuidas[-1] not in funcoes_pesadas or funcao not in funcoes_pesadas)):


                    if funcao == 8 and funcoes_atribuidas.count(8) >= 2:
                        continue  # Continue se já houver duas ocorrências da função 8

                    #if any(funcoes_pessoas.get(p, []) == [funcao] for p in funcoes_pessoas) and funcao != 8:
                        #continue  # Continue se a função já estiver atribuída a outra pessoa

                    funcoes_atribuidas.append(funcao)

                funcoes_disponiveis.remove(funcao)
            funcoes_pessoas[pessoa] = funcoes_atribuidas


        return funcoes_pessoas.items()

                # Exibir as funções atribuídas a cada pessoa
        #for pessoa, funcoes in funcoes_pessoas.items():
            #return funcoes
            #print(f"{pessoa}:{funcoes[0]}")

