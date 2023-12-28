from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.recycleview import RecycleView
from rodizio_FHF_3 import Logic
Builder.load_file('src/style_.kv')

class MyBoxLayout(BoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        Main = BoxLayout()  # principal
        logica = Logic()
        header_label = MDLabel( text='Rodizio FHF 3',
                                id='header_label',
                                halign='center',
                                size_hint=(1, None),  # Define o tamanho da label
                                height='2',  # Define a altura da label
                                padding=[0, 0, 0, 100])#text='Rodizio FHF 3 ', id='header_label', halign='center', size_hint=(0.1,0.5))
        Main.add_widget(header_label  )

        Main_secundary = MyBoxLayout()
        Main.add_widget(Main_secundary)

        # Cabeçalho


        # Lista de pessoas e funções
        people_list = ['Petrianne', 'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia', 'Lenilza', 'Ana']

        functions_list = ['2',' 8',' 9', '10']

        # Layout para pessoas e funções
        people_functions_layout = GridLayout(cols=len(functions_list) + 2, )

        # Adiciona os rótulos das pessoas
        for i, nome in enumerate(people_list):



            person_label = MDLabel(text=nome, id=f'person_label')
            people_functions_layout.add_widget(person_label)

            # Adiciona os rótulos das funções numeradas
            for func in functions_list:

                function_label = MDLabel(text=str(func), id='function_label')
                people_functions_layout.add_widget(function_label)
                # Adiciona o botão de edição para cada função


            # Adiciona o botão de edição para a última função
            edit_button = MDIconButton(icon="pencil", id='edit_button', pos_hint={"center_x": .1, "center_y":.1}, icon_size="16sp")
            people_functions_layout.add_widget(edit_button)


        Main_secundary.add_widget(people_functions_layout)

        return Main


if __name__ == '__main__':
    app = MainApp()
    app.run()