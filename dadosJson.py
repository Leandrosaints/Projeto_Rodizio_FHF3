import asyncio
import json
import os
from cachetools import TTLCache
from cachetools.keys import hashkey
from rodizio_FHF_3 import Logic
from kivy.utils import platform
from pathlib import Path
import os.path
import os
from kivymd.app import MDApp
from appdirs import user_data_dir






class JsonFileManager:
    def __init__(self, maxsize=100, ttl=3600):
        self.file_path = 'dados.json'
        self.cache = TTLCache(maxsize=maxsize, ttl=ttl)
        self.data = Logic()

        self.request_permissions(None)
    def request_permissions(self, instance):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            permissions = [Permission.WRITE_EXTERNAL_STORAGE]

            def callback(permissions, results):

                if all([res for res in results]):
                    ...
                    #self.create_and_write_file()

            request_permissions(permissions, callback=callback)

    def create_and_write_file(self):
        dir_path = os.path.join(os.environ['EXTERNAL_STORAGE'], 'MyAppFolder')
        os.makedirs(dir_path, exist_ok=True)

        self.file_path = os.path.join(dir_path, self.file_path)
    async def load_json_async(self):
        # Simule uma operação assíncrona de carregamento de dados do arquivo JSON
        # initial_data = self.data.funcoes_pessoas
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, file.read)
                return json.loads(data)
        else:
            # print(f'O arquivo "{self.file_path}" não existe.')
            # print("criando arquivo com dados")
            self.create_file(initial_data={**self.data.funcoes_pessoas, "pessoas": self.data.pessoas})

            with open(self.file_path, 'r') as file:
                dados = json.load(file)
                return dados

    def save_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
        # print(f'Dados salvos no arquivo "{self.file_path}".')
        # Atualiza o cache
        self.cache[hashkey(self.file_path)] = data

    def create_file(self, initial_data=None):
        if not os.path.exists(self.file_path):
            if initial_data is None:
                initial_data = {}
            with open(self.file_path, 'w') as file:
                json.dump(initial_data, file, indent=4)
            # print(f'Arquivo "{self.file_path}" criado com sucesso.')
            # Atualiza o cache com os dados iniciais
            self.cache[hashkey(self.file_path)] = initial_data
        else:
            ...
            # print(f'O arquivo "{self.file_path}" já existe.')

    async def get_cached_data_async(self):
        cached_data = self.cache.get(hashkey(self.file_path))
        if cached_data is None:
            # print("Os dados não estão em cache. Carregando...")
            cached_data = await self.load_json_async()

            self.cache[hashkey(self.file_path)] = cached_data
            return cached_data
        else:
            return None

    async def load_names_async(self):
        cached_data = await self.load_json_async()

        return cached_data.get('pessoas')
        # print(cached_data.get('pessoas'))
        # data.get['pessoas']
        '''if cached_data is not None and 'pessoas' in cached_data:
            for item in cached_data.get('pessoas'):
               item
        else:
            print("Não foi possível carregar os nomes. Dados não encontrados")'''


# Acessa os dados em cache
"""data = file_manager.get_cached_data()

if data is None:
    # Se os dados não estiverem em cache, cria o arquivo e carrega os dados
    initial_data = ['exemplo1', 'exemplo2', 'exemplo3']  # Exemplo de lista inicial
    file_manager.create_file(initial_data)
    data = file_manager.get_cached_data()

# Realiza operações com os dados (por exemplo, adiciona ou modifica dados)
# Supondo que 'data' seja uma lista
data.append('novo_exemplo')

# Salva os dados de volta no arquivo
file_manager.save_json(data)
"""
