

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

#...
                
