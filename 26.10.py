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













