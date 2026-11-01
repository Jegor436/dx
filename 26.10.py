#LIST =================================================================================

#1. Saraksta izveidošana --------------------------------------------------------------

# augli = ["banans", "abols", "bumbieris", "apelsins", "citrons"]
# print(augli[0])
# print(augli[4])

#2. Elementu pievienošana -------------------------------------------------------------

# skaitli = [10, 20, 30]
# skaitli.append(40)
# skaitli.insert(2, 15)

# print(skaitli)

#3. Elementu dzēšana -------------------------------------------------------------------

# krasas = ["sarkana", "zaļa", "zila", "dzeltena"]
# del krasas[1]
# del krasas[2]

# print(krasas)

#4. Skaitļu summa un vidējais ----------------------------------------------------------

# skaitli = [5, 10, 15, 20, 25]
# summa = sum(skaitli)
# videjais = sum(skaitli) / len(skaitli)
# minimalais = min(skaitli)
# maksimalais = max(skaitli)

# print(summa)
# print(videjais)
# print(minimalais)
# print(maksimalais)

#5. Pāra un nepāra skaitļi -------------------------------------------------------------

# skaitli = [1, 4, 7, 10, 13, 16, 19, 22]
# para = [x for x in skaitli if x % 2 == 0]
# nepara = [x for x in skaitli if x %2 != 0]

# print(para)
# print(nepara)

#6. Saraksta kārtošana -----------------------------------------------------------------

# atzimes = [7, 10, 5, 8, 9, 6]
# atzimes.sort()
# atzimes.sort(reverse=True)

# print(atzimes)

#7. Elementu meklēšana -----------------------------------------------------------------

# vardi = ["Anna", "Jānis", "Pēteris", "Laura", "Marta"]
# vards = input("Ievadi vārdu: ")
# if vards in vardi:
#     print(vards)
# else:
#     print("Vārds nav atrasts")    

#8. Dublikātu skaitīšana ---------------------------------------------------------------

# skaitli = [2, 3, 2, 5, 3, 2, 7, 5]
# print(skaitli.count(2))
# print(skaitli.count(3))
# print(skaitli.count(5))
# print(skaitli.count(7))

#9. Otrais lielākais skaitlis ----------------------------------------------------------

# skaitli = [12, 45, 23, 67, 67, 34, 56]
# skaitlis = sorted(list(set(skaitli)), reverse=True)
# if len(skaitlis) >= 2:
#     otrais = skaitlis[1]
#     print(otrais)
# else:
#     print("Nav")

#10. Skolēnu atzīmju analīze -----------------------------------------------------------

# atzimes = [5, 3, 8, 6, 10]
# videjais = sum(atzimes) / len(atzimes)
# maks = max(atzimes)
# mini = min(atzimes)
# skaits = sum(1 for a in atzimes if a >= 8)
# sakart = sorted(atzimes)

# print(atzimes)
# print(videjais)
# print(maks)
# print(mini)
# print(skaits)
# print(sakart)

#TUPLE =================================================================================

#1. Kortēža izveidošana ----------------------------------------------------------------

# dienas = ("Pirmdiena", "Otrdiena", "Trešdiena", "Ceturdiena", "Piektdiena", "Sestdiena", "Svētdiena")
# print(dienas[0])
# print(dienas[2])
# print(dienas[-1])

#2. Elementu skaitīšana ----------------------------------------------------------------

# skaitli = (5, 10, 15, 20, 25)
# skaits = len(skaitli)
# summa = sum(skaitli)
# maks = max(skaitli)
# mini = min(skaitli)

# print(skaitli)
# print(skaits)
# print(summa)
# print(maks)
# print(mini)

#3. Vērtības atkārtojumi ---------------------------------------------------------------

# skaitli = (1, 2, 3, 2, 4, 2, 5)
# print(skaitli.count(2))
# print(skaitli.index(2))

#4. Korteža izpakošana -----------------------------------------------------------------

# students = ("Anna", 17, "Rīga", 9)
# vards, vecums, pilseta, atzime = students

# print(vards)
# print(vecums)
# print(pilseta)
# print(atzime)

#5. Korteža šķēlēšana ------------------------------------------------------------------

# skaitli = (10, 20, 30, 40, 50, 60, 70)
# print(skaitli[:3])
# print(skaitli[4:])
# print(skaitli[::2])
# print(skaitli[::-1])

#6. Korteža pārveidošana ---------------------------------------------------------------

# augli = ("ābols", "banāns", "ķirsis")
# saraksts = list(augli)
# saraksts.append("apelsīns")
# augli = tuple(saraksts)
# print(augli)

#7. Divu kortežu apvienošana -----------------------------------------------------------

# a = (1, 2, 3)
# b = (4, 5, 6)
# apvienot = a + b
# atkartot = apvienot * 2
# print(apvienot)
# print(atkartot)

#8. Koordinātu attālums ----------------------------------------------------------------

# import math

# A = (2, 3)
# B = (6, 6)
# attalums = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

# print(attalums)

#9. Lielākā vērtība kortežu sarakstā ---------------------------------------------------

# studenti = [("Anna", 9), ("Jānis", 7), ("Laura", 10), ("Pēteris", 8)]
# maks = max(studenti, key=lambda s: s[1])

# vards, atzime = maks
# print(vards, atzime)

#10. Temperatūras analīze --------------------------------------------------------------

# temperaturas = (12, 15, 14, 18, 20, 17, 13)
# videja = sum(temperaturas) // len(temperaturas)
# maks = max(temperaturas)
# indekss = temperaturas.index(maks)
# diena = sum(1 for t in temperaturas if t > 15)

# print(videja)
# print(maks)
# print(indekss)
# print(diena)

# SET ==================================================================================

#1. Kopas izveidošana ------------------------------------------------------------------

# kopa = {1, 2, 3, 3, 4, 4, 5}

# print(kopa)
# print(len(kopa))

#2. Elementu pievienošana --------------------------------------------------------------

# skaitli = {10, 20, 30}
# skaitli.add(40)
# skaitli.add(50)
# skaitli.add(20)

# print(skaitli)

# # 20 nepievienojas otrreiz, tāpēc ka Python šo komandu ignorēja, jo kopām katrs elements ir unikāls.

#3. Elementu dzēšana --------------------------------------------------------------------

# augli = {"ābols", "banāns", "ķirsis", "apelsīns"}
# augli.remove("banāns")
# augli.discard("mango")

# print(augli)

#4. Kopu apvienojums ---------------------------------------------------------------------

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)
# print(A & B)
# print(A - B)
# print(A ^ B)

#5. Dublikātu noņemšana -------------------------------------------------------------------

# skaitli = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# rezultats = sorted(set(skaitli))

# print(rezultats)

#6. Kopīgie skolēni -----------------------------------------------------------------------

# matematika = {"Anna", "Jānis", "Laura", "Pēteris"}
# fizika = {"Anna", "Laura", "Marta", "Roberts"}
# print(matematika & fizika)
# print(matematika - fizika)
# print(matematika | fizika)

#7. Apakškopu pārbaude --------------------------------------------------------------------

# A = {1, 2}
# B = {1, 2, 3, 4, 5}
# apakskopa = A.issubset(B)
# virskopa = B.issuperset(A)

# print(apakskopa)
# print(virskopa)

#8. Unikālie burti -------------------------------------------------------------------------

# vards = input("Ievadi jūsu vārdu: ")
# burti = set(burts for burts in vards.lower() if burts.isalpha())

# print(sorted(burti))
# print(len(burti))

#9. Kopīgie elementi trīs kopās ------------------------------------------------------------

# A = {1, 2, 3, 4, 5}
# B = {3, 4, 5, 6, 7}
# C = {2, 3, 5, 7, 9}
# visas = A.intersection(B, C)
# vismaz = A.union(B, C)

# print(visas)
# print(vismaz)

#10. Aptaujas rezultātu analīze -------------------------------------------------------------

# python = {"Anna", "Jānis", "Laura", "Marta"}
# java = {"Jānis", "Pēteris", "Laura"}
# javascript = {"Anna", "Laura", "Roberts"}
# visas = python & java & javascript
# tikai = python - (java | javascript)
# vismaz = (python & java) | (python & javascript) | (java & javascript)
# skoleni = python | java | javascript
# skaits = len(skoleni)

# print(visas)
# print(tikai)
# print(vismaz)
# print(skaits)

#DICTIONARY ==================================================================================

#1. Vārdnīcas izveidošana --------------------------------------------------------------------

# students = {"vārds": "Jānis", "vecums": 18, "klase": 12, "atzime": 8}

# print(students["vārds"])
# print(students["vecums"])
# print(students["klase"])
# print(students["atzime"])

#2. Vērtību mainīšana ------------------------------------------------------------------------

# students = {"vards": "Anna", "vecums": 16, "atzime": 8}
# students["vecums"] = 17
# students["atzime"] = 9
# students["pilseta"] = "Rīga"

# print(students)

#3. Atslēgu un vērtību izvadīšana ------------------------------------------------------------

# cenas = {"maize": 2.0, "piens": 1.5, "siers": 3.5}
# print(list(cenas.keys()))
# print(list(cenas.values()))
# for prece, cena in cenas.items():
#     print(prece, cena)

#4. Preču cenu summa -------------------------------------------------------------------------

# cenas = {"maize": 2.0, "piens": 1.5, "siers": 3.5}
# summa = sum(cenas.values())
# videja = summa // len(cenas)
# prece = max(cenas, key=cenas.get)
# cena = cenas[prece]

# print(summa)
# print(videja)
# print(prece, cena)

#5. Vārdnīcas elementu dzēšana ---------------------------------------------------------------

# students = {"vards": "Jānis", "vecums": 18, "atzime": 7, "pilsēta": "Liepāja"}
# del students["pilsēta"]
# skola = "skola" in students

# print(skola)
# print(students)

#6. Skolēnu atzīmes --------------------------------------------------------------------------

# atzimes = {"Anna": 9, "Jānis": 7, "Laura": 10, "Pēteris": 6, "Marta": 8}
# videja = sum(atzimes.values()) / len(atzimes)
# maks = max(atzimes, key=atzimes.get)
# augst = atzimes[maks]
# vismaz = {vards: atzime for vards, atzime in atzimes.items() if atzime >= 8}

# print(videja)
# print(maks, augst)
# print(vismaz)

#7. Burtu biežuma skaitīšana -----------------------------------------------------------------

# teksts = input("Ievadi tekstu: ")
# skaits = {}
# for burts in teksts.lower():
#     if burts.isalpha():
#         skaits[burts] = skaits.get(burts, 0) + 1

# print(skaits)

#8. Divu vārdnīcu apvienošana ----------------------------------------------------------------

# A = {"a": 10, "b": 20}
# B = {"b": 30, "c": 40}
# apvienota = A.copy()
# for atslega, vertiba in B.items():
#     apvienota[atslega] = apvienota.get(atslega, 0) + vertiba

# print(apvienota)

#9. Ligzdota vārdnīca ------------------------------------------------------------------------

# studenti = {
#     "Anna": {"matematika": 9, "fizika": 8},
#     "Jānis": {"matematika": 7, "fizika": 6},
#     "Laura": {"matematika": 10, "fizika": 9}
# }
# videjais = {}
# for vārds, priekšmeti in studenti.items():
#     atzimes = priekšmeti.values()
#     videjais[vārds] = sum(atzimes) / len(atzimes)
# vards = max(videjais, key=videjais.get)
# maks = videjais[vards]
# matemātikas_atzīmes = [priekšmeti["matematika"] for priekšmeti in studenti.values()]
# matemātikas_vidējais = sum(matemātikas_atzīmes) / len(matemātikas_atzīmes)

# for vārds, vid in videjais.items():
#     print(f"- {vārds}: {vid}")

# print(f"\nSkolēns ar augstāko vidējo: {vards} ({maks})")
# print(f"Visu skolēnu matemātikas vidējais: {matemātikas_vidējais:.2f}")


