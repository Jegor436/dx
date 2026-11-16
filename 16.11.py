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

teksts = "Pieauguša mājas kaķa vidējais kopējais garums (no deguna gala līdz astes galam) ir aptuveni 50 centimetri."
lll = list(teksts)
print(lll)