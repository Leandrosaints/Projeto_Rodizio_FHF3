
from kivy.properties import StringProperty
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import GridLayout

from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout

from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.list import  BaseListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField

from rodizio_FHF_3 import Logic
Builder.load_file('src/style_.kv')
people_list = ['Petrianne', 'M.Eduarda', 'M.Eduarda', 'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia',
               'Lenilza', 'Ana']

class MyListItem(BaseListItem):
    def __init__(self, **kwargs):
        super(MyListItem, self).__init__(**kwargs)
        self.size_hint = (None, 0.1)
        self.adaptive_width = True
        self.size = [110, 1]
        self.theme_text_color = "Custom"
        self.text_color = get_color_from_hex("#111111")
        self.bg_color =  get_color_from_hex("#FFD700")


class Dialog(MDDialog):
    def __init__(self, **kwargs):
        super(Dialog, self).__init__(**kwargs)
        self.text_input = None
        #self.title = "Custom Dialog"
        self.size_hint = (None, None)
        self.size = (300, 100)
        self.auto_dismiss = False

        # Cria explicitamente o BoxLayout para o conteúdo do diálogo
        #self.content_cls = BoxLayout(orientation="vertical")


        # Adiciona um rótulo ao conteúdo do diálogo
        #self.content_cls.add_widget(MDLabel(text="This is a custom dialog."))

        # Adiciona o campo de texto ao conteúdo do diálogo
        self.text_field = MDTextField(hint_text="Digite algo")


        #self.content_cls.add_widget(self.text_field)
        #buttons = MDIconButton(on_release=self.dismiss,  )
        button_layout = BoxLayout(size_hint_y=None, height="40dp", padding=("250dp", "0dp"),
                                 )
        close_button = MDIconButton(icon='close-circle', on_release=self.dismiss)

        # Adiciona o botão "Fechar" ao layout do botão
        button_layout.add_widget(close_button)

        # Adiciona o layout do botão ao conteúdo do diálogo

        self.add_widget(self.text_field)
        self.add_widget(button_layout)



    def show_dialog(self):
        self.open()
    def on_close_dialog(self, dialog):
        dialog.dismiss()

    def get_text(self):
        if self.text:
            return self.text


class MyLabel(MDLabel):

    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        caixa = Dialog()
        self.bind(on_touch_down=lambda _, touch: caixa.show_dialog() if self.collide_point(*touch.pos) else False)

        #self.adaptive_width = True
    def on_label_click(self):
        self.theme_text_color = "Secondary"
        #caixa = Dialog()
        #caixa.show_dialog()

        for nome in people_list:


            if self.text == nome:

                index = nome.index(self.text)
                people_list.remove(self.text)
                #people_list.insert(index, caixa.get_text())
               # Chama o método refresh_list() do aplicativo
                print(nome)
        #self.text = caixa.get_text()




        # Atribua a função ao evento de clique do MDLabel

    #self.bind(on_touch_down=lambda _, touch: self.on_label_click() if self.collide_point(*touch.pos) else False)
    id = StringProperty()
class Search(MDTextField):
    pass
class MyBoxLayout(MDBoxLayout):
    adaptive_width = True
    '''def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        # Criação do widget MDTextField
        self.search_field = MDTextField(
            hint_text="Pesquisar",
            on_text_validate=self.on_search,
            size_hint=(1, None),
            height="48dp")

    def on_search(self, instance):
        search_text = instance.text
        # Lógica para filtrar a lista de pessoas com base no texto de pesquisa
        filtered_list = [person for person in people_list if search_text.lower() in person.lower()]
        self.refresh_list(filtered_list)'''
class Scroll(ScrollView):
    adaptive_width = True

class MainApp(MDApp):

    def build(self):
        #DEVICE_TYPE = 'mobile'
        sideScroll = Scroll()
        Main = MDBoxLayout()

        #self.adaptive_width = True

        header_label = MDLabel(
            text='Rodizio FHF 3',
            id='header_label',
            halign='center',
            size_hint=(1, None),
            height='2',
            padding=[0, 0, 0, 0]
        )
        self.search_field = Search(halign="center", pos_hint={"center_x": 0.5, "center_y": 0.5})

        Main.add_widget(header_label)
        Main.add_widget(self.search_field)

        Main_secundary = MyBoxLayout()

        #people_list = ['Petrianne', 'M.Eduarda',  'M.Eduarda',  'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia', 'Lenilza', 'Ana']
        functions_list = ['2', '8', '9', '10']

        people_functions_layout = GridLayout(cols=len(functions_list) + 2)

        for i, nome in enumerate(people_list):
            item = MyLabel(
                text=nome,
                size_hint=(None, 0.1),
                size=[110, 1],



            )
            people_functions_layout.add_widget(item)

            for func in functions_list:
                function_label = MyLabel(
                    text=str(func),
                    id='function_label',
                    size_hint=(0.1, 0.1),
                    height="40"
                )
                people_functions_layout.add_widget(function_label)

            edit_button = MDIconButton(
                icon="pencil",
                id='edit_button',)
                #pos_hintcenter_x": .1, "center_y": .1                icon_size="16sp"

            people_functions_layout.add_widget(edit_button)

        sideScroll.add_widget(people_functions_layout)
        Main_secundary.add_widget(sideScroll)
        Main.add_widget(Main_secundary)

        return Main



if __name__ == '__main__':
    app = MainApp()
    app.run()