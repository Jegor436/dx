# 1.uzd Botāniskais dārzs -----------------------------------------------------------------

# class BotaniskaisDarzs:
#     def __init__(self):
#         self.nosaukums = ""
#         self.skaits = 0
#         self.pilseta = ""

#     def ievadit(self):
#         self.nosaukums = input("Ievadiet dārza nosaukumu: ")
#         self.skaits = int(input("Ievadiet augu skaitu: "))
#         self.pilseta = input("Ievadiet pilsētu: ")

#     def izvadit(self):
#         print(f'Botāniskais dārzs "{self.nosaukums}". Atrašanās vieta: {self.pilseta}. Botāniskajā dārzā ir {self.skaits} augi.')

#     def parbaudit(self):
#         if self.skaits > 1000:
#             print("Kolekcija ir ļoti plaša.")
#         else:
#             print("Kolekcijā vēl ir vietas.")


# botaniskais_darzs = BotaniskaisDarzs()
# botaniskais_darzs.ievadit()
# botaniskais_darzs.izvadit()
# botaniskais_darzs.parbaudit()


#2.uzd. Augi: koki un ziedi ---------------------------------------------------------------

# class Augs:
#     def __init__(self, nosaukums, vecums, tips):
#         self.nosaukums = nosaukums
#         self.vecums = vecums
#         self.tips = tips

# class Koks(Augs):
#     def __init__(self, nosaukums, vecums, augstums):
#         super().__init__(nosaukums, vecums, 1)
#         self.augstums = augstums

#     def izdrukat(self):
#         print(f'Koks (tips - {self.tips}) nosaukums: {self.nosaukums}', end="")
#         print(f', augstums: {self.augstums}m, vecums: {self.vecums} gadi.')

# class Zieds(Augs):
#     def __init__(self, nosaukums, vecums, krasa):
#         super().__init__(nosaukums, vecums, 2)
#         self.krasa = krasa

#     def izdrukat(self):
#         print(f'Zieds (tips - {self.tips}) nosaukums: {self.nosaukums}', end="")
#         print(f', zieda krāsa: {self.krasa}, vecums: {self.vecums} gads.')


# nosaukums_koks = input("Ievadiet koka nosaukumu: ")
# vecums_koks = input("Ievadiet koka vecumu: ")
# augstums_koks = input("Ievadiet koka augstumu: ")
# koks = Koks(nosaukums_koks, vecums_koks, augstums_koks)

# nosaukums_zieds = input("Ievadiet zieda nosaukumu: ")
# vecums_zieds = input("Ievadiet zieda vecumu: ")
# krasa_zieds = input("Ievadiet zieda krāsu: ")
# zieds = Zieds(nosaukums_zieds, vecums_zieds, krasa_zieds)

# koks.izdrukat()
# zieds.izdrukat()


#3. uzd. Nogrieznis koordinātu plaknē -----------------------------------------------------

# import tkinter as tk
# import math

# class KoordinatuPlakne(tk.Canvas):
#     def __init__(self, logs, platums=400, augstums=400, solis=20):
#         # Inicializē kanvu ar baltu fonu
#         super().__init__(logs, width=platums, height=augstums, bg="white")
#         self.platums = platums
#         self.augstums = augstums
#         self.solis = solis
#         # Nosaka koordinātu sākumpunktu (0,0) ekrānā
#         self.x0 = platums // 2
#         self.y0 = augstums // 2
#         # Zīmē režģi un asis
#         self.zimet_rezgi()
#         self.zimet_asis()

#     # --- Koordinātu pārveidošana ---
#     def uz_ekrana_koordinatam(self, x: float, y: float):
#         return int(self.x0 + x * self.solis), int(self.y0 - y * self.solis)

#     # --- Režģis un asis ---
#     def zimet_rezgi(self):
#         self.delete("rezgis")
#         # Vertikālās līnijas
#         x = self.x0
#         while x < self.platums:
#             self.create_line(x, 0, x, self.augstums, fill="#c9c9c9", width=1, tags=("rezgis",))
#             x += self.solis
#         x = self.x0
#         while x > 0:
#             self.create_line(x, 0, x, self.augstums, fill="#c9c9c9", width=1, tags=("rezgis",))
#             x -= self.solis

#         # Horizontālās līnijas
#         y = self.y0
#         while y < self.augstums:
#             self.create_line(0, y, self.platums, y, fill="#c9c9c9", width=1, tags=("rezgis",))
#             y += self.solis
#         y = self.y0
#         while y > 0:
#             self.create_line(0, y, self.platums, y, fill="#c9c9c9", width=1, tags=("rezgis",))
#             y -= self.solis

#     def zimet_asis(self):
#         self.delete("asis")
#         # X ass
#         self.create_line(0, self.y0, self.platums, self.y0, fill="black", width=2, tags=("asis",))
#         bulta = [self.platums-10, self.y0-5, self.platums, self.y0, self.platums-10, self.y0+5]
#         self.create_polygon(bulta, fill="black", tags=("asis",))
#         # Y ass
#         self.create_line(self.x0, 0, self.x0, self.augstums, fill="black", width=2, tags=("asis",))
#         bulta = [self.x0-5, 10, self.x0, 0, self.x0+5, 10] 
#         self.create_polygon(bulta, fill="black", tags=("asis",))
#         # X ass cipari
#         xmin = -self.platums // (2 * self.solis)
#         xmax =  self.platums // (2 * self.solis)
#         for x in range(xmin, xmax + 1):
#             if x == 0:
#                 continue
#             xs, ys = self.uz_ekrana_koordinatam(x, 0)
#             self.create_text(xs, ys + 12, text=str(x), font=("Arial", 8), fill = "black", tags=("asis",))
#         # Y ass cipari
#         ymin = -self.augstums // (2 * self.solis)
#         ymax =  self.augstums // (2 * self.solis)
#         for y in range(ymin, ymax + 1):
#             if y == 0:
#                 continue
#             xs, ys = self.uz_ekrana_koordinatam(0, y)
#             self.create_text(xs - 12, ys, text=str(y), font=("Arial", 8), tags=("asis",))

#     # --- Punktu zīmēšana ---
#     def zimet_punktu(self, P, r: int = 4, birka: str = "dati"):
#         krasa = P.color
#         xs, ys = self.uz_ekrana_koordinatam(P.x, P.y)
#         self.create_oval(xs - r, ys - r, xs + r, ys + r, fill=krasa, outline="", tags=(birka,))

#     def uzraksts_pie_punkta(self, x: float, y: float, teksts: str, nobide_x: int = 12, nobide_y: int = -12, birka: str = "dati"):
#         xs, ys = self.uz_ekrana_koordinatam(x, y)
#         if y<0:
#             nobide_y *= -1
#         self.create_text(xs + nobide_x, ys + nobide_y, text=teksts, font=("Arial", 10), fill="black", tags=(birka,))
           
#     # UZDEVUMS: uzrakstit metodi nogrieznis(P1, P2) — zime liniju starp P1 un P2
#     def nogrieznis(self, P1, P2, birka: str = "dati"):
#         xs1, ys1 = self.uz_ekrana_koordinatam(P1.x, P1.y)
#         xs2, ys2 = self.uz_ekrana_koordinatam(P2.x, P2.y)
#         self.create_line(xs1, ys1, xs2, ys2, fill="blue", width=2, tags=(birka,))
        
#      # UZDEVUMS: uzrakstit metodi nogriezna_garums(P1, P2) — izvadit garumu apakseja kreisaja sturi
#     def nogriezna_garums(self, P1, P2):
#         garums = math.sqrt((P2.x - P1.x)**2 + (P2.y - P1.y)**2)
#         self.create_text(10, self.augstums - 15, anchor="sw", text=f'Nogriežņa garums: {garums:.2f}', font=("Arial", 10, "bold"), fill="blue", tags=("dati",))

# class Punkts:
#     def __init__(self, x, y, color="red"):
#         self.x = x
#         self.y = y
#         self.color = color

# # ====== Demonstrācija ======
# pamatne = tk.Tk()
# pamatne.title("Nogriežnis koordinātu plaknē")
# plakne = KoordinatuPlakne(pamatne, platums=400, augstums=300, solis=20)
# plakne.pack()

# A = Punkts(-5, -2, "grey")
# # Uzzīmējam punktus un etiķetes
# plakne.zimet_punktu(A)
# plakne.uzraksts_pie_punkta(A.x, A.y, f"A({A.x:.1f}; {A.y:.1f})")

# # UZDEVUMS: Izveidot punktu B
# B = Punkts(4, 3, "blue")

# # UZDEVUMS: Uzzīmēt punktu B
# plakne.zimet_punktu(B)
# plakne.uzraksts_pie_punkta(B.x, B.y, f"B({B.x:.1f}; {B.y:.1f})")

# # UZDEVUMS: Uzzīmēt AB nogriezni koordinātu plaknē
# plakne.nogrieznis(A, B)

# # UZDEVUMS: Aprēķināt un parādīt nogriežņa AB garumu
# plakne.nogriezna_garums(A, B)

# pamatne.mainloop()


#4.uzd. Punkti koordinātu plaknē ------------------------------------------------------------------------------

#---
