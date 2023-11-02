from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.toast import toast
import Database as Database
db = Database.Database()


class PdC(FloatLayout, Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            valores = db.info("PdC", "CINCUENTA, SETENTACINCO, CIEN")
            # Se llenan los campos de la ventana
            self.ids.PCAE_C.text = str(valores[1][0])
            self.ids.PCAE_S.text = str(valores[1][1])
            self.ids.PCAE_CI.text = str(valores[1][2])

            self.ids.PCAS_C.text = str(valores[2][0])
            self.ids.PCAS_S.text = str(valores[2][1])
            self.ids.PCAS_CI.text = str(valores[2][2])

            self.ids.PCFV_C.text = str(valores[3][0])
            self.ids.PCFV_S.text = str(valores[3][1])
            self.ids.PCFV_CI.text = str(valores[3][2])

            self.ids.PCPVP_C.text = str(valores[4][0])
            self.ids.PCPVP_S.text = str(valores[4][1])
            self.ids.PCPVP_CI.text = str(valores[4][2])

            self.ids.PCTVP_C.text = str(valores[5][0])
            self.ids.PCTVP_S.text = str(valores[5][1])
            self.ids.PCTVP_CI.text = str(valores[5][2])

            self.ids.PCFVS_C.text = str(valores[6][0])
            self.ids.PCFVS_S.text = str(valores[6][1])
            self.ids.PCFVS_CI.text = str(valores[6][2])

            self.ids.PCTVS_C.text = str(valores[7][0])
            self.ids.PCTVS_S.text = str(valores[7][1])
            self.ids.PCTVS_CI.text = str(valores[7][2])

            self.ids.PCTAA_C.text = str(valores[8][0])
            self.ids.PCTAA_S.text = str(valores[8][1])
            self.ids.PCTAA_CI.text = str(valores[8][2])

            self.ids.PCFC_C.text = str(valores[9][0])
            self.ids.PCFC_S.text = str(valores[9][1])
            self.ids.PCFC_CI.text = str(valores[9][2])

            self.ids.PCNQ_C.text = str(valores[10][0])
            self.ids.PCNQ_S.text = str(valores[10][1])
            self.ids.PCNQ_CI.text = str(valores[10][2])

            self.ids.PCFVA_C.text = str(valores[11][0])
            self.ids.PCFVA_S.text = str(valores[11][1])
            self.ids.PCFVA_CI.text = str(valores[11][2])

            self.ids.PCPVA_C.text = str(valores[12][0])
            self.ids.PCPVA_S.text = str(valores[12][1])
            self.ids.PCPVA_CI.text = str(valores[12][2])

            self.ids.PCPVAK_C.text = str(valores[13][0])
            self.ids.PCPVAK_S.text = str(valores[13][1])
            self.ids.PCPVAK_CI.text = str(valores[13][2])

            self.ids.PCEVS_C.text = str(valores[14][0])
            self.ids.PCEVS_S.text = str(valores[14][1])
            self.ids.PCEVS_CI.text = str(valores[14][2])

            self.ids.PCELS_C.text = str(valores[15][0])
            self.ids.PCELS_S.text = str(valores[15][1])
            self.ids.PCELS_CI.text = str(valores[15][2])

            self.ids.PCEVP_C.text = str(valores[16][0])
            self.ids.PCEVP_S.text = str(valores[16][1])
            self.ids.PCEVP_CI.text = str(valores[16][2])

            self.ids.PCES_C.text = str(valores[17][0])
            self.ids.PCES_S.text = str(valores[17][1])
            self.ids.PCES_CI.text = str(valores[17][2])

            self.ids.PCPD_C.text = str(valores[18][0])
            self.ids.PCPD_S.text = str(valores[18][1])
            self.ids.PCPD_CI.text = str(valores[18][2])

            self.ids.PCEAA_C.text = str(valores[19][0])
            self.ids.PCEAA_S.text = str(valores[19][1])
            self.ids.PCEAA_CI.text = str(valores[19][2])

            self.ids.PCFVSH_C.text = str(valores[20][0])
            self.ids.PCFVSH_S.text = str(valores[20][1])
            self.ids.PCFVSH_CI.text = str(valores[20][2])

            self.ids.PCTVSH_C.text = str(valores[21][0])
            self.ids.PCTVSH_S.text = str(valores[21][1])
            self.ids.PCTVSH_CI.text = str(valores[21][2])

            self.ids.PCPVSH_C.text = str(valores[22][0])
            self.ids.PCPVSH_S.text = str(valores[22][1])
            self.ids.PCPVSH_CI.text = str(valores[22][2])

            self.ids.PCEVSO_C.text = str(valores[23][0])
            self.ids.PCEVSO_S.text = str(valores[23][1])
            self.ids.PCEVSO_CI.text = str(valores[23][2])

            self.ids.PCTGR_C.text = str(valores[24][0])
            self.ids.PCTGR_S.text = str(valores[24][1])
            self.ids.PCTGR_CI.text = str(valores[24][2])

            self.ids.PCEGR_C.text = str(valores[25][0])
            self.ids.PCEGR_S.text = str(valores[25][1])
            self.ids.PCEGR_CI.text = str(valores[25][2])

            self.ids.PCIR_C.text = str(valores[26][0])
            self.ids.PCIR_S.text = str(valores[26][1])
            self.ids.PCIR_CI.text = str(valores[26][2])

        except Exception as e:
            print("Error de conexion a la base de datos:")
            print(e)

    def guardar(self):

        PCAE_C = self.ids.PCAE_C.text
        PCAE_S = self.ids.PCAE_S.text
        PCAE_CI = self.ids.PCAE_CI.text

        PCAS_C = self.ids.PCAS_C.text
        PCAS_S = self.ids.PCAS_S.text
        PCAS_CI = self.ids.PCAS_CI.text

        PCFV_C = self.ids.PCFV_C.text
        PCFV_S = self.ids.PCFV_S.text
        PCFV_CI = self.ids.PCFV_CI.text

        PCPVP_C = self.ids.PCPVP_C.text
        PCPVP_S = self.ids.PCPVP_S.text
        PCPVP_CI = self.ids.PCPVP_CI.text

        PCTVP_C = self.ids.PCTVP_C.text
        PCTVP_S = self.ids.PCTVP_S.text
        PCTVP_CI = self.ids.PCTVP_CI.text

        PCFVS_C = self.ids.PCFVS_C.text
        PCFVS_S = self.ids.PCFVS_S.text
        PCFVS_CI = self.ids.PCFVS_CI.text

        PCTVS_C = self.ids.PCTVS_C.text
        PCTVS_S = self.ids.PCTVS_S.text
        PCTVS_CI = self.ids.PCTVS_CI.text

        PCTAA_C = self.ids.PCTAA_C.text
        PCTAA_S = self.ids.PCTAA_S.text
        PCTAA_CI = self.ids.PCTAA_CI.text

        PCFC_C = self.ids.PCFC_C.text
        PCFC_S = self.ids.PCFC_S.text
        PCFC_CI = self.ids.PCFC_CI.text

        PCNQ_C = self.ids.PCNQ_C.text
        PCNQ_S = self.ids.PCNQ_S.text
        PCNQ_CI = self.ids.PCNQ_CI.text

        PCFVA_C = self.ids.PCFVA_C.text
        PCFVA_S = self.ids.PCFVA_S.text
        PCFVA_CI = self.ids.PCFVA_CI.text

        PCPVA_C = self.ids.PCPVA_C.text
        PCPVA_S = self.ids.PCPVA_S.text
        PCPVA_CI = self.ids.PCPVA_CI.text

        PCPVAK_C = self.ids.PCPVAK_C.text
        PCPVAK_S = self.ids.PCPVAK_S.text
        PCPVAK_CI = self.ids.PCPVAK_CI.text

        PCEVS_C = self.ids.PCEVS_C.text
        PCEVS_S = self.ids.PCEVS_S.text
        PCEVS_CI = self.ids.PCEVS_CI.text

        PCELS_C = self.ids.PCELS_C.text
        PCELS_S = self.ids.PCELS_S.text
        PCELS_CI = self.ids.PCELS_CI.text

        PCEVP_C = self.ids.PCEVP_C.text
        PCEVP_S = self.ids.PCEVP_S.text
        PCEVP_CI = self.ids.PCEVP_CI.text

        PCES_C = self.ids.PCES_C.text
        PCES_S = self.ids.PCES_S.text
        PCES_CI = self.ids.PCES_CI.text

        PCPD_C = self.ids.PCPD_C.text
        PCPD_S = self.ids.PCPD_S.text
        PCPD_CI = self.ids.PCPD_CI.text

        PCEAA_C = self.ids.PCEAA_C.text
        PCEAA_S = self.ids.PCEAA_S.text
        PCEAA_CI = self.ids.PCEAA_CI.text

        PCFVSH_C = self.ids.PCFVSH_C.text
        PCFVSH_S = self.ids.PCFVSH_S.text
        PCFVSH_CI = self.ids.PCFVSH_CI.text

        PCTVSH_C = self.ids.PCTVSH_C.text
        PCTVSH_S = self.ids.PCTVSH_S.text
        PCTVSH_CI = self.ids.PCTVSH_CI.text

        PCPVSH_C = self.ids.PCPVSH_C.text
        PCPVSH_S = self.ids.PCPVSH_S.text
        PCPVSH_CI = self.ids.PCPVSH_CI.text

        PCEVSO_C = self.ids.PCEVSO_C.text
        PCEVSO_S = self.ids.PCEVSO_S.text
        PCEVSO_CI = self.ids.PCEVSO_CI.text

        PCTGR_C = self.ids.PCTGR_C.text
        PCTGR_S = self.ids.PCTGR_S.text
        PCTGR_CI = self.ids.PCTGR_CI.text

        PCEGR_C = self.ids.PCEGR_C.text
        PCEGR_S = self.ids.PCEGR_S.text
        PCEGR_CI = self.ids.PCEGR_CI.text

        PCIR_C = self.ids.PCIR_C.text
        PCIR_S = self.ids.PCIR_S.text
        PCIR_CI = self.ids.PCIR_CI.text

        if PCAE_C == "" or PCAE_S == "" or PCAE_CI == "" or PCAS_C == "" or PCAS_S == "" or PCAS_CI == "" or PCFV_C == "" or PCFV_S == "" or PCFV_CI == "" or PCPVP_C == "" or PCPVP_S == "" or PCPVP_CI == "" or PCTVP_C == "" or PCTVP_S == "" or PCTVP_CI == "" or PCFVS_C == "" or PCFVS_S == "" or PCFVS_CI == "" or PCTVS_C == "" or PCTVS_S == "" or PCTVS_CI == "" or PCTAA_C == "" or PCTAA_S == "" or PCTAA_CI == "" or PCFC_C == "" or PCFC_S == "" or PCFC_CI == "" or PCNQ_C == "" or PCNQ_S == "" or PCNQ_CI == "" or PCFVA_C == "" or PCFVA_S == "" or PCFVA_CI == "" or PCPVA_C == "" or PCPVA_S == "" or PCPVA_CI == "" or PCPVAK_C == "" or PCPVAK_S == "" or PCPVAK_CI == "" or PCEVS_C == "" or PCEVS_S == "" or PCEVS_CI == "" or PCELS_C == "" or PCELS_S == "" or PCELS_CI == "" or PCEVP_C == "" or PCEVP_S == "" or PCEVP_CI == "" or PCES_C == "" or PCES_S == "" or PCES_CI == "" or PCPD_C == "" or PCPD_S == "" or PCPD_CI == "" or PCEAA_C == "" or PCEAA_S == "" or PCEAA_CI == "" or PCFVSH_C == "" or PCFVSH_S == "" or PCFVSH_CI == "" or PCTVSH_C == "" or PCTVSH_S == "" or PCTVSH_CI == "" or PCPVSH_C == "" or PCPVSH_S == "" or PCPVSH_CI == "" or PCEVSO_C == "" or PCEVSO_S == "" or PCEVSO_CI == "" or PCTGR_C == "" or PCTGR_S == "" or PCTGR_CI == "" or PCEGR_C == "" or PCEGR_S == "" or PCEGR_CI == "" or PCIR_C == "" or PCIR_S == "" or PCIR_CI == "":
            toast("Ningun campo debe quedar vacio")

        try:
            sql = "UPDATE PdC SET CINCUENTA = ?, SETENTACINCO = ?, CIEN = ? WHERE CODIGO = ?"

            updates = [(PCAE_C, PCAE_S, PCAE_CI, "PDC_002"),
                       (PCAS_C, PCAS_S, PCAS_CI, "PDC_003"),
                       (PCFV_C, PCFV_S, PCFV_CI, "PDC_004"),
                       (PCPVP_C, PCPVP_S, PCPVP_CI, "PDC_005"),
                       (PCTVP_C, PCTVP_S, PCTVP_CI, "PDC_006"),
                       (PCFVS_C, PCFVS_S, PCFVS_CI, "PDC_007"),
                       (PCTVS_C, PCTVS_S, PCTVS_CI, "PDC_008"),
                       (PCTAA_C, PCTAA_S, PCTAA_CI, "PDC_009"),
                       (PCFC_C, PCFC_S, PCFC_CI, "PDC_010"),
                       (PCNQ_C, PCNQ_S, PCNQ_CI, "PDC_011"),
                       (PCFVA_C, PCFVA_S, PCFVA_CI, "PDC_012"),
                       (PCPVA_C, PCPVA_S, PCPVA_CI, "PDC_013"),
                       (PCPVAK_C, PCPVAK_S, PCPVAK_CI, "PDC_014"),
                       (PCEVS_C, PCEVS_S, PCEVS_CI, "PDC_015"),
                       (PCELS_C, PCELS_S, PCELS_CI, "PDC_016"),
                       (PCEVP_C, PCEVP_S, PCEVP_CI, "PDC_017"),
                       (PCES_C, PCES_S, PCES_CI, "PDC_018"),
                       (PCPD_C, PCPD_S, PCPD_CI, "PDC_019"),
                       (PCEAA_C, PCEAA_S, PCEAA_CI, "PDC_020"),
                       (PCFVSH_C, PCFVSH_S, PCFVSH_CI, "PDC_021"),
                       (PCTVSH_C, PCTVSH_S, PCTVSH_CI, "PDC_022"),
                       (PCPVSH_C, PCPVSH_S, PCPVSH_CI, "PDC_023"),
                       (PCEVSO_C, PCEVSO_S, PCEVSO_CI, "PDC_024"),
                       (PCTGR_C, PCTGR_S, PCTGR_CI, "PDC_025"),
                       (PCEGR_C, PCEGR_S, PCEGR_CI, "PDC_026"),
                       (PCIR_C, PCIR_S, PCIR_CI, "PDC_027"),
                       ]
            db.update(sql, updates)
            toast("Los datos han sido actualizados satisfactoriamente.")
            self.dismiss()
        except Exception as e:
            print("Error de conexion a la base de datos:")
            print(e)
