import random,sqlite3

connection = sqlite3.connect('/home/polonec/Documents/Ivt/pokusna')
cursor = connection.cursor()
cursor.execute("SELECT id FROM studenti")
vsetky_oci = [riadok[0] for riadok in cursor.fetchall()]
for i in range(5):
    student_id = i + 1
    nahodna_farba = random.choice(vsetky_oci)
    cursor.execute("UPDATE studenti SET INTEGER = ? WHERE id = ?", (nahodna_farba, student_id))
connection.close()