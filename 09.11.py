# tabula = [[0 for _ in range(9)] for _ in range(9)]

# for i in range(9):
#     for j in range(9):
#         tabula[i][j] = (i+j) % 3

# for i in range(9):
#     for j in range(9):
#         print(f'{tabula[i][j]:2}', end="")
#     print()


# der_nosacijums_1 = False
# der_nosacijums_2 = False
# der_nosacijums_3 = False
# der_nosacijums_4 = False
# der_nosacijums_5 = False
# cipari= '0124673896'
# burti_mazie = 'hsjknfihdyuknf'
# burti_lieli = burti_mazie.upper()


# parole = "1325fSE"

# garums = len(parole)
# if 8<=garums<=20:
#     der_nosacijums_1 = True

# der_skaits = 0
# for simbols in parole:
#     nosacijums = simbols in burti_mazie
#     nosacijums = nosacijums or simbols in burti_lieli
#     nosacijums = nosacijums or simbols in cipari
#     if nosacijums:
#         der_skaits += 1

# if der_skaits==len(parole):
#     der_nosacijums_2 = True

# skaits_lieli = 0
# skaits_mazie = 0
# skaits_cipari = 0
# for simbols in parole:
#     if simbols in burti_lieli:
#         skaits_lieli += 1
#     if simbols in burti_mazie:
#         skaits_mazie += 1
#     if simbols in cipari:
#         skaits_cipari += 1

# if skaits_lieli>0 and skaits_mazie>0 and skaits_cipari>0:
#     der_nosacijums_3 = True


# der_nosacijums_5 = True
# for i in range(len(parole)-2):
#     tekosais_simbols = parole[i]
#     nakamais_simbols1 = parole[i+1]
#     nakamais_simbols2 = parole[i+2]
#     if tekosais_simbols==nakamais_simbols1 and nakamais_simbols1==nakamais_simbols2:
#         if tekosais_simbols not in cipari:
#             der_nosacijums_5 = False

# print(der_nosacijums_1, der_nosacijums_2, der_nosacijums_3, der_nosacijums_4, der_nosacijums_5)
# der = der_nosacijums_1 and der_nosacijums_2 and der_nosacijums_3
# der = der and der_nosacijums_4 and der_nosacijums_5
# atbilde = 'YES' if der else 'NO'
# print(f'{atbilde}')

#=========================================================

# vards = 'KARTUPELIS'
# vards = 'Kurmis'

# while len(vards)>1:
#     jauns_vards = ''
#     for i in range(0, len(vards), 2):
#         jauns_vards += vards[i]
#     print(jauns_vards)
#     jauns_vards = jauns_vards[::-1]
#     print(jauns_vards)
#     vards = jauns_vards

#======================================================

rinda=[0]
print(rinda)

N=3
rinda.append(N)
print(rinda)

kopa = rinda[0]+rinda[1]
rinda.append(kopa)

grupu_skaits = kopa // 3
rinda.append(grupu_skaits)

jaunie_roboti = grupu_skaits * 5
rinda.append(jaunie_roboti)

parstradei = 0
rinda.append(parstradei)

gada_beigas = kopa + jaunie_roboti
rinda.append(gada_beigas)
#print(rinda)

tabula = []
tabula.append(rinda)

i=1
rinda=[]
rinda.append(tabula[i-1][2]-tabula[i-1][5])
rinda.append(tabula[i-1][4])
rinda.append(rinda[0]+rinda[1])
rinda.append(rinda[2]//3)
rinda.append(rinda[3]*5)
rinda.append(0)
rinda.append(rinda[2]+rinda[4]-rinda[5])
tabula.append(rinda)

i=2
rinda=[]
rinda.append(tabula[i-1][2]-tabula[i-1][5])
rinda.append(tabula[i-1][4])
rinda.append(rinda[0]+rinda[1])
rinda.append(rinda[2]//3)
rinda.append(rinda[3]*5)
rinda.append(0)
rinda.append(rinda[2]+rinda[4]-rinda[5])
tabula.append(rinda)

i=3
rinda=[]
rinda.append(tabula[i-1][2]-tabula[i-1][5])
rinda.append(tabula[i-1][4])
rinda.append(rinda[0]+rinda[1])
rinda.append(rinda[2]//3)
rinda.append(rinda[3]*5)
rinda.append(0)
rinda.append(rinda[2]+rinda[4]-rinda[5])
tabula.append(rinda)

i=4
rinda=[]
rinda.append(tabula[i-1][2]-tabula[i-1][5])
rinda.append(tabula[i-1][4])
rinda.append(rinda[0]+rinda[1])
rinda.append(rinda[2]//3)
rinda.append(rinda[3]*5)
rinda.append(0)
rinda.append(rinda[2]+rinda[4]-rinda[5])
tabula.append(rinda)

i=5
rinda=[]
rinda.append(tabula[i-1][2]-tabula[i-1][5])
rinda.append(tabula[i-1][4])
rinda.append(rinda[0]+rinda[1])
rinda.append(rinda[2]//3)
rinda.append(rinda[3]*5)
rinda.append(tabula[i-2][1])
rinda.append(rinda[2]+rinda[4]-rinda[5])
tabula.append(rinda)


for rrr in tabula:
    print(rrr)


