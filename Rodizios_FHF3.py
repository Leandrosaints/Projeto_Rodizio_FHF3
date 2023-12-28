from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.list import MDList, OneLineListItem,TwoLineListItem, BaseListItem
from kivy.uix.scrollview import ScrollView
from rodizio_FHF_3 import Logic
Builder.load_file('src/style_.kv')

class MyListItem(BaseListItem):
    def __init__(self, **kwargs):
        super(MyListItem, self).__init__(**kwargs)
        self.size_hint = (None, 0.1)
        self.size = [110, 1]
        self.theme_text_color = "Custom"
        self.text_color = get_color_from_hex("#111111")
        self.bg_color =  get_color_from_hex("#FFD700")



class MyLabel(MDLabel):

    id = StringProperty()
class MyBoxLayout(BoxLayout):
    pass

class Scroll(ScrollView):
    pass

class MainApp(MDApp):
    def build(self):
        sideScroll = Scroll()
        Main = BoxLayout()

        header_label = MDLabel(
            text='Rodizio FHF 3',
            id='header_label',
            halign='center',
            size_hint=(1, None),
            height='2',
            padding=[0, 0, 0, 100]
        )

        Main.add_widget(header_label)
        Main_secundary = MyBoxLayout()

        people_list = ['Petrianne', 'M.Eduarda',  'M.Eduarda',  'M.Eduarda', 'Shirlene', 'Marilene', 'Alberta', 'Patricia', 'Lenilza', 'Ana']
        functions_list = ['2', '8', '9', '10']

        people_functions_layout = GridLayout(cols=len(functions_list) + 2)

        for i, nome in enumerate(people_list):
            item = MyListItem(
                text=nome,
                size_hint=(None, 0.1),
                size=[110, 1],
                _txt_bot_pad=-50,
                divider_color=(1, 1, 1, 1),
                bg_color=get_color_from_hex('#f0f0f0')
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