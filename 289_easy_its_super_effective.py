"""
https://redd.it/5961a5

Description

In the popular Pokemon games all moves and Pokemons have types that determine 
how effective certain moves are against certain Pokemons. These work by some 
very simple rules, a certain type can be super effective, normal, not very 
effective or have no effect at all against another type. These translate 
respectively to 2x, 1x, 0.5x and 0x damage multiplication. If a Pokemon has 
multiple types the effectiveness of a move against this Pokemon will be the 
product of the effectiveness of the move to it's types.

Formal Inputs & Outputs

Input

The program should take the type of a move being used and the types of the 
Pokemon it is being used on.

Example inputs
 fire -> grass
 fighting -> ice rock
 psychic -> poison dark
 water -> normal
 fire -> rock
Output

The program should output the damage multiplier these types lead to.

Example outputs
2x
4x
0x
1x
0.5x

Use the Pokemon api to calculate the output damage.
Like, http://pokeapi.co/api/v2/type/fire/
"""

import requests
from operator import mul
from functools import reduce


POKEPI_URL = 'http://pokeapi.co/api/v2/type/'
DAMAGES = {
    'no_damage_to': 0,
    'half_damage_to': 0.5,
    'double_damage_to': 2
}


def parse_input(attack_string):
    attackers, defenders = attack_string.split(' -> ')
    defenders = set(defenders.split())
    return attackers, defenders


def get_data(attacker):
    url = ''.join((POKEPI_URL, attacker))
    response = requests.get(url)
    return response.json()


def parse_damage_relations(attacker, defenders, data):
    output = dict.fromkeys(defenders, 1)
    damage_relations = data['damage_relations']

    for damage_rel, multiplier in DAMAGES.items():
        damage_types = damage_relations[damage_rel]
        
        for damage_type in damage_types:
            if damage_type['name'] in defenders:
                output[damage_type['name']] = multiplier

    return output


def get_damage(inp):
    attacker, defenders = parse_input(inp)
    data = get_data(attacker)
    multipliers = parse_damage_relations(attacker, defenders, data)
    multiplier = reduce(mul, multipliers.values())
    return "{} : {}x".format(inp, multiplier)


test_inputs = '''fire -> grass
fighting -> ice rock
psychic -> poison dark
water -> normal
fire -> rock'''


for line in test_inputs.splitlines():
    print get_damage(line)
