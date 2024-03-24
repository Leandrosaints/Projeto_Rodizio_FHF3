from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Loading_animation(BoxLayout):
    size_hint = None
    size = (200, 100)  # Tamanho padrão
    pos = (0, 0)  # Posição padrão

    def __init__(self, **kwargs):
        super(Loading_animation, self).__init__(**kwargs)
        self.create_shimmer_animation()

    def create_shimmer_animation(self):
        anim_duration = 1.0  # Duração da animação em segundos
        anim_label1 = Animation(
            opacity=0,
            duration=anim_duration/2
        ) + Animation(
            opacity=1,
            duration=anim_duration/2
        )
        anim_label2 = Animation(
            opacity=0,
            duration=anim_duration/2,
            delay=anim_duration/2  # Delay para a segunda animação
        ) + Animation(
            opacity=1,
            duration=anim_duration/2
        )
        anim_label1.repeat = True
        anim_label2.repeat = True
        anim_label1.start(self.ids.label1)
        anim_label2.start(self.ids.label2)
