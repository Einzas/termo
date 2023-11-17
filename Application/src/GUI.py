from datetime import datetime, timedelta
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tooltip import MDTooltip
from kivy.clock import Clock
from src.GDV import GdV
from src.CQE import CQEPopup
from src.PDC import PdC
from src.Gases import Gases


class Gui(BoxLayout, MDTooltip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ahora = datetime.now()
        self.ids.fecha.text = self.ahora.strftime("%d/%m/%Y")
        Clock.schedule_interval(self.actualizar_hora, 1)

    def actualizar_hora(self, *args):
        self.ahora += timedelta(seconds=1)
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

    def mostrar_Gases(self):
        self.gases_popup = Gases()
        self.gases_popup.open()

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
        if value == "Gases":
            self.defaultSpinner()
            self.mostrar_Gases()
