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

class Augs:
    def __init__(self, nosaukums, vecums, tips):
        self.nosaukums = nosaukums
        self.vecums = vecums
        self.tips = tips

class Koks(Augs):
    def __init__(self, nosaukums, vecums, augstums):
        super().__init__(nosaukums, vecums, 1)
        self.augstums = augstums

    def izdrukat(self):
        print(f'Koks (tips - {self.tips}) nosaukums: {self.nosaukums}', end="")
        print(f', augstums: {self.augstums}m, vecums: {self.vecums} gadi.')

class Zieds(Augs):
    def __init__(self, nosaukums, vecums, krasa):
        super().__init__(nosaukums, vecums, 2)
        self.krasa = krasa

    def izdrukat(self):
        print(f'Zieds (tips - {self.tips}) nosaukums: {self.nosaukums}', end="")
        print(f', zieda krāsa: {self.krasa}, vecums: {self.vecums} gads.')


nosaukums_koks = input("Ievadiet koka nosaukumu: ")
vecums_koks = input("Ievadiet koka vecumu: ")
augstums_koks = input("Ievadiet koka augstumu: ")
koks = Koks(nosaukums_koks, vecums_koks, augstums_koks)

nosaukums_zieds = input("Ievadiet zieda nosaukumu: ")
vecums_zieds = input("Ievadiet zieda vecumu: ")
krasa_zieds = input("Ievadiet zieda krāsu: ")
zieds = Zieds(nosaukums_zieds, vecums_zieds, krasa_zieds)

koks.izdrukat()
zieds.izdrukat()

