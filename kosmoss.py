import tkinter as tk
import math
import random

class KosmosaObjekts:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zimet(self, kanva):
        raise NotImplementedError("Metode zimet() jārealizē atvasinātajā klasē")

    def atjaunot(self, kanva):
        pass


class Zvaigzne(KosmosaObjekts):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radiuss = random.randint(15, 25)
        self.redzams = True
        self.taimeris = 0

    def zimet(self, kanva):
        if not self.redzams:
            return

        punkti = []
        for i in range(10):
            lenkis = math.pi / 2 + i * math.pi / 5
            radiuss = self.radiuss if i % 2 == 0 else self.radiuss / 2
            px = self.x + math.cos(lenkis) * radiuss
            py = self.y - math.sin(lenkis) * radiuss
            punkti.extend([px, py])

        kanva.create_polygon(
            punkti,
            fill="yellow",
            outline="orange",
            tags="animacija"
        )

    def atjaunot(self, kanva):
        # Ik pēc 15 kadriem samaina redzamību (mirgošanas efekts)
        self.taimeris += 1
        if self.taimeris % 15 == 0:
            self.redzams = not self.redzams


class Kometa(KosmosaObjekts):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.atrums_x = random.randint(4, 7)
        self.atrums_y = random.randint(3, 5)

    def zimet(self, kanva):
        # Aste
        kanva.create_line(
            self.x - 50, self.y - 35,
            self.x, self.y,
            fill="orange", width=6, tags="animacija"
        )
        kanva.create_line(
            self.x - 40, self.y - 25,
            self.x, self.y,
            fill="yellow", width=3, tags="animacija"
        )
        # Kodols
        kanva.create_oval(
            self.x - 12, self.y - 12,
            self.x + 12, self.y + 12,
            fill="white", outline="yellow", width=2, tags="animacija"
        )

    def atjaunot(self, kanva):
        # Kustība pa diagonāli uz leju un pa labi
        self.x += self.atrums_x
        self.y += self.atrums_y


class Rakete(KosmosaObjekts):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.atrums = random.randint(4, 7)

    def zimet(self, kanva):
        # Korpuss
        kanva.create_rectangle(
            self.x - 12, self.y - 30,
            self.x + 12, self.y + 25,
            fill="lightgrey", outline="white", tags="animacija"
        )
        # Purngals
        kanva.create_polygon(
            self.x - 12, self.y - 30,
            self.x, self.y - 55,
            self.x + 12, self.y - 30,
            fill="red", tags="animacija"
        )
        # Iluminators
        kanva.create_oval(
            self.x - 7, self.y - 18,
            self.x + 7, self.y - 4,
            fill="deepskyblue", tags="animacija"
        )
        # Spārni
        kanva.create_polygon(
            self.x - 12, self.y + 10,
            self.x - 25, self.y + 30,
            self.x - 12, self.y + 25,
            fill="red", tags="animacija"
        )
        kanva.create_polygon(
            self.x + 12, self.y + 10,
            self.x + 25, self.y + 30,
            self.x + 12, self.y + 25,
            fill="red", tags="animacija"
        )
        # Liesma (maina izmēru dinamikai)
        liesmas_garums = random.randint(45, 55)
        kanva.create_polygon(
            self.x - 8, self.y + 25,
            self.x, self.y + liesmas_garums,
            self.x + 8, self.y + 25,
            fill="orange", tags="animacija"
        )

    def atjaunot(self, kanva):
        # Kustība uz augšu
        self.y -= self.atrums


# Globalais objektu saraksts
aktīvie_objekti = []

def pievienot_zvaigzni():
    x = random.randint(100, 800)
    y = random.randint(100, 500)
    aktīvie_objekti.append(Zvaigzne(x, y))

def pievienot_kometu():
    x = random.randint(50, 300)
    y = random.randint(50, 150)
    aktīvie_objekti.append(Kometa(x, y))

def pievienot_raketi():
    x = random.randint(100, 800)
    y = 550
    aktīvie_objekti.append(Rakete(x, y))

def notirit_kanvu():
    aktīvie_objekti.clear()

def animacijas_cikls():
    kanva.delete("animacija")
    
    # Atjauno un pārzīmē katru objektu
    for objekts in aktīvie_objekti:
        objekts.atjaunot(kanva)
        objekts.zimet(kanva)
        
    # Izdzēš objektus, kas izlidojuši ārpus ekrāna
    aktīvie_objekti[:] = [
        obj for obj in aktīvie_objekti 
        if -100 <= obj.x <= 1000 and -100 <= obj.y <= 700
    ]

    # Atkārto ciklu ik pēc 30 milisekundēm (~33 FPS)
    logs.after(30, animacijas_cikls)


# Galvenais logs
logs = tk.Tk()
logs.title("Kosmosa konstruktors")
logs.geometry("900x600")

kanva = tk.Canvas(logs, width=900, height=600, bg="midnightblue")
kanva.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

panelis = tk.Frame(logs, width=180, bg="gray20")
panelis.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(
    panelis,
    text="KOSMOSS",
    fg="white",
    bg="gray20",
    font=("Arial", 16, "bold")
).pack(pady=20)

# Pogas objektu palaišanai
tk.Button(
    panelis,
    text="Palaist Raķeti ",
    width=18,
    command=pievienot_raketi
).pack(pady=10)

tk.Button(
    panelis,
    text="Palaist Kometu ",
    width=18,
    command=pievienot_kometu
).pack(pady=10)

tk.Button(
    panelis,
    text="Pievienot Zvaigzni ",
    width=18,
    command=pievienot_zvaigzni
).pack(pady=10)

tk.Button(
    panelis,
    text="Notīrīt visu ",
    width=18,
    bg="crimson",
    fg="white",
    command=notirit_kanvu
).pack(pady=30)

# Palaist animācijas ciklu un galveno logu
animacijas_cikls()
logs.mainloop()