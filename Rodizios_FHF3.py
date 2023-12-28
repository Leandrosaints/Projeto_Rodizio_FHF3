from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.list import MDList, OneLineListItem,TwoLineListItem, BaseListItem

from rodizio_FHF_3 import Logic
Builder.load_file('src/style_.kv')

class MyListItem(OneLineListItem):
    def __init__(self, **kwargs):
        super(MyListItem, self).__init__(**kwargs)
        self.size_hint = (None, 0.1)
        self.size = [110, 1]
        self.theme_text_color = "Custom"
        self.text_color = get_color_from_hex("#111111")
        #self.text_active_color = get_color_from_hex("#FFD700")
        #self.divider = True
        #self.divider_color =  get_color_from_hex("#FF0000")
        #self.icon = "star"
        #self.icon_color = (1, 1, 1, 1)



class MyLabel(MDLabel):

    id = StringProperty()
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

            item = MyListItem(text=nome,
                                   size_hint=(None, 0.1),
                                   size=[110, 1],
                                   _txt_bot_pad=-50,
                                    divider_color=(1, 1, 1, 1))





                                    # Define o alinhamento do texto como à direita
                                    #item.theme_text_color = "Custom"
            #item.text_color = (1, 0, 0, 1)
            #item.theme_text_active_color = "Custom"
            #item.text_active_color = (0, 1, 0, 1)
            #item.divider = True  # Exibe uma linha divisória abaixo do item
            #item.divider_color = (0, 0, 1, 1)  # Define a cor da linha divisória como azul
            #item.icon = "star"  # Define o ícone "star" no início do item
            #item.icon_color = (1, 1, 0, 1)  # Define a cor do ícone como amarelo
            #item.on_press = self.item_pressed  # Define a função a ser executada quando o item é pressionado
            #item.on_release = self.item_clicked  # Define a função a ser executada quando o item é liberado
            # Adiciona os itens à lista



            person_label = MDLabel(text=nome,
                                   id='person_label',
                                   size_hint=(None, 0.1),

                                  )
            people_functions_layout.add_widget(item)

            # Adiciona os rótulos das funções numeradas
            for func in functions_list:

                function_label = MyLabel(text=str(func),
                                        id = 'function_label',
                                        size_hint=(0.1, 0.1),
                                        height = "40",


                                         )
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