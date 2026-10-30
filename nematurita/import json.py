
import json
dzejson = json.load(open("/home/polonec/Downloads/effectiveness.json", 'r', encoding='cp1250'))
typy = {'supereffective': 2, 'not_effective': 0.5, 'no_effect': 0, 'normale': 1}
mia = {}
for type1 in dzejson['supereffective']:     
    mia[type1] = {}
    for type2 in dzejson['supereffective'][type1]:
        mia[type1][type2] = typy['supereffective']


for type1 in dzejson['not_effective']:
    for type2 in dzejson['not_effective'][type1]:
        mia[type1][type2] = typy['not_effective']
        

for type1 in dzejson['no_effect']:
    for type2 in dzejson['no_effect'][type1]:
        mia[type1][type2] = typy['no_effect']
        
 
for type1 in dzejson['normale']:
    for type2 in dzejson['normale'][type1]:
        mia[type1][type2] = typy['normale']

print(mia)

for strenght in dzejson:
    for attacker in dzejson[strenght]:
        if not attacker in mia:
            mia[attacker] = ()
        for defender in dzejson[strenght][attacker]:
            mia[attacker][defender] = typy[strenght]

def attack(n1: int, n2: int, army : str) -> tuple:
    zoz_pok = army.split(',')
    myarmy= zoz_pok[:n1:]
    enemyarmy= zoz_pok[n1::]
    print(myarmy, enemyarmy)
attack(2,2,'fire,water,grass,electric')