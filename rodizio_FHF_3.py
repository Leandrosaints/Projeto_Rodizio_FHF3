import json
import random

from colorama import Fore
class Logic():
    def __init__(self):
        #self.todas_funcoes = []
        self.logic()
    def logic(self):

        self.pessoas = ['Petrianne','leandro','lucas','maria','isac','higor', 'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia', 'Lenilza', 'Ana']

        # Lista de funções numeradas
        self.funcoes = [2, 8, 9, 12, 13, 20]

        # Dicionário para armazenar as funções atribuídas a cada pessoa
        self.funcoes_pessoas = {}

        # Funções consideradas pesadas
        funcoes_pesadas = [8, 13, 20]

        # Funções predefinidas para cada pessoa
        funcoes_predefinidas = [8, 8, 9, 12, 13, 20, 9, 2, 1, 2, 3, 4, 5]

        # Distribuir funções adicionais para cada pessoa
        for i, pessoa in enumerate(self.pessoas):
            funcoes_disponiveis = self.funcoes.copy()
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
            self.funcoes_pessoas[i] = funcoes_atribuidas


"""with open('dadoss.json', 'w') as json_file:
    json.dump(self.funcoes_pessoas, json_file)"""


            #return funcoes_pessoas[pessoa]

        #return funcoes_pessoas.items()
                # Exibir as funções atribuídas a cada pessoa
        #for pessoa, funcoes in funcoes_pessoas.items():
            #self.todas_funcoes.append(funcoes)

            #print(f"{pessoa}:{funcoes}")


