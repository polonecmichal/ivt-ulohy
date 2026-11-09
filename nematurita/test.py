import json

# Načítanie JSON súboru s efektívnosťou typov
dzejson = json.load(open("/home/polonec/Downloads/effectiveness(1).json", 'r', encoding='utf-8'))

def get_effectiveness(attacker_type: str, defender_type: str) -> float:
    """Vráti efektívnosť útočiacieho typu proti brániacemu sa typu."""
    attacker_type = attacker_type.capitalize()
    defender_type = defender_type.capitalize()
    
    # Overenie kategórií v JSON súbore
    if attacker_type in dzejson.get('supereffective', {}) and defender_type in dzejson['supereffective'][attacker_type]:
        return 2.0
    if attacker_type in dzejson.get('not_effective', {}) and defender_type in dzejson['not_effective'][attacker_type]:
        return 0.5
    if attacker_type in dzejson.get('no_effect', {}) and defender_type in dzejson['no_effect'][attacker_type]:
        return 0.0
    # Ak nie je špecifikované inak, štandardná efektívnosť je 1.0
    return 1.0

def calculate_team_power(my_army_str: str, enemy_army_str: str) -> float:
    """Spočíta celkovú útočnú silu jedného tímu proti druhému."""
    my_pokemons = [p.strip() for p in my_army_str.split(',')]
    enemy_pokemons = [p.strip() for p in enemy_army_str.split(',')]
    
    total_power = 0.0
    
    for my_poke in my_pokemons:
        # Rozdelenie typov pokémona (napr. "Psychic Dark" -> ['Psychic', 'Dark'])
        my_types = my_poke.split()  
        
        for enemy_poke in enemy_pokemons:
            enemy_types = enemy_poke.split()  # napr. "Ghost Ice"
            
            max_poke_power = 0.0
            
            # Ak má tvoj pokémon dva typy, vyberie sa ten silnejší útok (max)
            for m_type in my_types:
                current_attack_power = 1.0
                # Ak má nepriateľ dva typy, hodnoty sa vynásobia
                for e_type in enemy_types:
                    current_attack_power *= get_effectiveness(m_type, e_type)
                
                if current_attack_power > max_poke_power:
                    max_poke_power = current_attack_power
            
            total_power += max_poke_power
            
    return total_power

def atack(n1: int, n2: int, army: str) -> tuple:
    """
    Hlavná funkcia podľa zadania.
    Vrátí trojicu (f1, f2, S).
    """
    zoz_pok = [p.strip() for p in army.split(',')]
    
    # Prvých n1 pokémonov je prvý tím, zvyšných n2 je druhý tím
    my_team = ",".join(zoz_pok[:n1])
    enemy_team = ",".join(zoz_pok[n1:])
    
    f1 = round(calculate_team_power(my_team, enemy_team), 1)
    f2 = round(calculate_team_power(enemy_team, my_team), 1)
    
    if f1 > f2:
        s = "ME"
    elif f2 > f1:
        s = "FOE"
    else:
        s = "EQUAL"
        
    return (f1, f2, s)

# Príklad použitia:
# print(atack(2, 2, "Psychic Dark, Fire, Ghost Ice, Fairy Electric"))