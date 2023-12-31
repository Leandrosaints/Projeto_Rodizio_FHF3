import cProfile

from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from rodizio_FHF_3 import Logic
Builder.load_file('src/style_.kv')

from kivy.properties import ListProperty

class MyData(BoxLayout):
    people_list = ListProperty(['Petrianne', 'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia',
               'Lenilza', 'Ana'])

class Dialog(MDDialog):
    def __init__(self, text, main_app, **kwargs):
        super(Dialog, self).__init__(**kwargs)
        self.text_input = text
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
        for i, nome in enumerate(self.my_list.people_list):
            if self.text_input == nome:
                index =self.my_list.people_list.index(self.text_input)
                self.my_list.people_list.remove(self.text_input)
                self.my_list.people_list.insert(index, self.text_field.text)
                self.main_app.update_people_functions_layout()

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
    adaptive_width = True

class Scroll(ScrollView):
    adaptive_width = True

class MainApp(MDApp):
    def build(self):
        sideScroll = Scroll()
        Main = MDBoxLayout()
        self.my_data = MyData()
        self.logic_instance = Logic()
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

        #self.functions_list = ['2', '8', '9', '10']
        #todas_funcoes = self.logic_instance.todas_funcoes
        self.people_functions_layout = MDGridLayout(cols=6)#len(self.logic_instance.funcoes) -2)
        for i, nome in enumerate(self.my_data.people_list):


            item = MyLabel(
                main_app=self,
                text=nome,
                size_hint=(None, 0.1),
                size=[110, 1],

            )
            self.people_functions_layout.add_widget(item)

            for func in self.logic_instance.funcoes_pessoas[nome]:
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
        sideScroll.add_widget(self.people_functions_layout)
        Main_secundary.add_widget(sideScroll)
        Main.add_widget(Main_secundary)

        return Main


    def update_people_functions_layout(self):
        Clock.schedule_once(lambda dt: self._update_people_functions_layout(), 0)


    def _update_people_functions_layout(self):

        self.people_functions_layout.clear_widgets()

        for i, nome in enumerate(self.my_data.people_list):
            item = MyLabel(
                text=nome,
                main_app=self,
                size_hint=(None, 0.1),
                size=[110, 1]
            )
            self.people_functions_layout.add_widget(item)

            for func in self.functions_list:
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






if __name__ == '__main__':
    app = MainApp()
    app.run()

