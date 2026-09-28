import tkinter as tk
import math
import random

class KosmosaObjekts:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zimet(self, kanva):
        raise NotImplementedError(
            "Metode zimet() jārealizē atvasinātajā klasē"
        )

class Zvaigzne(KosmosaObjekts):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radiuss = random.randint(10, 25)
        self.krasa = "yellow"
        objekti = []

    def zimet(self, kanva):
        punkti = []

        for i in range(10):
            lenkis = math.pi / 2 + i * math.pi / 5
            if i % 2 == 0:
                radiuss = self.radiuss
            else:
                radiuss = self.radiuss / 2  

            x = self.x + math.cos(lenkis) * radiuss
            y = self.y - math.sin(lenkis) * radiuss

            kanva.create_polygon(
                punkti,
                fill="yellow",
                outline="orange"
            )

    def pievienot_zvaigzni(event):
        x = event.x
        y = event.y

        zvaigzne = Zvaigzne(x, y)
        zvaigzne.zimet(kanva)

    kanva.bind(
        "<Button-1>",
        pievienot_zvaigzni
        )

class Kometa(KosmosaObjekts):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.atrums_x = random.randint(2, 5)
        self.atrums_y = random.randint(1, 3)

    def zimet(self, kanva):
        kanva.create_line(
            self.x-70, self.y-40,
            self.x, self.y,
            fill="orange", width=8
        )
        
        kanva.create_line(
            self.x-60, self.y-30,
            self.x, self.y,
            fill="yellow", width=4
        )
        
        kanva.create_oval(
            self.x-15, self.y-15,
            self.x+15, self.y+15,
            fill="white", outline="yellow", width=3
        )

class Rakete(KosmosaObjekts):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.atrums = random.randint(2, 5)

    def zimet(self, kanva):
        kanva.create_rectangle(
            self.x-12,
            self.y-30,
            self.x+12,
            self.y+25,
            fill="lightgrey",
            outline="white"
            )
        
        kanva.create_polygon(
            self.x-12, self.y-30,
            self.x, self.y - 55,
            self.x+12, self.y-30,
            fill="red",
            )
        
        kanva.create_oval(
            self.x-7,
            self.y-18,
            self.x+7,
            self.y-4,
            fill="deepskyblue"
            )
        
        kanva.create_polygon(
            self.x-12, self.y+10,
            self.x-28, self.y+30,
            self.x-12, self.y+25,
            fill="red"
            )
        
        kanva.create_polygon(
            self.x+12, self.y+10,
            self.x+28, self.y+30,
            self.x+12, self.y+25,
            fill="red"
            )
        
        kanva.create_polygon(
            self.x-8, self.y+25,
            self.x, self.y+50,
            self.x+8, self.y+25,
            fill="orange"
            )

        rakete = Rakete(400, 300)
        rakete.zimet(kanva)


logs = tk.Tk()
logs.title("Kosmosa konstruktors")
logs.geometry("900x600")

kanva = tk.Canvas(
    logs, width=900, height=600, bg="midnightblue")

kanva.pack(
    side = tk.RIGHT,
    fill=tk.BOTH,
    expand=True)

panelis = tk.Frame(
    logs,
    width=180,
    bg="gray20"
)

panelis.pack(
    side=tk.LEFT,
    fill=tk.Y
)

tk.Label(
    panelis,
    text="KOSMOSS",
    fg="white",
    bg="gray20",
    font=("Arial", 16, "bold")
).pack(pady=20)

def izveleties_tipu(tips):
    global izveletais_tips

    izveletais_tips = tips

tk.Button(
    panelis,
    text="Zvaigzne",
    width=15,
    command=lambda: izveleties_tipu("zvaigzne")
).pack(pady=5)

tk.Button(
    panelis,
    text="Kometa",
    width=15,
    command=lambda: izveleties_tipu("kometa")
).pack(pady=5)

tk.Button(
    panelis,
    text="Raķete",
    width=15,
    command=lambda: izveleties_tipu("rakete")
).pack(pady=5)

def pievienot_objektu(event):
    x = event.x
    y = event.y

    if izveletais_tips == "zvaigzne":
        objekts = Zvaigzne(x, y)
    elif izveletais_tips == "kometa":
        objekts = Kometa(x, y)
    elif izveletais_tips == "rakete":
        objekts = Rakete(x, y)

    objekti.append(objekts)
    objekts.zimet(kanva)

kanva.bind(
    "<Button-1>",
    pievienot_objektu
)

# def zimet_raketi(x, y):

#     kanva.create_rectangle(
#         x-12,
#         y-30,
#         x+12,
#         y+25,
#         fill="lightgrey",
#         outline="white"
#         )

#     kanva.create_polygon(
#         x-12, y-30,
#         x, y - 55,
#         x+12, y-30,
#         fill="red",
#     )

#     kanva.create_oval(
#         x-7,
#         y-18,
#         x+7,
#         y-4,
#         fill="deepskyblue"
#     )

#     kanva.create_polygon(
#         x-12, y+10,
#         x-28, y+30,
#         x-12, y+25,
#         fill="red"
#     )

#     kanva.create_polygon(
#         x+12, y+10,
#         x+28, y+30,
#         x+12, y+25,
#         fill="red"
#     )

#     kanva.create_polygon(
#         x-8, y+25,
#         x, y+50,
#         x+8, y+25,
#         fill="orange"
#         )

# def zimet_kometu(x, y):

#     kanva.create_line(
#         x-70, y-40,
#         x, y,
#         fill="orange", width=8
#     )

#     kanva.create_line(
#         x-60, y-30,
#         x, y,
#         fill="yellow", width=4
#     )

#     kanva.create_oval(
#         x-15, y-15,
#         x+15, y+15,
#         fill="white", outline="yellow", width=3
#     )
 
# def zimet_zvaigzni(x, y, radiuss=25):
#     punkti = []

#     for i in range(10):
#             lenkis = math.pi / 2 + i * math.pi / 5
#     if i % 2 == 0:
#             r = radiuss
#     else:
#             r = radiuss / 2

#     punkts_x = x + math.cos(lenkis) * r
#     punkts_y = y + math.sin(lenkis) * r
#     punkti.extend([punkts_x, punkts_y])

#     kanva.create_polygon(
#          punkti,
#          fill="yellow",
#          outline="orange"
#          )


zimet_raketi(400, 250)
zimet_kometu(700, 250)
zimet_zvaigzni(150, 150, 100)

ooo = KosmosaObjekts()
ooo.zimet()

logs.mainloop()