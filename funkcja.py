import random
import sqlite3
def create_name(dlzka):
    samo = 'aeiou'
    spolu = 'bcdfghjklmnopqrstvwxyz'
    temp = ''
    for i in range(dlzka):
        if random.choice([True, False]):
            temp += random.choice(spolu)
        else:
            temp += random.choice(spolu)
    return temp.capitalize()
print(create_name(5))
conn = sqlite3.connect('pokusna.db')
pokusna = sqlite3.Cursor(conn)
print("INSERT INTO studenti (meno, priezvisko, vek, noha, oci) VALUES ('"+create_name(random.randint(3,10))+"','"+create_name(5)+"','"+random.randint(18,25)+'","'+random.randint(36,42)+'","'+random.randint(36,42)+'",?)", random.choice(['modre', 'zelene', 'cirene'])))
