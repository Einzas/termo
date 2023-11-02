from kivy.uix.popup import Popup
import Database
from kivymd.toast import toast

db = Database.Database()


class GdV(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            valores = db.info("GdV", "VALOR")
            self.ids.CG.text = str(valores[0]).strip("()").strip(",")
            self.ids.EGV.text = str(valores[1]).strip("()").strip(",")
            self.ids.PVM.text = str(valores[2]).strip("()").strip(",")
            self.ids.CEAH.text = str(valores[3]).strip("()").strip(",")

        except Exception as e:
            print("Error de conexion a la base de datos:")
            print(e)

    def guardar(self):
        CG = self.ids.CG.text
        EGV = self.ids.EGV.text
        PVM = self.ids.PVM.text
        CEAH = self.ids.CEAH.text

        if CG == "" or EGV == "" or PVM == "" or CEAH == "":
            toast("Ningun campo debe quedar vacio")
        try:
            updates = [(CG, "GDV_001"),
                       (EGV, "GDV_002"),
                       (PVM, "GDV_003"),
                       (CEAH, "GDV_004")
                       ]

            db.update_data_params("GdV", "VALOR", updates, "CODIGO = ?")
            toast("Los datos han sido actualizados satisfactoriamente.")
            self.dismiss()
        except Exception as e:
            print("Error de conexion a la base de datos:")
            print(e)
