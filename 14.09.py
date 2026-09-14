#1.uzd

# class Kvadrats:
#     def __init__(self, mala):
#         self.mala = mala
#     def laukums(self):
#         return self.mala**2
#     def perimetrs(self):
#         return self.mala*4
#     def informacija(self):
#         print(f'Malas garums: {self.mala}')
#         print(f'Laukums: {self.laukums()}')
#         print(f'Perimetrs: {self.perimetrs()}')


# # -------------------------------
# kvadrats = Kvadrats(5)
# print(f'Kvadrata ar malas garumu {kvadrats.mala}', end= " ")
# print(f' S = {kvadrats.laukums()}, perimetrs = {kvadrats.perimetrs()}')
# kvadrats.informacija()
        



# 2.uzd

# class Persona:
#     def __init__(self, vards, vecums):
#         self.vards = vards
#         self.vecums = vecums
#     def attelot(self):
#         print(f'Vārds: {self.vards}')
#         print(f'Vecums: {self.vecums}')

# class Skolens(Persona):
#     def __init__(self, vards, vecums, klase):
#         super().__init__(vards, vecums)
#         self.klase = klase
#     def informacijaParSkolenu(self):
#         print(f'Vārds: {self.vards}')
#         print(f'Vecums: {self.vecums}')
#         print(f'Klase: {self.klase}')
#         super().attelot()

# persona = Persona("Anna", 30)
# persona.attelot() 

# skolens = Skolens("Mareks", 16, "10.a")
# skolens.informacijaParSkolenu()



#3.uzd

# class BankasKonts:
#     def __init__(self, kontsNumurs, ipasnieks, bilance):
#         self.kontsNumurs = kontsNumurs
#         self.ipasnieks = ipasnieks
#         self.bilance = bilance
#     def iemaksa(self, summa):
#         self.bilance += summa
#     def izmaksa(self, summa):
#         if self.bilance>= summa:
#             self.bilance -= summa
#         else:
#             print('Trūks naudas :(')

#     def parskaitit(self, summa):
#         if self.bilance + summa * 0.05>= summa:
#             self.bilance -= summa
#             self.bilance -= summa*0.05
#         else:
#             print('Trūks naudas :(')


# konts = BankasKonts("LV123456", "Anna Ozola", 100)
# print(f'Konta īpašniece: {konts.ipasnieks}, summa= {konts.bilance}')
# konts.iemaksa(1000)
# print(f'Konta īpašniece: {konts.ipasnieks}, summa= {konts.bilance}')
# konts.izmaksa(500)
# print(f'Konta īpašniece: {konts.ipasnieks}, summa= {konts.bilance}')
# konts.izmaksa(100)


#4.uzd

# import math
# class Aplis:
#     def __init__(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.r = r

#     def laukums(self):
#         return math.pi * self.r **2
#     def rinkaLinijasGarums(self):
#         return 2*math.pi*self.r
#     def vaiPieder(self, x0, y0):
#         pieder = (x0-self.x)**2+(y0- self.y)**2 <= self.r**2
#         return pieder

# aplis = Aplis(0,0,5)
# print(f'Laukums={aplis.laukums()}')
# print(f'Riņķa linijas garums={aplis.rinkaLinijasGarums()}')
# x0 = 1
# y0 = 1
# vaiTeksa = aplis.vaiPieder(x0, y0)
# teksts = 'ir iekšā' if aplis.vaiPieder(x0, y0) else 'nav iekšā'
# print(f'Punkts: ({x0}, {y0}) {teksts} riņķī')


#5.uzd

# class Gramata:
#     def __init__(self, nosaukums, autors, cena):
#         self.nosaukums = nosaukums
#         self.autors = autors
#         self.cena = cena
#     def informacija(self):
#         print(f'Grāmatas nosaukums: {self.nosaukums}')
#         print(f'Grāmatas autors: {self.autors}')
#         print(f'Grāmatas cena: {self.cena}')
#     def atlaide(self, procenti):
#         self.cena = round(self.cena - self.cena*procenti / 100)
#         print(f'Jaunā grāmatas cena: {self.cena}')

# gramata = Gramata("Mežu dievs", "Liza Mora", 19.98)
# gramata.informacija()
# gramata.atlaide(50)        
         

#6.uzd

# class Spele:
#     def __init__(self, speletajaVards, punkti):
#         self.speletajaVards = speletajaVards
#         self.punkti = 0
#     def pieskaitit(self, punkti):
#         self.punkti += punkti
#     def paradit(self):
#         print("Speletajs:", self.speletajaVards)
#         print("Punkti:", self.punkti)

#     def parbauditRezultatu(self):
#         if self.punkti >= 100:
#             print("Uzvara!")
#         else:
#             print("Speles turpinajums")


#8.uzd

# class Dzivnieks:
#     def __init__(self, nosaukums):
#         self.nosaukums = nosaukums
#     def izdodSkanu(self):
#         print("Nezinama skaņa")
# class Suns(Dzivnieks):
#     def izdotSkanu(self):
#         print("Vau Vau")
# class Kakis(Dzivnieks):
#     def __init__(self, nosaukums, ipasnieks):
#         super().__init__(nosaukums)
#         ....


#9.uzd

# import math

# class Punkts:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Linija:
#     def __init__(self, punkts1, punkts2):
#         self.punkts1 = punkts1
#         self.punkts2 = punkts2
#     def nogrieznaGarums(self):
#         dx = self.punkts1.x - self.punkts2.x
#         dy = self.punkts1.y - self.punkts2.y
#         return math.sqrt(dx**2 + dy**2)

# class Trijsturis:
#     def __init__(self, A, B, C):
#         self.A = A
#         self.B = B
#         self.C = C

#     def perimetrs(self):
#         AB = Linija(self.A, self.B).nogrieznaGarums()
#         BC = Linija(self.B, self.C).nogrieznaGarums()
#         CA = Linija(self.C, self.A).nogrieznaGarums()
#         return AB + BC + CA 

#     def laukums(self):
#         AB = Linija(self.A, self.B).nogrieznaGarums()
#         BC = Linija(self.B, self.C).nogrieznaGarums()
#         CA = Linija(self.C, self.A).nogrieznaGarums()
#         p = (AB + BC + CA)/2
#         return math.sqrt(p*(p-AB)*(p-BC)*(p-CA)) 

#     def vaiPieder(self, punkts):
#         trijsturis1 = Trijsturis(self.A, self.B, punkts)
#         trijsturis2 = Trijsturis(self.B, self.C, punkts)
#         trijsturis3 = Trijsturis(self.C, self.A, punkts)
#         laukums1 = trijsturis1.laukums()
#         laukums2 = trijsturis2.laukums()
#         laukums3 = trijsturis3.laukums()
#         mazoLaukumuSumma = laukums1 + laukums2 + laukums3
#         lielaisLaukums = self.laukums()

#         return abs(mazoLaukumuSumma-lielaisLaukums)<0.00000001


        

# #----------------------------------------
# A = Punkts(0,0)
# B = Punkts(0,4)
# AB = Linija(A,B)
# print(AB.nogrieznaGarums())
# ABC = Trijsturis(A,B,C)
# print(f'Laukums: {ABC.laukums()}')
# print(f'Perimetrs: {ABC.perimetrs()}')

# punkts1 = Punkts(1,1)
# print(f'Punkts 1 pieder vai nē: {ABC.vaiPieder(punkts1)}')
# punkts2 = Punkts(1,10)
# print(f'Punkts 2 pieder vai nē: {ABC.vaiPieder(punkts2)}')



#1.uzd "Taisnstūris"

# class Taisnsturis:
#     def __init__(self, garums, platums):
#         self.garums = garums
#         self.platums = platums
#     def laukums(self):
#         return self.garums*self.platums
#     def perimetrs(self):
#         return self.garums*2 + self.platums*2
#     def informacija(self):
#         print(f'Garums: {self.garums}')
#         print(f'Platums: {self.platums}')
#         print(f'Laukums: {self.laukums()}')
#         print(f'Perimetrs: {self.perimetrs()}')

# taisnsturis = Taisnsturis(10,5)
# print(f' Taisnstūris ar garumu: {taisnsturis.garums}', end="")
# print(f' Taisnstūris ar platumu: {taisnsturis.platums}', end="")
# print(f' laukums ={taisnsturis.laukums()}, perimetrs ={taisnsturis.perimetrs()}')
# taisnsturis.informacija()


#2.uzd "Darbinieki"

class Darbinieks:
    def __init__(self, vards, alga):
        self.vards = vards
        self.alga = alga
    def paradit(self):
        print(f' Darbinieka vards: {self.vards}')
        print(f' Darbinieka alga: {self.alga}')
class Vaditajs(Darbinieks):
    def __init__(self, vards, alga, nodala):
        super().__init__(vards, alga)
        self.nodala = nodala
    def informacijaParVaditaju(self):
        # print(f' Vadītāja vārds: {self.vards}')
        # print(f' Vadītāja alga: {self.alga}')
        super().paradit()
        print(f' Vadītāja nodaļa: {self.nodala}')

darbinieks = Darbinieks("Jānis", 1000)
darbinieks.paradit()
vaditajs = Vaditajs("Aija", 900, "policija")
vaditajs.informacijaParVaditaju()
   
                