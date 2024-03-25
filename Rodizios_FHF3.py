import asyncio
import json
import os

from kivy.utils import platform
from kivy.metrics import dp
from kivy.uix.popup import Popup

from kivy.uix.screenmanager import SlideTransition

from kivymd.theming import ThemeManager
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField


Builder.load_file('src/style_.kv')

from kivy.properties import ListProperty

from kivy.uix.boxlayout import BoxLayout

from animation_shimmer import ShimmerWidget
# from kivymd.uix.progressloader import MDProgressLoader
from dadosJson import JsonFileManager
from kivy.clock import Clock

"""class ShimmerWidget(Widget):
    def __init__(self, **kwargs):
        super(ShimmerWidget, self).__init__(**kwargs)
        self.duration = 1.5  # Duração total da animação
        self.num_rectangles = 10  # Número de retângulos no shimmer
        self.rectangles = []
        self.create_rectangles()
        self.start_animation()

    def create_rectangles(self):
        for i in range(self.num_rectangles):
            rectangle = Rectangle(size=(self.width / self.num_rectangles, self.height), pos=(self.width * i / self.num_rectangles, 0))
            self.rectangles.append(rectangle)
            self.canvas.add(Color(1, 1, 1, 0))  # Começa com opacidade 0
            self.canvas.add(rectangle)

    def start_animation(self):
        for i, rectangle in enumerate(self.rectangles):
            animation = Animation(pos=(self.width, 0), duration=self.duration) + \
                        Animation(pos=(self.width * (i - 1) / self.num_rectangles, 0), duration=self.duration)
            animation.repeat = True
            animation.start(rectangle)
            Clock.schedule_once(lambda dt, rect=rectangle: self.start_opacity_animation(rect), i * (self.duration / self.num_rectangles))

    def start_opacity_animation(self, rectangle):
        animation = Animation(r=0, g=0, b=0, a=0, duration=self.duration) + \
                    Animation(r=1, g=1, b=1, a=1, duration=self.duration)
        animation.repeat = True
        animation.start(rectangle)

# Define a largura e altura desejadas"""

class  MyMDTextField(MDTextField):
    ...
class Dialog(MDDialog):
    def __init__(self, text, main_app, **kwargs):
        super(Dialog, self).__init__(**kwargs)
        self.text_label = text
        # self.my_list = main_app.my_data
        self.main_app = main_app
        self.size_hint = (None, None)
        self.size = (Window.width * 0.5, Window.height * 0.5)
        self.auto_dismiss = True

        self.text_field = MyMDTextField(hint_text="Digite algo", size_hint=(None, None), height=100, width=400)

        button_layout = BoxLayout(size_hint_y=None, height="40dp", padding=("250dp", "0dp"))
        button = MDFlatButton(text="Enviar")
        close_button = MDIconButton(icon='close', on_release=self.dismiss)

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
            # index_sublista = lista_valores.index(valor_antigo)
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
            # self.main_app.logic_instance.funcoes_pessoas[chave][index_sublista] = novo_valor

            # Chama o método de substituição na classe MyLabel
            # self.main_app.logic_instance.funcoes_pessoas[0][valor_antigo] = novo_valor
            # self.main_app.logic_instance.funcoes_pessoas[0][2] = 9
            # print(self.main_app.logic_instance.funcoes_pessoas)
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
class LabelClick(MDLabel):
    def __init__(self, **kwargs):
        super(LabelClick, self).__init__(**kwargs)
        self.radius = (20, 20, 20, 20)
        self.bind(on_touch_down=self.on_label_click)
    """"    self.bind(on_touch_down=lambda _, touch: self.on_label_clicck(touch) if self.collide_point(*touch.pos) else False)

    def on_label_clicck(self, touch):
        CardScreen.on_touch_move(touch)
        # Supondo que você tenha uma instância do MDLabel chamada label
        self.md_bg_color = (0.4, 0.4, 0.4, 0.1)

        #self.theme_text_color = "Secondary"""""


    def on_label_click(self, instance, touch):
        if self.collide_point(*touch.pos):
            self.on_label_clicked(touch)

    def on_label_clicked(self, touch):
        self.md_bg_color = (0.4, 0.4, 0.4, 0.1)
        self.parent.parent.on_touch_move(touch)

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


    ...
class Scroll(ScrollView):
    ...

    # ... (seu código anterior)


class MyMDCard(MDCard):
    # Exemplo de variável
    def __init__(self, card_number, **kwargs):
        super(MyMDCard, self).__init__(**kwargs)
        self.card_number = card_number
        self.var_width = Window.width
        self.var_height = Window.height
        self.size = (Window.width * 0.9, Window.height * 0.9)


class ShimmerLayout:
    pass


class CardScreen(Screen):

    def __init__(self, main_app, card_number, **kwargs):
        super(CardScreen, self).__init__(name=f'Card_{card_number}', **kwargs)
        self.main_app = main_app
        self.card_number = card_number

        self.json_manager = JsonFileManager()

        # self.json_manager = JsonFileManager('dados.json')

        # Crie uma instância de MDCard
        self.card = MyMDCard(self.card_number)

        # Adicione um ScrollView na vertical
        self.side_scroll = ScrollView(
            size_hint=(None, None),
            size=(Window.width * 0.9, Window.height * 0.9)
        )

        # Adicione o MDGridLayout ao ScrollView
        self.people_functions_layout = MDGridLayout(cols=6, size_hint_y=None, padding=(10))
        self.people_functions_layout.bind(minimum_height=self.people_functions_layout.setter('height'))

        # Adicione o ScrollView ao MDCard
        # self.card.add_widget(self.side_scroll)
        # self.side_scroll.add_widget(self.people_functions_layout)
        # Adicione o MDCard à tela
        # self.add_widget()
        self.shimmer_widget = ShimmerWidget(size=(280, 350))
        #self.add_widget(self.card)
        self.add_widget(self.shimmer_widget)

        asyncio.run(self.load_data_and_display_card())

    def show_error_popup(self, error_details):
        # Crie o conteúdo do pop-up com os detalhes do erro
        popup_content = MDLabel(text=json.dumps(error_details, indent=4))

        # Crie o pop-up
        popup = Popup(title='Erro', content=popup_content, size_hint=(None, None), size=(400, 200))

        # Adicione um botão para fechar o pop-up
        popup_content.bind(on_touch_down=popup.dismiss)

        # Exiba o pop-up
        popup.open()
    async def load_data_and_display_card(self):
        try:


            data = await self.json_manager.get_cached_data_async()
            data_names = await self.json_manager.load_json_async()
            # print(data_names.get('pessoas'))

            for i, nome in enumerate(data_names.get('pessoas')):

                item = MDLabel(text=nome, size_hint=(None, 0.1), size=[200, 1])
                self.people_functions_layout.add_widget(item)
                functions = data.get(str(i))

                if functions:
                    for func in functions:
                        # print(func)
                        function_label = MyLabel(
                            text=str(func),
                            main_app=self.main_app,
                            id='function_label',
                            size_hint=(0.1, 0.1),
                            height="40"
                        )
                        self.people_functions_layout.add_widget(function_label)

                    edit_button = MDIconButton(

                        id='edit_button',
                    )
                    self.people_functions_layout.add_widget(edit_button)

            self.side_scroll.add_widget(self.people_functions_layout)
            self.card.add_widget(self.side_scroll)
            self.add_widget(self.card)
        except Exception as e:
        # Se ocorrer uma exceção, crie um JSON com os detalhes do erro
            error_details = {
                "type": type(e).__name__,
                "message": str(e)
            }
            # Exiba o JSON em um pop-up
            self.show_error_popup(error_details)


    # Restante do código...

    # Restante do código...
    def update_card_number(self, card_number):
        self.card_number = card_number

        # card_screen = self.main_app.screen_manager.get_screen(self.name)
        # card_screen.card_number = card_number
        # card_screen.ids.card_id.card_number = card_number  # Atualiza também usando o ID do MDCard

    def on_touch_move(self, touch):
        print('saindo aqui')

        # Verifica se o movimento é horizontal
        if abs(touch.dx) > abs(touch.dy):

            # Desloca para a esquerda
            app = self.main_app.get_running_app()
            if touch.dx < -20:

                # app = self.main_app.get_running_app()
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
        # self.my_data = MyData()
        ######  Layout  #####
        self.sinal = False
        Main = MDBoxLayout()
        # self.shimmer_widget = ShimmerWidget(size=(280, 350))
        self.Main_secundary = MyBoxLayout()

        self.screen_manager = ScreenManager()
        # self.Main_secundary.add_widget(self.shimmer_widget)
        ##### add hearde_label #####
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"  # Ou "Light" conforme necessário

        header_label = MDLabel(
            text='Rodizio FHF 3',
            theme_text_color='Custom',
            text_color="white",  # Use 'Custom' para personalizar a cor do texto
            halign='right',
            bold=True,
            height=dp(10),
            font_style="H5",  # Estilo da fonte (pode ser "Subtitle1", "Body1", "H1", etc.)
            # font_name="src/fontes/Lato/Lato-LightItalic.ttf",
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
            padding=[0, 0, 20, 0],

        )
        self.search_field = Search(halign="center", pos_hint={"center_x": 0.5, "top": 0.5})

        ######## Cards ########

        # Adiciona três instâncias de telas (cada uma com um card)

        ##### Add os cards a Main secundary e principal######
        Main.add_widget(self.search_field)
        Main.add_widget(header_label)
        Main.add_widget(date_label)

        self.Main_secundary.add_widget(self.screen_manager)
        Main.add_widget(self.Main_secundary)

        # thread = threading.Thread(target=self.delayed_loading)
        # thread.start()
        Clock.schedule_once(lambda dt: self.add_card_screen(), 2)
        # Clock.schedule_once(lambda dt: self.add_secund_card(), 2)
        # thread = threading.Thread(target=self.time).start()
        return Main

    def add_card_screen(self):
        for card_number in range(0, 1):
            screen = CardScreen(self, card_number=card_number)
            self.screen_manager.add_widget(screen)

    def on_start(self):

       ...



    '''def add_secund_card(self):
        screen = CardScreen(self, card_number=1)
        self.screen_manager.add_widget(screen)'''

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
