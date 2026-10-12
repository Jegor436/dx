#1. dzivnieku patversme -----------------------------------------------------------------

# class DzivniekuPatversme:
#     def __init__(self):
#         self.nosaukums = ""
#         self.dzivnieku_skaits = 0
#         self.pilseta = ""

#     def ievade(self):
#         self.nosaukums = input("Ievadiet patversmes nosaukums: ")
#         self.dzivnieku_skaits = int(input("Ievadiet dzīvnieku skaits: "))
#         self.pilseta = input("Ievadiet pilsētu: ")

#     def izdruka(self):
#         print(f'Patversme "{self.nosaukums}", atrodas {self.pilseta} ', end="")
#         print(f'un tajā ir {self.dzivnieku_skaits} dzivnieki.')

#     def parbaudi_vietu_skaitu(self):
#         if self.dzivnieku_skaits > 100:
#             print("Patversme ir pārpildīta")
#         else:
#             print("Patversmē vēl ir vietas")


# patversme = DzivniekuPatversme()
# patversme.ievade()
# patversme.izdruka()
# patversme.parbaudi_vietu_skaitu()

#2. majdzivnieki -----------------------------------------------------------------------

# class Majdzivnieks:
#     def __init__(self, vards, vecums, tips):
#         self.vards = vards
#         self.vecums = vecums
#         self.tips = tips

# class Suns(Majdzivnieks):
#     def __init__(self, vards, vecums, suga):
#         super().__init__(vards, vecums, 1)
#         self.suga = suga

#     def izdruka(self):
#         print(f'Suns (tips - {self.tips} vārdā {self.vards})', end="")
#         print(f'suga: {self.suga}, vecums: {self.vecums} gadi.')

# class Kakis(Majdzivnieks):
#     def __init__(self, vards, vecums, bariba):
#         super().__init__(vards, vecums, 2)
#         self.bariba = bariba

#     def izdruka(self):
#         print(f'Kaķis (tips - {self.tips} vārdā {self.vards})', end="")
#         print(f'barība: {self.bariba}, vecums: {self.vecums} gadi.')


# vards_suns = input("Ievadiet suņa vārdu: ")
# vecums_suns = input("Ievadiet suņa vecumu: ")
# suga_suns = input("Ievadiet suņa sugu: ")
# suns = Suns(vards_suns, vecums_suns, suga_suns)

# vards_kakis = input("Ievadiet kaķa vārdu: ")
# vecums_kakis = input("Ievadiet kaķa vecumu: ")
# bariba_kakis = input("Ievadiet kaķa mīļāko barību: ")
# kakis = Kakis(vards_kakis, vecums_kakis, bariba_kakis)

# suns.izdruka()
# kakis.izdruka()


#3. doktorats --------------------------------------------------------------------------

# class Doktorats:
#     def __init__(self):
#         self.nosaukums = ""
#         self.pacientu_skaits = 0

#     def ievade(self):
#         self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")
#         self.pacientu_skaits = int(input("Ievadiet doktorāta pacientu skaits: "))

#     def izvade(self):
#         print(f'Doktorāts {self.nosaukums} apkalpo {self.pacientu_skaits} pacientus.')


# doktorats = Doktorats()
# doktorats.ievade()
# doktorats.izvade()


#4. skolotaji ---------------------------------------------------------------------------

# class Skolotajs:
#     def __init__(self, skaits, tips):
#         self.skaits = skaits
#         self.tips = tips

# class Sakumskola(Skolotajs):
#     def __init__(self, uzvards, klase, skaits):
#         super().__init__(skaits, 1)
#         self.uzvards = uzvards
#         self.klase = klase

#     def izdruka(self):
#         print(f'Sākumskolas (tips - {self.tips})', end="")
#         print(f'skolotājs {self.uzvards} māca {self.skaits} stundas {self.klase} klasē.')

# class Vidusskola(Skolotajs):
#     def __init__(self, uzvards, prieksmets1, prieksmets2, skaits, skaits1, skaits2):
#         super().__init__(skaits, 3)
#         self.uzvards = uzvards
#         self.prieksmets1 = prieksmets1
#         self.prieksmets2 = prieksmets2
#         self.skaits1 = skaits1
#         self.skaits2 = skaits2

#     def aprekina(self):
#         self.skaits1 + self.skaits2

#     def izdruka(self):
#         print(f'Vidusskolas (tips - {self.tips})', end="")
#         print(f'skolotājs {self.uzvards} māca šādus priekšmetus: {self.prieksmets1} un {self.prieksmets2}, kopā {self.skaits1 + self.skaits2} stundas.')


# uzvards_sakumskola = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
# klase_sakumskola = input("Ievadiet skolotāja klasi: ")
# skaits_sakumskola = input("Ievadiet skolotāja stundu skaitu: ")
# sakumskola = Sakumskola(uzvards_sakumskola, klase_sakumskola, skaits_sakumskola)

# uzvards_vidusskola = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
# prieksmets1_vidusskola = input("Ievadiet pirmo pasniegto priekšmetu: ")
# skaits1_vidusskola = input("Ievadiet pirmā priekšmeta stundu skaitu: ")
# prieksmets2_vidusskola = input("Ievadiet otro pasniegto priekšmetu: ")
# skaits2_vidusskola = input("Ievadiet otrā priekšmeta stundu skaitu: ")
# vidusskola = Vidusskola(uzvards_vidusskola, prieksmets1_vidusskola, skaits1_vidusskola, prieksmets2_vidusskola, skaits2_vidusskola)


# sakumskola.izdruka()
# vidusskola.aprekina()
# vidusskola.izdruka()