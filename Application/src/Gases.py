from kivy.uix.popup import Popup
import Database as Database
import math
db = Database.Database()


class Gases(Popup):

    def redondear(numero):
        partes = str(numero).split(".")
        print(partes)
        parte_entera = partes[0]
        parte_decimal = partes[1] if len(partes) > 1 else ""
        print(parte_decimal)
        if parte_decimal and int(parte_decimal[-1]) >= 5:
            if len(str(parte_decimal)) == 1:
                parte_entera = int(parte_entera) + 1
                parte_decimal = "00"
            else:
                parte_decimal = parte_decimal[:-2] + \
                    str(int(parte_decimal[-2]) + 1)
                print(parte_decimal)

        return float(f"{parte_entera}.{parte_decimal}")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        elementos = db.info("CQE", "ELEMENTO, PORCENTAJE",
                            "CODIGO like 'CQE_0%' ORDER BY CODIGO ASC")
        cqe = db.info("CQE", "ELEMENTO, PORCENTAJE",
                      "CODIGO like 'CQEC_0%' ORDER BY CODIGO ASC")
        gdv = db.info("GdV", "VALOR")

        carbono = elementos[0][1]
        hidrogeno = elementos[1][1]
        azufre = elementos[2][1]
        oxigeno = elementos[3][1]
        nitrogeno = elementos[4][1]
        humedad = elementos[5][1]
        cenizas = elementos[6][1]

        temperatura_media_fuel_oil = cqe[0][1]
        flujo_vapor_atomizacion_gf = cqe[1][1]
        poder_calorico_combustible = cqe[2][1]
        poder_calorico_inferior_combustible = cqe[3][1]
        temperatura_fuente_oil = cqe[4][1]
        calor_especifico_fuente_oil = cqe[5][1]

        coeficiente_exceso_horno = gdv[3][0]

        GAS_VTANC = (0.0889 * (carbono + (0.375 * azufre))) + \
            (0.265 * hidrogeno) - (0.0333 * oxigeno)
        self.ids.GAS_VTANC.text = str(Gases.redondear(GAS_VTANC))
        GAS_VGT = round((1.866 * ((carbono + (0.375 * azufre))/100)), 9)
        self.ids.GAS_VGT.text = str(GAS_VGT)
        GAS_VNT = round((0.79 * GAS_VTANC) + (0.8 * (nitrogeno/100)), 9)
        self.ids.GAS_VNT.text = str(GAS_VNT)
        GAS_VTVA = round((0.111*hidrogeno) + (0.0124*humedad) +
                         (0.0161*GAS_VTANC) + (1.24 * flujo_vapor_atomizacion_gf), 9)
        print(GAS_VTANC, GAS_VGT, GAS_VNT, GAS_VTVA)

        self.ids.GAS_VTVA.text = str(GAS_VTVA)
        GAS_VTGPC = round(GAS_VGT + GAS_VNT + GAS_VTVA, 9)
        self.ids.GAS_VTGPC.text = str(GAS_VTGPC)

        GAS2_MPC = (1)-(cenizas/100)+((1.306*coeficiente_exceso_horno)*(GAS_VTANC))
        self.ids.GAS2_MPC.text= str(GAS2_MPC)
        GAS2_VRPA = GAS_VTVA + (0.0161*(coeficiente_exceso_horno-1)*GAS_VTANC)
        self.ids.GAS2_VRPA.text = str(GAS2_VRPA)
        GAS2_VRGPGPC = (GAS_VGT + GAS_VNT + GAS2_VRPA) + ((coeficiente_exceso_horno -1 ) * GAS_VTANC )
        self.ids.GAS2_VRGPGPC.text = str(GAS2_VRGPGPC)
        GAS2_VGRG = GAS2_VRGPGPC * 0.2
        self.ids.GAS2_VGRG.text = str(GAS2_VGRG)
        GAS2_VTGPC = GAS2_VRGPGPC + GAS2_VGRG
        self.ids.GAS2_VTGPC.text = str(GAS2_VTGPC)
        GAS2_FVGT = GAS_VGT / GAS2_VTGPC
        self.ids.GAS2_FVGT.text = str(GAS2_FVGT)
        GAS2_FVVA = GAS2_VRPA / GAS2_VTGPC
        self.ids.GAS2_FVVA.text = str(GAS2_FVVA)
        GAS2_FVT = GAS2_FVGT + GAS2_FVVA
        self.ids.GAS2_FVT.text = str(GAS2_FVT)
        GAS2_VGS = GAS_VGT + GAS_VNT + ((coeficiente_exceso_horno-1)*GAS_VTANC)
        self.ids.GAS2_VGS.text = str(GAS2_VGS)
    def guardar():
        print("Guardando datos")
