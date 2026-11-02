# tabula = [[0 for _ in range(10)] for _ in range(10)]
# # print(tabula)
# for i in range(10):
#     tabula[i][i] = 1
#     tabula[i][i] = 1



# # tabula[2][1] = '+'

# # tabula[3][1] = '+'
# # tabula[3][2] = '+'

# # tabula[4][1] = '+'
# # tabula[4][2] = '+'
# # tabula[4][3] = '+'


# for i in range(2, 10):
#     for j in range(1, 9):
#         # tabula[i][j] = '+'
#         tabula[i][j] = tabula[i-1][j] + tabula[i-1][j-1]


# # for rinda in tabula:
# #     print(rinda)

# for i in range(10):
#     for j in range(10):
#         print(f'{tabula[i][j]:4}', end="")
#         print()


sorobans = [['-' for _ in range(13)] for _ in range(10)]

for j in range(13):
    sorobans[1][j]='o'
    sorobans[2][j]='o'
    sorobans[3][j]='|'
    sorobans[4][j]='|'
    sorobans[5][j]='o'
    sorobans[6][j]='o'
    sorobans[7][j]='o'
    sorobans[8][j]='o'

for i in range(10):
    for j in range(13):
        print(f'{sorobans[i][j]:2}, end=''')
        print()

kolonna = 12
skaitlis = int(input("Ievadi skaitli: "))
while skaitlis!=0:
    cipars = skaitlis % 10
    #print(cipars)
    skaitlis = skaitlis // 10
    if cipars >= 5:
        leja = 1
        pacelt_augsa = cipars % 5
    else:
        leja = 0
        pacelt_augsa = cipars
    if leja == 1:
        sorobans[1][kolonna]='|'
        sorobans[2][kolonna]='o'
    for i in range(pacelt_augsa):
        sorobans[i+4][kolonna]='o'
        sorobans[pacelt_augsa+4][kolonna]='|'
        kolonna -= 1

for i in range(10):
    for j in range(13):
        print(f'{sorobans[i][j]:2}, end=''')
        print()



