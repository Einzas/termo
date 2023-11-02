from kivy.uix.popup import Popup
import Database as Database
from kivymd.toast import toast

db = Database.Database()


class CQEPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            porcentaje = db.info("CQE", "PORCENTAJE",
                                 "CODIGO like 'CQE_0%' Order by codigo")
            # Se llenan los campos de la ventana
            self.ids.C.text = str(porcentaje[0]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.H.text = str(porcentaje[1]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.S.text = str(porcentaje[2]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.O.text = str(porcentaje[3]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.N.text = str(porcentaje[4]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.W.text = str(porcentaje[5]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.A.text = str(porcentaje[6]).strip(
                "[]").strip("()").strip("''").strip(",")

            # Se suma el porcentaje de CQE
            suma = float(str(porcentaje[0]).strip('()').strip(",")) + float(str(porcentaje[1]).strip('()').strip(",")) + float(str(porcentaje[2]).strip('()').strip(",")) + float(
                str(porcentaje[3]).strip('()').strip(",")) + float(str(porcentaje[4]).strip('()').strip(",")) + float(str(porcentaje[5]).strip('()').strip(",")) + float(str(porcentaje[6]).strip('()').strip(","))

            if suma >= 99.99:
                suma = 100
            # Se asignal el valor al campo total
            self.ids.Total.text = str(suma) + "%"

            # Se cargan los datos de la base de datos

            valores = db.info(
                "CQE", "PORCENTAJE", "CODIGO like 'CQEC_0%' Order by codigo")
            self.ids.TMFO.text = str(valores[0]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.FVAGF.text = str(valores[1]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.PCC.text = str(valores[2]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.PCIC.text = str(valores[3]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.TFO.text = str(valores[4]).strip(
                "[]").strip("()").strip("''").strip(",")
            self.ids.CEFO.text = str(valores[5]).strip(
                "[]").strip("()").strip("''").strip(",")

        except Exception as e:
            print("Error de conexion a la base de datos:")
            print(e)

    def guardar(self):

        # Se obtienen los valores de los campos
        C = self.ids.C.text
        H = self.ids.H.text
        S = self.ids.S.text
        O = self.ids.O.text
        N = self.ids.N.text
        W = self.ids.W.text
        A = self.ids.A.text
        TMFO = self.ids.TMFO.text
        FVAGF = self.ids.FVAGF.text
        PCC = self.ids.PCC.text
        PCIC = self.ids.PCIC.text
        TFO = self.ids.TFO.text
        CFO = self.ids.CEFO.text
        # Se valida que los campos no esten vacios

        if C == "" or H == "" or S == "" or O == "" or N == "" or W == "" or A == "" or TMFO == "" or FVAGF == "" or PCC == "" or PCIC == "" or TFO == "" or CFO == "":
            toast("No se permiten campos vacios")
        else:
            try:
                update_array = [(C, "CQE_001"),
                                (H, "CQE_002"),
                                (S, "CQE_003"),
                                (O, "CQE_004"),
                                (N, "CQE_005"),
                                (W, "CQE_006"),
                                (A, "CQE_007"),
                                (TMFO, "CQEC_001"),
                                (FVAGF, "CQEC_002"),
                                (PCC, "CQEC_003"),
                                (PCIC, "CQEC_004"),
                                (TFO, "CQEC_005"),
                                (CFO, "CQEC_006"),
                                ]
                db.update_data_params(
                    "CQE", "PORCENTAJE", update_array, "CODIGO = ?")
                toast('CQE actualizado correctamente')
                self.dismiss()

            except Exception as e:
                print("Error de conexion a la base de datos:")
                print(e)
