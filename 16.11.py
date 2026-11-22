#VĀRDNĪCAS ===================================================

# skolens_1 = {"vards": "Anna", "vecums": 14, "klase": "8A"}
# skolens_2 = {"vards": "Jānis", "vecums": 15, "klase": "8B"}

# print(skolens_1["vards"])
# print(skolens_1["vecums"])
# print(skolens_1["klase"])
# print(skolens_2["vards"])
# print(skolens_2["vecums"])
# print(skolens_2["klase"])

#-------------------------------------------------------------

# valstis = {
#     "Latvija": "Rīga", 
#     "Lietuva": "Viļņa",
#     "Igaunija": "Tallina",
#     "Vācija": "Berlīne",
#     "Francija": "Parīze"
#     }

# print(valstis["Latvija"])
# print(valstis["Lietuva"])
# print(valstis["Igaunija"])
# print(valstis["Vācija"])
# print(valstis["Francija"])

#------------------------------------------------------------

# preces = {"piens": 1.10, "maize": 1.20, "sviests": 2.50, "siers": 3.40, "olas": 2.10}

# cena_1 = preces["piens"] * (1 + 10 /100)
# cena_2 = preces["maize"] * (1 + 10 /100)
# cena_3 = preces["sviests"] * (1 + 10 /100)
# cena_4 = preces["siers"] * (1 + 10 /100)
# cena_5 = preces["olas"] * (1 + 10 /100)

# print(cena_1)
# print(cena_2)
# print(cena_3)
# print(cena_4)
# print(cena_5)

#-------------------------------------------------------------

# tulkojumi = {
#     "dog": "suns",
#     "cat": "kaķis",
#     "house": "māja",
#     "tree": "koks",
#     "book": "grāmata"
# }

# vards = input("Ievadi vārdu: ")
# if vards in tulkojumi:
#     print(f'{vards} eksistē')
#     print(tulkojumi.keys())
#     print(tulkojumi.values())
# else:
#     print(f'{vards} neeksistē')

# for anglu, latviesu in tulkojumi.items():
#     print(anglu, latviesu)

#-------------------------------------------------------

# teksts = "Pieauguša mājas kaķa vidējais kopējais garums (no deguna gala līdz astes galam) ir aptuveni 50 centimetri. Kaķenes parasti ir nedaudz mazākas nekā runči, lai gan izmēru atšķirības galvenokārt ir atkarīgas no šķirnes. Saskaņā ar Ginesa rekordu grāmatu, garākais reģistrētais mājas kaķis sasniedza 121,9 centimetru garumu.[3] Pasaulē garākā reģistrētā mājas kaķa aste ir bijusi 46,99 centimetrus gara.[4] Atšķirībā no suņiem, kaķiem nav izteiktu punduršķirņu, tomēr dažām šķirnēm (piemēram, Munchkin) ir raksturīga ģenētiska pundurība."
# saraksts = teksts.split()
# print(saraksts)
# skaits = {}
# for vards in saraksts:
#     if vards in skaits.keys():
#         skaits[vards]+= 1
#     else:
#         skaits[vards]=1

# print(skaits)

#--------------------------------------------------------

# atzimes = {
#     "Anna": 8,
#     "Jānis": 6,
#     "Laura": 9,
#     "Mārtiņš": 7,
#     "Elīna": 10
# }
# videjo = sum(atzimes.values()) / len(atzimes)
# print(videjo)

# print({vards: atzime for vards, atzime in atzimes.items() if atzime >= 7})

#---------------------------------------------------------

# vardnica_1 = {"piens": 1.10, "maize": 1.20, "sviests": 2.50}
# vardnica_2 = {"siers": 3.40, "jogurts": 0.90}

# apvienota = vardnica_1 | vardnica_2
# # apvienota = vardnica_1.copy()
# # for atslega, vertiba in vardnica_2.items():
# #     apvienota[atslega] = apvienota.get(atslega, 0) + vertiba
# print(apvienota)

# maks = max(apvienota.keys())
# print(maks)

#--------------------------------------------------------------

# skoleni = [
#     ("Anna", "8A"),
#     ("Jānis", "8B"),
#     ("Laura", "8A"),
#     ("Mārtiņš", "8C"),
#     ("Elīna", "8B"),
# ]

# vardnica = {}
# for vards, klase in skoleni:
#     if klase in vardnica:
#         vardnica[klase].append(vards)
#     else:
#         vardnica[klase] = []
#         vardnica[klase].append(vards)

# print(vardnica)

#----------------------------------------------

# teksts = "Pieauguša mājas kaķa vidējais kopējais garums (no deguna gala līdz astes galam) ir aptuveni 50 centimetri."
# lll = list(teksts)

# skaits = {}
# for simbols in lll:
#     if simbols in skaits.keys():
#         skaits[simbols] += 1
#     else:
#         skaits[simbols] = 1

# kopa = len(lll)
# print("Kopējais simbolu skaits:", kopa)
# print()

# for simbols, reizes in skaits.items():
#     relativais = reizes / kopa
#     procenti = relativais * 100
#     print(f"Simbols '{simbols}', Absolūtais skaits {reizes}, Relatīvais biežums {relativais:.3f} ({procenti:.1f}%)")

#------------------------------------------------

# tests_1  = {"Anna": 7, "Jānis": 6, "Laura": 8, "Mārtiņš": 7, "Elīna": 9}
# tests_2  = {"Anna": 9, "Jānis": 6, "Laura": 7, "Mārtiņš": 8, "Elīna": 9}

# mainas = {
#     atslega: (tests_1[atslega], tests_2[atslega])
#       for atslega in tests_1.keys() & tests_2.keys()
#       if tests_1[atslega] != tests_2[atslega]
# }

# print(mainas)

#KOPAS ==========================================
#1.uzd. -----------------------------------------

# vards = input("Ievadi vārdu: ")

# dazadi_simboli = set(vards)
# skaits = len(dazadi_simboli)
# print(dazadi_simboli)
# print(skaits)

#2.uzd. -----------------------------------------

# teksts = input("Ievadi tekstu: ")

# dazadi_simboli = set(teksts)
# skaits = len(dazadi_simboli)
# print(dazadi_simboli)
# print(skaits)

#3.uzd. -----------------------------------------

# skaitli = input("Ievadi veselus skaitļus: ")

# dazadi_skaitli = set(skaitli)
# dazadi_skaitli = sorted(dazadi_skaitli)
# skaits = len(dazadi_skaitli)
# print(dazadi_skaitli)
# print(skaits)

#4.uzd. ------------------------------------------

# skaitlu_virkne = input("Ievadi veselus skaitļus: ")
# skaitlis = input("Ievadi skaitlis: ")

# if skaitlis in skaitlu_virkne:
#     print("YES")
# else:
#     print("NO")

#5.uzd. -----------------------------------------

# A = {1, 2, 3, 4, 5}
# B = {3, 4, 5, 6, 7}

# visi = (A | B)
# skelums = (A & B)
# starpiba = (A - B)

# print("Union: ", visi)
# print("Intersection: ", skelums)
# print("Difference: ", starpiba)

#6.uzd. ------------------------------------------

# A = {2, 3}
# B = {1, 2, 3, 4, 5}

# if A.issubset(B):
#     print("YES")
# else:
#     print("NO")

#7.uzd. ------------------------------------------

# vards_1 = input("Ievadi pirmo vārdu: ")
# vards_2 = input("Ievadi otro vārdu: ")

# skelums = set(vards_1) & set(vards_2)
# for skelums in sorted(skelums):
#     print(skelums)

#8.uzd. ------------------------------------------

# vards = input("Ievadi vārdu: ")

# burti = set(vards)
# skaits = len(burti)
# print(burti)
# print(skaits)

#9.uzd. ------------------------------------------

# vards = input("Ievadi vārdu: ")

# patskani = {"a", "e", "i", "o", "u"}
# skaits = set(vards)

# if patskani.issubset(skaits):
#     print("YES")
# else:
#     print("NO")

#10.uzd. ----------------------------------------

# teikums = "Šis ir tests un šis ir tikai tests".lower()

# vardi = [vards for vards in teikums.split()]
# unikali_vardi = set(vardi)
# skaits = len(unikali_vardi)
# print(unikali_vardi)
# print(skaits)

#11.uzd. ----------------------------------------

# faila_nosaukums = input("Ievadi faila nosaukumu: ").strip()

# unikali_skaitli = set()
# with open(faila_nosaukums, "r", encoding="utf-8") as fails:
#     for rinda in fails:
#         rinda = rinda.strip()
#         if rinda:
#             unikali_skaitli.add(int(rinda))

# print(len(unikali_skaitli))

