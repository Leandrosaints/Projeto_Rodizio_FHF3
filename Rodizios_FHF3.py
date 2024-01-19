import cProfile

from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.screenmanager import SlideTransition
from kivymd.theming import ThemeManager
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager

from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from rodizio_FHF_3 import Logic
Builder.load_file('src/style_.kv')

from kivy.properties import ListProperty, DictProperty


class MyData(BoxLayout):
    people_list = ListProperty(['Petrianne', 'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia',
               'Lenilza', 'Ana'])
    funcoes = ListProperty([2, 8, 9, 12, 13, 20])

class Dialog(MDDialog):
    def __init__(self, text, main_app, **kwargs):
        super(Dialog, self).__init__(**kwargs)
        self.text_label = text
        self.my_list = main_app.my_data
        self.main_app = main_app
        self.size_hint = (None, None)
        self.size = (300, 100)
        self.auto_dismiss = False

        self.text_field = MDTextField(hint_text="Digite algo")

        button_layout = BoxLayout(size_hint_y=None, height="40dp", padding=("250dp", "0dp"))
        button = MDFlatButton(text="Enviar")
        close_button = MDIconButton(icon='close-circle', on_release=self.dismiss)

        button_layout.add_widget(button)
        button_layout.add_widget(close_button)

        button.bind(on_release=self.on_send_button_click)

        self.add_widget(self.text_field)
        self.add_widget(button_layout)

    def on_send_button_click(self, instance):
        self.get_text()
        self.dismiss()

    def get_text(self):
        if self.text_label.isdigit():

            valor_antigo = int(self.text_label)
            novo_valor = int(self.text_field.text)
            #index_sublista = lista_valores.index(valor_antigo)
            # Obtém a chave associada ao valor antigo na lista de funções
            chave_associada = None
            for chave, lista_valores in self.main_app.logic_instance.funcoes_pessoas.items():
                if valor_antigo in lista_valores:
                    chave_associada = chave
                    break

            # Se encontrarmos a chave associada, substituímos o valor apenas nessa chave
            if chave_associada is not None:
                index_sublista = self.main_app.logic_instance.funcoes_pessoas[chave_associada].index(
                    valor_antigo)
                self.main_app.logic_instance.funcoes_pessoas[chave_associada][index_sublista] = novo_valor
                self.main_app.update_people_functions_layout(chave)

            # Substitui o valor na sub-lista
            #self.main_app.logic_instance.funcoes_pessoas[chave][index_sublista] = novo_valor


            # Chama o método de substituição na classe MyLabel
            #self.main_app.logic_instance.funcoes_pessoas[0][valor_antigo] = novo_valor
            # self.main_app.logic_instance.funcoes_pessoas[0][2] = 9
            #print(self.main_app.logic_instance.funcoes_pessoas)
        try:


            for i, nome in enumerate(self.my_list.people_list):
                self.index_ = i

                try:
                    if self.text_label == nome:
                        index = self.my_list.people_list.index(self.text_label)
                        self.my_list.people_list.remove(self.text_label)
                        self.my_list.people_list.insert(index, self.text_field.text)
                        self.main_app.update_people_functions_layout()
                except:
                    pass

                try:
                    ...
                    # Verifica se o texto de entrada é um número
                    """if self.text_label.isdigit():

                        valor_antigo = int(self.text_label)
                        novo_valor = int(self.text_field.text)

                        # Chama o método de substituição na classe MyLabel
                        #self.main_app.logic_instance.funcoes_pessoas[0][valor_antigo]=novo_valor
                        print(self.main_app.logic_instance.funcoes_pessoas[0]"""
                except:
                    pass

        except:
            ...

class MyLabel(MDLabel):
    def __init__(self, main_app, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.caixa = Dialog(self.text, main_app)

        self.bind(on_touch_down=lambda _, touch: self.on_label_click() if self.collide_point(*touch.pos) else False)

    def on_label_click(self):
        self.theme_text_color = "Secondary"
        self.caixa.open()

class Search(MDTextField):
    pass

class MyBoxLayout(MDBoxLayout):
   ...

class Scroll(ScrollView):
    ...

    # ... (seu código anterior)




class MyMDCard(MDCard):

    def __init__(self, card_number, **kwargs):
        super(MyMDCard, self).__init__(**kwargs)
        self.card_number = card_number
class CardScreen(Screen):

    def __init__(self, main_app, card_number, **kwargs):
        super(CardScreen, self).__init__(name=f'Card_{card_number}', **kwargs)
        self.main_app = main_app
        self.card_number = card_number
        """with self.canvas.before:
            Color(1, 0, 0, 1)  # Cor da sombra (vermelho puro para demonstração)
            self.shadow_rectangle = Rectangle(pos=self.pos, size=self.size)"""

        # Crie uma instância de MDCard
        self.card = MyMDCard(self.card_number)


        # Adicione um ScrollView na vertical
        side_scroll = ScrollView(
            size_hint=(None, None),
            size=(300, 350),
        )

        # Adicione o MDGridLayout ao ScrollView
        self.people_functions_layout = MDGridLayout(cols=6, size_hint_y=None)
        self.people_functions_layout.bind(minimum_height=self.people_functions_layout.setter('height'))

        for i, nome in enumerate(main_app.my_data.people_list):
            item = MyLabel(
                main_app=main_app,
                text=nome,
                size_hint=(None, 0.1),
                size=[100, 1],
            )
            self.people_functions_layout.add_widget(item)

            for func in main_app.logic_instance.funcoes_pessoas[i]:
                function_label = MyLabel(
                    text=str(func),
                    main_app=main_app,
                    id='function_label',
                    size_hint=(0.1, 0.1),
                    height="40"
                )
                self.people_functions_layout.add_widget(function_label)

            edit_button = MDIconButton(
                icon="pencil",
                id='edit_button',
            )
            self.people_functions_layout.add_widget(edit_button)

        # Adicione o MDGridLayout ao ScrollView
        side_scroll.add_widget(self.people_functions_layout)

        # Adicione o ScrollView ao MDCard
        self.card.add_widget(side_scroll)

        # Adicione o MDCard à tela
        self.add_widget(self.card)

    # Restante do código...

# Restante do código...
    def update_card_number(self, card_number):
        self.card_number = card_number
        print(self.card_number)

        #card_screen = self.main_app.screen_manager.get_screen(self.name)
        #card_screen.card_number = card_number
        #card_screen.ids.card_id.card_number = card_number  # Atualiza também usando o ID do MDCard
    def on_touch_move(self, touch):
        # Verifica se o movimento é horizontal
        if abs(touch.dx) > abs(touch.dy):
            # Desloca para a esquerda
            app = self.main_app.get_running_app()
            if touch.dx < -20:
                #app = self.main_app.get_running_app()
                screen_manager = app.screen_manager
                next_card_number = int(self.name.split('_')[1]) + 1
                next_card_name = f'Card_{next_card_number}'

                if screen_manager.has_screen(next_card_name):
                    screen_manager.current = next_card_name
                    self.update_card_number(next_card_number)


                    return True
            # Desloca para a direita (pode adicionar lógica semelhante para deslocar para a tela anterior)
            elif touch.dx > 20:
                prev_card_number = int(self.name.split('_')[1]) - 1
                prev_card_name = f'Card_{prev_card_number}'
                if prev_card_number >= 1 and app.screen_manager.has_screen(prev_card_name):
                    # Change the transition to SlideTransition
                    app.screen_manager.transition = SlideTransition(direction='right')
                    app.screen_manager.current = prev_card_name
                    self.update_card_number(prev_card_number)
                    return True

                # Reset the transition to the default
            app.screen_manager.transition = SlideTransition(direction='left')
            return super(CardScreen, self).on_touch_move(touch)

class MainApp(MDApp):
    def build(self):
        self.my_data = MyData()
        ######  Layout  #####
        Main = MDBoxLayout()


        self.logic_instance = Logic()
        self.Main_secundary = MyBoxLayout()
        self.screen_manager = ScreenManager()

        ##### add hearde_label #####
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"  # Ou "Light" conforme necessário

        header_label = MDLabel(
            text='Rodizio FHF 3',
            theme_text_color='Custom',
            text_color="white",# Use 'Custom' para personalizar a cor do texto
            halign='right',
            bold=True,
            height=dp(10),
            font_style= "H5",  # Estilo da fonte (pode ser "Subtitle1", "Body1", "H1", etc.)
            font_name="src/fontes/Lato/Lato-LightItalic.ttf",
            size_hint=(1, None),
            padding=[0, 0, 20, 0],


        )
        date_label = MDLabel(
            text='seg - 14/01/2024',
            theme_text_color='Custom',
            text_color="white",
            size_hint=(1, None),
            halign='right',
            height=dp(3),
            padding=[0,0,20,0],


        )
        self.search_field = Search(halign="center", pos_hint={"center_x": 0.4, "top":0.5})

        ######## Cards ########


        # Adiciona três instâncias de telas (cada uma com um card)
        for card_number in range(1, 4):
            screen = CardScreen(self, card_number=card_number)
            self.screen_manager.add_widget(screen)


        ##### Add os cards a Main secundary e principal######
        Main.add_widget(self.search_field)
        Main.add_widget(header_label)
        Main.add_widget(date_label)

        self.Main_secundary.add_widget(self.screen_manager)
        Main.add_widget(self.Main_secundary)

        return Main

    """def update_people_functions_layout(self,  chave=None):
        Clock.schedule_once(lambda dt: self._update_people_functions_layout(chave), 0)


    def _update_people_functions_layout(self, chave=None):

        self.people_functions_layout.clear_widgets()

        for i, nome in enumerate(self.my_data.people_list):
            item = MyLabel(
                text=nome,
                main_app=self,
                size_hint=(None, 0.1),
                size=[110, 1]
            )
            self.people_functions_layout.add_widget(item)
            if chave is None:
                for func in self.logic_instance.funcoes_pessoas[i]:
                    function_label = MyLabel(
                        text=str(func),
                        main_app=self,
                        id='function_label',
                        size_hint=(0.1, 0.1),
                        height="40"
                    )
                    self.people_functions_layout.add_widget(function_label)

                edit_button = MDIconButton(
                    icon="pencil",
                    id='edit_button',
                )

                self.people_functions_layout.add_widget(edit_button)
"""


if __name__ == '__main__':
    app = MainApp()
    app.run()

