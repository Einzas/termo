from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Entalpia(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EntalpiaApp(App):
    def build(self):
        return Entalpia()


if __name__ == '__main__':
    EntalpiaApp().run()
