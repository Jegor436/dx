# orders = {
#     "Anna":12,
#     "Jānis":8,
#     "Laura":15,
#     "Mārtiņš":10,
#     "Elina":15,
#     "Roberts":7,
#     "Sofija":11,
#     "Kristaps":9,
# }

# print(orders)

# # orders.sort()
# # print(orders)


# klienti = list(orders.items())

# klienti.sort()
# print(klienti)

# def get_count(klients):
#     return klients[1]

# klienti.sort(key=get_count, reverse=True)
# print(klienti)

# print("TOP 3 klienti: ")
# for vards, skaits in klienti[:3]:
#     print(vards, skaits)

#----------------------------------------------

import csv
from decimal import Decimal

VIP_CODES = {'VIP20', 'VIP25'}

def nolasit_datus():
    with open('orders.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dati = list(reader)
    # print(dati)
    
    for i in range(len(dati)):
        dati[i]['Order_ID']=dati [i]['ï»¿Order ID']
        dati[i].pop('ï»¿Order ID')
        dati[i]['Unit Price']=float(dati[i]['Unit Price'])
        dati[i]['Qty']=int(dati[i]['Qty'])
        if dati[i]['Ship Days'] != '':
            dati[i]['Ship Days']=int(dati[i]['Ship Days'])
        else:
            dati[i]['Ship Days']=0

    return dati


def uzd_1(dati):
    maksajumi_1 = dict()
    sk = 0
    bezmaksas = 0
    for i in range(len(dati)):
        if dati[i]['Qty'] < 5:
            maksajumi_1[dati[i]['Order_ID']]= 3
        else:
            bezmaksas+=1
    print(maksajumi_1)
    kopa_maksat = sk * 3
    print(kopa_maksat)
    kopa_maksat1 = sum(maksajumi_1.values())
    print(kopa_maksat1)
    print(f'Bezmaksas piegade bija {bezmaksas} nosūtījumiem.')


def uzd_2(dati):
    nav_jamaksa_par_apstradi = []
    for i in range(len(dati)):
        if dati[i]['Discount Code'] in VIP_CODES:
            nav_jamaksa_par_apstradi.append(dati[i]['Order_ID'])
    print(nav_jamaksa_par_apstradi)  
    nav_jamaksa = len(nav_jamaksa_par_apstradi)
    maksat = len(dati) - nav_jamaksa
    print(maksat)

def kategorija(pasutijums):
    if pasutijums ['Discount Code'] in VIP_CODES:
        return"VIP"
    if pasutijums ['Discount Code'] == 'WELCOME5':
        return "Newcower"
    if pasutijums['Qty'] in (4, 5):
        return "Pro"
    return "Regular"


def uzd_3(dati):
    kategorijas = dict()
    for i in range(len(dati)):
        kategorijas[dati[i]['Order_ID']] = kategorija(dati[i])
    # print(kategorijas)
    kategoriju_skaits = dict()
    # for ieraksts in kategorijas:
    for ieraksts in kategorijas.values():
        print(ieraksts)
        if ieraksts in kategoriju_skaits.keys():
            kategoriju_skaits[ieraksts] += 1
        else:
            kategoriju_skaits[ieraksts] = 1
    print(kategoriju_skaits)


def uzd_4(dati):
    atmaksas_nosacijumi = []
    kam_atmaksat = []
    nosacijumu_vardnica = {'0':0, '1':0, '2':0, '3':0}
    for i in range(len(dati)):
        nosacijums1 = dati[i]['Discount Code'] in VIP_CODES
        nosacijums2 = dati[i]['Unit Price'] >= 50
        nosacijums3 = dati[i]['Status'] == 'Delivered'
        tris_nosacijumi = (nosacijums1, nosacijums2, nosacijums3)
        atmaksas_nosacijumi.append(tris_nosacijumi)
        summa = nosacijums1 + nosacijums2 + nosacijums3
        if summa ==1:
            kam_atmaksat.append(dati[i]['Order_ID'])
        nosacijumu_vardnica[str(summa)] += 1
    # print(atmaksas_nosacijumi)
    print(f'Kopējais atmaksas summa ir {len(kam_atmaksat)}')
    print(nosacijumu_vardnica)


def uzd_5(dati):
    EU = {'France', 'Germany', 'Italy', 'Netherlands', 'Poland', 'Spain'}
    valsti_sodi = dict()
    for valsts in EU:
        valsti_sodi[valsts] = [0,0]
        print(valsti_sodi)
    for i in range(len(dati)):
        piegade = dati[i]['Ship_Days']>=5
        valsts = dati[i]['Country'] in EU
        status_1 = dati[i]['Status'] == 'Delivered'
        status_2 = dati[i]['Status'] == 'Returned'
        if status_1 and piegade and valsts:
            sods = 10
        if status_2 and valsts:
            sods = 50
        valsts_sodi[dati[i]['Country']]['sods'] += sods
        valsts_sodi[dati[i]['Country']]['pas_skaits'] += 1

    print(valsti_sodi)
    for valsts, ieraksts in valsti_sodi.items():
        ieraksts_list = list(ieraksts.values())
        print(valsts, ieraksts, ieraksts_list)
        valsti_sodi[valsts] = ieraksts_list

    print(valsti_sodi)

    valstis1 = list(valsti_sodi.items())
    print(valstis1)
    
    def get_sods(valsts):
        return valsts[1][0]

    valstis1.sort(key=get_sods, reverse=True)
    print(valstis1)

    print(f'Lielaka soda summa: {valstis1[0][0]}, pasutijumu skaits ar sodu: {valstis1[0][1][1]}')


    pass







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dati = nolasit_datus()
print(dati)

uzd_1(dati)
uzd_2(dati)
uzd_3(dati)
uzd_4(dati)
uzd_5(dati)


