import tkinter as tk
# --- Galvenais logs un pamatne ---
programmas_logs = tk.Tk()
programmas_logs.title("Klikšķini, lai zīmētu figūru")
pamatne = tk.Canvas(programmas_logs, width=600, height=450, bg="white")
pamatne.pack(fill="both", expand=True, padx=8, pady=8)
# --- Parametri figūrai (izmēri un krāsas) ---
# Ārējais aplis (zils aizpildījums + sarkana svītraina kontūra)
AR_APLIS_RAD = 60
APLS_FILL = "#3b6ed8"
APLS_OUTLINE = "red"
APLS_WIDTH = 4
APLS_DASH = (8, 4)
# Dzeltenais kvadrāts ar zaļu kontūru
KVADRA_PUSE = 40   # puse malas (tātad mala = 80)
KV_FILL = "lightyellow"
KV_OUTLINE = "green"
KV_WIDTH = 4
# Zaļš rombs (kvadrāts pa diagonāli) ar sarkanu kontūru
ROMBS_PUSE = 20
ROMBS_FILL = "lightblue"
ROMBS_OUTLINE = "green"
ROMBS_WIDTH = 2
def uzzimet_kompoziciju(x, y):
    """Uzzīmē kompozīto figūru ar centru punktā (x, y)."""
    punkti = [
        x, y,   
        x + 50, y + 60,   
        x + 25, y + 150,   
        x - 25, y + 150,
        x - 50, y + 60   
    ]
    pamatne.create_polygon(
        punkti, fill=ROMBS_FILL, outline=ROMBS_OUTLINE, width=ROMBS_WIDTH
    )


    # --- Ārējais aplis ---
    # pamatne.create_oval(
    #     x - AR_APLIS_RAD, y - AR_APLIS_RAD, x + AR_APLIS_RAD, y + AR_APLIS_RAD,
    #     fill=APLS_FILL, outline=APLS_OUTLINE, width=APLS_WIDTH, dash=APLS_DASH
    # )
    # # --- Iekšējais kvadrāts ---
    # pamatne.create_rectangle(
    #     x - KVADRA_PUSE, y - KVADRA_PUSE, x + KVADRA_PUSE, y + KVADRA_PUSE,
    #     fill=KV_FILL, outline=KV_OUTLINE, width=KV_WIDTH
    # )
    # # --- Rombs (kvadrāts, pagriezts par 45°) ---
    # punkti = [
    #     x, y - ROMBS_PUSE,   # augša
    #     x + ROMBS_PUSE, y,   # labā mala
    #     x, y + ROMBS_PUSE,   # apakša
    #     x - ROMBS_PUSE, y    # kreisā mala
    # ]
    # pamatne.create_polygon(
    #     punkti, fill=ROMBS_FILL, outline=ROMBS_OUTLINE, width=ROMBS_WIDTH
    # )
def klikskis(event):
    uzzimet_kompoziciju(event.x, event.y)
pamatne.bind("<Button-1>", klikskis)
# --- Poga pamatnes tīrīšanai ---
def notirit():
    pamatne.delete("all")
poga = tk.Button(programmas_logs, text="Notīrīt pamatni", command=notirit)
poga.pack(pady=(0, 8))
programmas_logs.mainloop()
