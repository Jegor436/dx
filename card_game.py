file_path = r'c:\Users\User\OneDrive\Documents\playing_cards.txt'

#1.uzd ============================================================

# try:
#     with open(file_path, 'r', encoding='utf-8') as f:
#         saturs = f.read()
        
#     kartis = saturs.split()
#     kāravu_skaits = sum(1 for karta in kartis if '♢' in karta)
#     print(f"Kāravu kāršu skaits: {kāravu_skaits}")
# except FileNotFoundError:
#     print("Neizdevās atrast datni.")

#2.uzd ============================================================

# try:
#     with open(file_path, 'r', encoding='utf-8-sig') as f:
#         lines = f.read()

#     if len(lines) >= 7:
#         septitais_rindas_teksts = lines[6]
#         kartis = septitais_rindas_teksts.split()
        
#         kopējie_punkti = 0
#         for karta in kartis:
#             karta = karta.strip()
#             if not karta:
#                 continue
#             rangs = karta[:-1]
            
#             if rangs == 'A':
#                 vertiba = 1
#             elif rangs == 'J':
#                 vertiba = 11
#             elif rangs == 'Q':
#                 vertiba = 12
#             elif rangs == 'K':
#                 vertiba = 13
#             else:
#                 try:
#                     vertiba = int(rangs)
#                 except ValueError:
#                     print(f"Neizdevās apstrādāt kārti: '{karta}' (rangs: '{rangs}')")
#                     raise
                
#             kopējie_punkti += vertiba
            
#         print(f"Septītā spēlētāja kāršu punktu summa: {kopējie_punkti}")
#     else:
#         print("Datnē nav pietiekami daudz rindu.")

# except FileNotFoundError:
#     print("Neizdevās atrast datni.")

#3.uzd ==============================================================

# try:
#     with open(file_path, 'r', encoding='utf-8-sig') as f:
#         lines = f.read()

#     max_punkti = -1
#     labakais_spelu_rindas_numurs = -1
#     for ind, line in enumerate(lines):
#         kartis = line.split()
#         if not kartis:
#             continue
            
#         spēletāja_punkti = 0
#         for karta in kartis:
#             karta = karta.strip()
#             if not karta:
#                 continue
#             rangs = karta[:-1]
            
#             if rangs == 'A':
#                 vertiba = 250
#             elif rangs == 'J':
#                 vertiba = 20
#             elif rangs == 'Q':
#                 vertiba = 50
#             elif rangs == 'K':
#                 vertiba = 100
#             else:
#                 vertiba = int(rangs)
#             spēletāja_punkti += vertiba    
            
#         print(f"{ind + 1}. spēlētāja punktu summa: {spēletāja_punkti}")
        
#         if spēletāja_punkti > max_punkti:
#             max_punkti = spēletāja_punkti
#             labakais_spelu_rindas_numurs = ind + 1

#     print(f"\nSpēlētājs ar lielāko punktu summu ir **{labakais_spelu_rindas_numurs}. spēlētājs** ar **{max_punkti}** punktiem.")


# except FileNotFoundError:
#     print("Neizdevās atrast datni.")

