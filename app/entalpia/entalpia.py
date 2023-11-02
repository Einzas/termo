from typing import Any
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime, timedelta
from kivy.clock import Clock
from kivy.config import Config
from plyer import notification
import plyer
import os
import sys
from GDV import GdV
from CQE import CQEPopup
from PDC import PdC
from kivy.resources import resource_add_path, resource_find
Window.fullscreen = 0
Window.maximize()


class Entalpia(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ahora = datetime.now()
        self.ids.fecha.text = self.ahora.strftime("%d/%m/%Y")
        Clock.schedule_interval(self.actualizar_hora, 1)

    def actualizar_hora(self, *args):
        self.ahora = self.ahora + timedelta(seconds=1)
        self.ids.hora.text = self.ahora.strftime("%H:%M:%S")

    def mostrar_cqe(self):
        self.cqe_popup = CQEPopup()
        self.cqe_popup.open()

    def mostrar_GdV(self):
        self.gdv_popup = GdV()
        self.gdv_popup.open()

    def mostrar_PdC(self):
        self.pdc_popup = PdC()
        self.pdc_popup.open()

    def defaultSpinner(self):
        self.ids.spinner_id.text = "Datos"

    def menuSeleccionado(self, value):
        if value == "CQE":
            self.mostrar_cqe()
            self.defaultSpinner()
        if value == "Generador de Vapor":
            self.mostrar_GdV()
            self.defaultSpinner()
        if value == "Porcentaje de Carga":
            self.mostrar_PdC()
            self.defaultSpinner()


class EntalpiaApp(MDApp, App):

    def build(self):

        Config.set('graphics', 'resizable', False)

        self.title = 'Nox_LVTE'
        self.icon = 'img/utelvte.png'

        return Entalpia()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    EntalpiaApp().run()
