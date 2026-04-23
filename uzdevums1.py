import sqlite3

def savienot():
    conn = sqlite3.connect('biblioteka.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS biblioteka (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT,
            autors TEXT,
            gads INTEGER
        )
    ''')
    conn.commit()
    return conn, cursor

def pievienot(cursor, conn, nosaukums, autors, gads):
    cursor.execute('INSERT INTO biblioteka (nosaukums, autors, gads) VALUES (?, ?, ?)',
                   (nosaukums, autors, gads))
    conn.commit()

def melet_pec_autora(cursor, autors):
    print(f'\n Grāmatas, ko sarakstījis {autors}')
    cursor.execute('SELECT * FROM biblioteka WHERE autors = ?', (autors,))
    rezultati = cursor.fetchall()
    for k in rezultati:
        print(f'ID: {k[0]} | {k[1]} ({k[3]})')

def jaunas_gramatas(cursor):
    print('\n Grāmatas, kas izdotas pēc 2000. gada')
    cursor.execute('SELECT * FROM biblioteka WHERE gads > 2000')
    rezultati = cursor.fetchall()
    for k in rezultati:
        print(f'ID: {k[0]} | {k[1]} | Autors: {k[2]} | Gads: {k[3]}')

def sakartot_pec_gada(cursor):
    print('\n Visas grāmatas hronoloģiskā secībā')
    cursor.execute('SELECT * FROM biblioteka ORDER BY gads')
    rezultati = cursor.fetchall()
    for k in rezultati:
        print(f'Gads: {k[3]} | Nosaukums: {k[1]} | Autors: {k[2]}')

# Galvenā programma
conn, cursor = savienot()

cursor.execute('SELECT COUNT(*) FROM biblioteka WHERE autors = "Jānis Joņevs"')
if cursor.fetchone()[0] == 0:
    pievienot(cursor, conn, "Jelgava 94", "Jānis Joņevs", 2013)
    pievienot(cursor, conn, "Tīģeris", "Jānis Joņevs", 2020)
    pievienot(cursor, conn, "Nāves ēnā", "Rūdolfs Blaumanis", 1899)
    pievienot(cursor, conn, "Straumēni", "Edvarts Virza", 1933)

melet_pec_autora(cursor, "Jānis Joņevs")
jaunas_gramatas(cursor)
sakartot_pec_gada(cursor)

conn.close()