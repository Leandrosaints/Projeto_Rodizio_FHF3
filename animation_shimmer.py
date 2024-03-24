<<<<<<< HEAD
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation

=======
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.clock import Clock
>>>>>>> 8575bc846aed3ac2fec4e9f460af200822f69b45

Builder.load_string('''
<ShimmerWidget>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            #size: self.size
            pos:self.pos[0] + 15, self.pos[1] + 50
            #pos: self.pos
            #source: 'brf.png'  # Um pixel branco como textura para criar o shimmer
''')

class ShimmerWidget(Widget):
    def __init__(self, size,  **kwargs):
        super(ShimmerWidget, self).__init__(**kwargs)
        self.duration = 0.5  # Duração de cada piscada
        self.opacity_change = 0.5  # Mudança na opacidade para cada piscada
        self.max_opacity = 2  # Opacidade máxima
        self.min_opacity = 0.2  # Opacidade mínima
        self.animation = None
        self.start_animation()
        #Clock.schedule_once(lambda dt: self.start_animation, 1)
        #self.pos = pos
        self.size = size#=(280, 350)



    def start_animation(self):
        self.animation = Animation(opacity=self.min_opacity, duration=self.duration / 2) + \
                         Animation(opacity=self.max_opacity, duration=self.duration / 2)
        self.animation.repeat = True
        self.animation.start(self)

#class ShimmerApp(App):
    #def build(self):
        #return ShimmerWidget()

#if __name__ == '__main__':
    #ShimmerApp().run()
