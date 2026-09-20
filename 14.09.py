

# 1.uzd "Taisnstūris"

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

# class Darbinieks:
#     def __init__(self, vards, alga):
#         self.vards = vards
#         self.alga = alga
#     def paradit(self):
#         print(f' Darbinieka vards: {self.vards}')
#         print(f' Darbinieka alga: {self.alga}')
# class Vaditajs(Darbinieks):
#     def __init__(self, vards, alga, nodala):
#         super().__init__(vards, alga)
#         self.nodala = nodala
#     def informacijaParVaditaju(self):
#         # print(f' Vadītāja vārds: {self.vards}')
#         # print(f' Vadītāja alga: {self.alga}')
#         super().paradit()
#         print(f' Vadītāja nodaļa: {self.nodala}')

# darbinieks = Darbinieks("Jānis", 1000)
# darbinieks.paradit()
# vaditajs = Vaditajs("Aija", 900, "policija")
# vaditajs.informacijaParVaditaju()


#3.uzd "Klase "Maks""

# class Maks:
#     def __init__(self, ipasnieks, nauda):
#         self.ipasnieks = ipasnieks
#         self.nauda = nauda

#     def pievienot(self, summa):
#         self.nauda += summa

#     def teret(self, summa):
#         if self.nauda >= summa:
#             self.nauda -= summa
#         else:
#             print("Nav naudas!")

#     def informacija(self):
#         print(f'Maka īpašnieks: {self.ipasnieks}')
#         print(f'Naudas daudzums: {self.nauda}')

# maka = Maks("Andris", 1000)
# print(f'Īpašnieks: {maka.ipasnieks}, summa={maka.nauda}')
# maka.pievienot(250)
# print(f'Īpašnieks: {maka.ipasnieks}, summa={maka.nauda}')
# maka.pievienot(500)
# print(f'Īpašnieks: {maka.ipasnieks}, summa={maka.nauda}')
# maka.teret(3000)
# print(f'Īpašnieks: {maka.ipasnieks}, summa={maka.nauda}')


#4.uzd "Klase "Trijstūris""

# import math
# class Trijsturis:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def perimetrs(self):
#         return self.a + self.b + self.c
#     def vaiEksiste(self):
#         if (self.a + self.b > self.c, self.a + self.c > self.b, self.b + self.c > self.a):
#             return True
#         else:
#             return False
#     def informacija(self):
#         eksiste = self.vaiEksiste()
#         print(f'Malas garumi: a={self.a}, b={self.b}, c={self.c}')
#         if eksiste:
#             print(f'Trijstūris eksistē. Tā perimetrs ir {self.perimetrs()}')
#         else:
#             print("Trijstūris neeksistē")

# trijsturis = Trijsturis(5, 7, 9)
# trijsturis.informacija()


#5.uzd "Klase "Produkts""

# class Produkts:
#     def __init__(self, nosaukums, cena, daudzums):
#         self.nosaukums = nosaukums
#         self.cena = cena
#         self.daudzums = daudzums

#     def informacija(self):
#         print(f'Produkta nosaukums: {self.nosaukums}')
#         print(f'Produkta cena: {self.cena}')
#         print(f'Produkta daudzums: {self.daudzums}')
#         print(f'Produkta kopējā vērtība: {self.kopejaCena()}')

#     def kopejaCena(self):
#         return self.cena * self.daudzums
#     def atlaide(self, procents):
#         self.cena = round (self.cena * (1 - procents / 100))

# produkts = Produkts("Bumbieri", 2.99, 3)
# produkts.informacija()

# print("Cena pēc atlaides: ")
# produkts.atlaide(40)
# produkts.informacija()


#6.uzd "Klase "Tests""

# class Tests:
#     def __init__(self, skolenaVards, punkti=0):
#         self.skolenaVards = skolenaVards
#         self.punkti = punkti

#     def pieskaitit(self, punkti):
#         self.punkti += punkti
#     def paradit(self):
#         print(f'Vārds: {self.skolenaVards}')
#         print(f'Punkti: {self.punkti}')
#     def rezultats(self):
#         if self.punkti >= 50:
#             print("Nokārtots")
#         else:
#             print("Nav nokārtots")

# tests = Tests("Ivars", 72)
# tests.rezultats()


#7.uzd "Klase "Divritenis""

# class Divritenis:
#     def __init__(self, marka, atrums=0):
#         self.marka = marka
#         self.atrums = atrums

#     def paatrinat(self, solis):
#         self.atrums += solis

#     def bremzet(self, solis):
#         self.atrums -= solis
#         if self.atrums > 0:
#             print(self.atrums)
#         else:
#             print("Velosipēds nekustas")
    
#     def paraditInfo(self):
#         print(f'Marka: {self.marka}')
#         print(f'Ātrums: {self.atrums} km/h')

# divritenis = Divritenis("Scott", 20)
# divritenis.paatrinat(5) 
# divritenis.paraditInfo()

# divritenis.bremzet(10)  
# divritenis.paraditInfo()


#8.uzd "Klases "Transports", "Auto" un "Motocikls""

# class Transports:
#     def __init__(self, marka):
#         self.marka = marka

#     def kusteties(self):
#         print("Transports kustas")

# class Auto(Transports):
#     def __init__(self, marka):
#         super().__init__(marka)

#     def kusteties(self):
#         print("Auto brauc")

# class Motocikls(Transports):
#      def __init__(self, marka):
#           super().__init__(marka)

#      def kusteties(self):
#         print("Motocikls brauc")

# transports = Transports("Transports")
# transports.kusteties()
# auto = Auto("BMW")
# auto.kusteties()
# motocikls = Motocikls("Kawasaki")
# motocikls.kusteties()


#9.1.uzd "Punkts un nogrieznis"

# import math
# class Punkts:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Linija:
#     def __init__(self, punkts1, punkts2):
#         self.punkts1 = punkts1
#         self.punkts2 = punkts2
        
#     def garums(self):
#         dx = self.punkts1.x - self.punkts2.x
#         dy = self.punkts1.y - self.punkts2.y
#         return math.sqrt(dx**2 + dy**2)

#     def vaiPieder(self, punkts):
#         attalums1 = math.sqrt((punkts.x - self.punkts1.x)**2 + (punkts.y - self.punkts1.y)**2)
#         attalums2 = math.sqrt((self.punkts2.x - punkts.x)**2 + (self.punkts2.y - punkts.y)**2)
#         return math.isclose(attalums1 + attalums2, self.garums())

# p1 = Punkts(2, 0)
# p2 = Punkts(0, 0)
# p3 = Punkts(5, 0)
# p4 = Punkts(2, 3)
# linija = Linija(p1, p2)

# print(f'Līnijas nogriežņa garums: {linija.garums()}')

# print(f'Vai punkts (2, 0) pieder nogrieznim? {linija.vaiPieder(p1)}')
# print(f'Vai punkts (0, 0) pieder nogrieznim? {linija.vaiPieder(p2)}')
# print(f'Vai punkts (5, 0) pieder nogrieznim? {linija.vaiPieder(p3)}')
# print(f'Vai punkts (2, 3) pieder nogrieznim? {linija.vaiPieder(p4)}')


#9.2.uzd "Klase "Bibliotēka""

# class Biblioteka:
#     def __init__(self):
#         self.gramatas = []

#     def pievienotGramatu(self, nosaukums):
#         self.gramatas.append(nosaukums)
#         print(f'Grāmata {nosaukums} ir pievienota.')

#     def iznemtGramatu(self, nosaukums):
#         if nosaukums in self.gramatas:
#             self.gramatas.remove(nosaukums)
#             print(f'Grāmata {nosaukums} izņemts no bibliotēkas.')
#         else :
#             print(f'Kļūda: Grāmata {nosaukums} netika atrasta.')

#     def paraditGramatas(self):
#         if not self.gramatas:
#             print("Bibliotēkā nav grāmatas.")
#         else:
#             print("Bibliotēkā esošās grāmatas:")
#             for gramata in self.gramatas:
#                 print(f' - {gramata}')

# biblioteka = Biblioteka()

# biblioteka.pievienotGramatu("Mērnieku laiki")
# biblioteka.pievienotGramatu("Nāves ēnā")
# biblioteka.pievienotGramatu("Straumēni")

# biblioteka.paraditGramatas()

# biblioteka.iznemtGramatu("Nāves ēnā")

# biblioteka.iznemtGramatu("Harijs Poters")

# biblioteka.paraditGramatas()

                
