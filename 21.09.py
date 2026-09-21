# class Persona:
#     def __init__(self, vards, vecums, dzimums):
#         self.vards = vards
#         self.dzimums = dzimums
#         if 0 <= vecums <= 150:
#             self.vecums = vecums
#         else:
#             self.vecums=0

#     def personasInformacija(self):
#         print(f'Persona: {self.vards}, vecums: {self.vecums}, dzimums: {self.dzimums}')

# class Darbinieks(Persona):
#     def __init__(self, vards, vecums, dzimums, amats, alga):
#         super().__init__(vards, vecums, dzimums)
#         self.amats = amats
#         self._alga = alga

#     def getAlga(self):
#         return self._alga

#     def darbiniekaInformacija(self):
#         super().personasInformacija()
#         print(f'Amats: {self.amats}, Alga: {self._alga}')

#     def mainitAmatu(self, jaunais_amats):
#         self.amats = jaunais_amats

#     def getAmats(self):
#         return self.amats

#     def paaugsinatAlgu(self, procenti):
#         self._alga *= round(1 + procenti/100)

# def vai_sakrit(amats1, amats2):
#     return amats1 == amats2

# # janis = Persona("Jānis", 200, "v.")

# # print(janis.vecums)


# anna = Persona("Anna", 25, "Sieviete")
# peteris = Persona("Pēteris", 45, "Vīrietis")
# kaspars = Persona("Kaspars", 65, "Vīrietis")

# anna.personasInformacija()
# peteris.personasInformacija()

# del kaspars
# try:
#     if hasattr(kaspars, 'vards'):
#         print("Objekts ar vārdu 'Kaspars' vēl joprojām ir pieejams!")

# except NameError:
#     print("Objekts ar vārdu 'Kaspars' vairs nav pieejams!")


# anna.personasInformacija()

# janis = Darbinieks("Jānis", 35, "Vīrietis", "Programmētājs", 5200)
# # print(janis.vards)
# # print(janis.vecums)
# print(janis.amats)
# # print(janis._alga)
# # print(janis.getAlga())
# ieva = Darbinieks("Ieva", 20, "Sieviete", "Pārdevēja", 900)
# janis.darbiniekaInformacija()

# print('~' *20)
# janis.darbiniekaInformacija()
# janis.mainitAmatu("Sistēmalīktis")
# janis.darbiniekaInformacija()

# print(janis.getAmats())

# print(janis.amats, ieva.amats)

# ieva.paaugsinatAlgu(10)
# ieva.darbiniekaInformacija()


#_________________________________________


# import tkinter as tk
# programmas_logs = tk.Tk()
# programmas_logs.title("Canvas: fill un expand kombinācijas")

# # 1. pamatne: fill=None, expand=False
# pamatne1 = tk.Canvas(programmas_logs, width=150, height=80, bg="lightblue")
# pamatne1.pack(fill='both', expand=False, padx=25, pady=5)

# # 2. pamatne: fill=None, expand=True
# pamatne2 = tk.Canvas(programmas_logs, width=150, height=80, bg="lightgreen")
# pamatne2.pack(fill='both', expand=True, padx=100, pady=100)

# # 3. pamatne: fill=None, expand=False
# pamatne3 = tk.Canvas(programmas_logs, width=150, height=80, bg="lightblue")
# pamatne3.pack(fill='both', expand=True, padx=100, pady=100)

# # 4. pamatne: fill="both", expand=True
# pamatne4 = tk.Canvas(programmas_logs, width=100, height=50, bg="pink")
# pamatne4.pack(fill='both', expand=False, padx=25, pady=50)
# programmas_logs.mainloop()



# import tkinter as tk

# # --- Galvenais logs un pamatne ---
# programmas_logs = tk.Tk()
# programmas_logs.title("Canvas.create_line demonstrācija")
# pamatne = tk.Canvas(programmas_logs, width=900, height=500, bg="white")
# pamatne.pack(fill="both", expand=True, padx=8, pady=8)

# # Palīgfunkcija: uzraksts virs piemēra
# def virsraksts(x, y, teksts):
#     pamatne.create_text(x, y, text=teksts, anchor="w", font=("Arial", 11, "bold"))

# # 1) Vienkārša līnija
# virsraksts(30, 30, "1) Vienkārša līnija")
# pamatne.create_line(30, 50, 260, 50)

# # 2) Bieza līnija (width)
# virsraksts(30, 90, "2) Bieza līnija (width=6)")
# pamatne.create_line(30, 110, 260, 110, width=6)

# # 3) Pārtraukta līnija (dash)
# virsraksts(30, 150, "3) Pārtraukta līnija (dash=(8, 4))")
# pamatne.create_line(30, 170, 260, 170, width=3, dash=(8, 4))

# # 4) Bultiņas (arrow=FIRST/LAST/BOTH)
# virsraksts(30, 210, "4) Bultiņas (arrow=FIRST, LAST, BOTH)")
# pamatne.create_line(30, 230, 260, 230, width=3, arrow=tk.FIRST)
# pamatne.create_line(30, 260, 260, 260, width=3, arrow=tk.LAST)
# pamatne.create_line(30, 290, 260, 290, width=3, arrow=tk.BOTH)

# # 5) capstyle (gali: butt/round/projecting)
# virsraksts(30, 330, "5) capstyle: 'butt', 'round', 'projecting' (width=14)")
# pamatne.create_line(30, 350, 260, 350, width=14, capstyle="butt", fill="#2b6cb0")
# pamatne.create_line(30, 380, 260, 380, width=14, capstyle="round", fill="#38a169")
# pamatne.create_line(30, 410, 260, 410, width=14, capstyle="projecting", fill="#d53f8c")
# pamatne.create_line(30, 340, 30, 420, dash=(2, 2))  # vertikālās palīglīnijas
# pamatne.create_line(260, 340, 260, 420, dash=(2, 2))

# # 6) Dažādi dash raksti
# virsraksts(320, 30, "6) Dažādi 'dash' raksti")
# pamatne.create_line(320, 60, 550, 60, width=4, dash=(3, 3))
# pamatne.create_line(320, 90, 550, 90, width=4, dash=(5, 1),fill="red")
# pamatne.create_line(320, 120, 550, 120, width=4, dash=(15, 7, 10, 3))

# # 7) Kombinācija: arrow + dash + width
# virsraksts(320, 160, "7) Kombinācija: arrow + dash + width")
# pamatne.create_line(320, 190, 550, 190, width=6, dash=(8, 4), arrow=tk.BOTH)

# # --- Palaišana ---
# programmas_logs.mainloop()



# import tkinter as tk

# # --- Galvenais logs un pamatne ---
# programmas_logs = tk.Tk()
# programmas_logs.title("Canvas: Taisnstūri, ovāli un poligoni")
# pamatne = tk.Canvas(programmas_logs, width=700, height=500, bg="white")
# pamatne.pack(fill="both", expand=True, padx=8, pady=8)
# def virsraksts(x, y, teksts):
#     """Uzzīmē virsrakstu pie piemēra"""
#     pamatne.create_text(x, y, text=teksts, anchor="w", font=("Arial", 11, "bold"))

# # 1) Vienkāršs taisnstūris
# virsraksts(30, 30, "1) Vienkāršs taisnstūris")
# pamatne.create_rectangle(30, 50, 180, 120)

# # 2) Aizpildīts taisnstūris
# virsraksts(30, 150, "2) Aizpildīts taisnstūris ")
# pamatne.create_rectangle(30, 170, 180, 240, fill="lightgreen", width=6, outline="red")

# # 3) Vienkāršs ovāls
# virsraksts(250, 30, "3) Vienkāršs ovāls")
# pamatne.create_oval(250, 50, 400, 120)

# # 4) Aplis ar biezāku kontūru
# virsraksts(250, 150, "4) Aplis ar biezāku kontūru")
# # aplis (taisnstūris kvadrāts)
# pamatne.create_oval(250, 170, 320, 240, fill="lightblue", outline="black", width=4)

# # 5, 6) Poligoni: trīsstūris un četrstūris
# virsraksts(470, 30, "5) Poligons: trīsstūris")
# # trīsstūris
# pamatne.create_polygon(470, 120, 520, 50, 570, 120,
#                        outline="black", fill="orange")
# virsraksts(470, 150, "6) Poligons: četrstūris")

# # četrstūris (rombveida)
# pamatne.create_polygon(520, 170, 580, 210, 520, 250, 460, 210,
#                        outline="blue", fill="lightgray", width=2)

# # --- Palaišana ---
# programmas_logs.mainloop()



# import tkinter as tk
# # --- Galvenais logs un pamatne ---
# programmas_logs = tk.Tk()
# programmas_logs.title("Klikšķini, lai zīmētu figūru")
# pamatne = tk.Canvas(programmas_logs, width=600, height=450, bg="white")
# pamatne.pack(fill="both", expand=True, padx=8, pady=8)
# # --- Parametri figūrai (izmēri un krāsas) ---
# # Ārējais aplis (zils aizpildījums + sarkana svītraina kontūra)
# pamatne.create_polygon(50, 150, 110, 100, 170, 150, 150, 200, 80, 200,
#                        outline="green", fill="blue")
# # Dzeltenais kvadrāts ar zaļu kontūru
# KVADRA_PUSE = 40   # puse malas (tātad mala = 80)
# KV_FILL = "lightyellow"
# KV_OUTLINE = "green"
# KV_WIDTH = 4
# # Zaļš rombs (kvadrāts pa diagonāli) ar sarkanu kontūru
# ROMBS_PUSE = 20
# ROMBS_FILL = "green"
# ROMBS_OUTLINE = "red"
# ROMBS_WIDTH = 4
# def uzzimet_kompoziciju(x, y):
#     """Uzzīmē kompozīto figūru ar centru punktā (x, y)."""
#     # --- Ārējais aplis ---
#     pamatne.create_oval(
#          x - AR_APLIS_RAD, y - AR_APLIS_RAD, x + AR_APLIS_RAD, y + AR_APLIS_RAD,
#          fill=APLS_FILL, outline=APLS_OUTLINE, width=APLS_WIDTH, dash=APLS_DASH
#          )
#     # --- Iekšējais kvadrāts ---
#     pamatne.create_rectangle(
#         x - KVADRA_PUSE, y - KVADRA_PUSE, x + KVADRA_PUSE, y + KVADRA_PUSE,
#        fill=KV_FILL, outline=KV_OUTLINE, width=KV_WIDTH
#     )
#     # --- Rombs (kvadrāts, pagriezts par 45°) ---
#     punkti = [
#         x, y - ROMBS_PUSE,   # augša
#         x + ROMBS_PUSE, y,   # labā mala
#         x, y + ROMBS_PUSE,   # apakša
#         x - ROMBS_PUSE, y  # kreisā mala
#     ]
#     pamatne.create_polygon( 
#     punkti, fill=ROMBS_FILL, outline=ROMBS_OUTLINE, width=ROMBS_WIDTH
#     )
# def klikskis(event):
#     uzzimet_kompoziciju(event.x, event.y)
# pamatne.bind("<Button-1>", klikskis)
# # --- Poga pamatnes tīrīšanai ---
# def notirit():
#     pamatne.delete("all")
# poga = tk.Button(programmas_logs, text="Notīrīt pamatni", command=notirit)
# poga.pack(pady=(0, 8))
# programmas_logs.mainloop()



