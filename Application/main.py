from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.app import App

from kivy.config import Config
import os
import sys
from src.GUI import Gui  # Cambiado el nombre a algo más descriptivo
from kivy.resources import resource_add_path

# Configuraciones
Config.set('graphics', 'resizable', False)
Window.fullscreen = 0
Window.maximize()


class GUIApp(MDApp, App):
    def build(self):
        self.title = 'Nox_LVTE'
        self.icon = 'img/utelvte.png'
        return Gui()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    GUIApp().run()
