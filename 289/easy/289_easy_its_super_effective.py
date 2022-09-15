import requests
from operator import mul
from functools import reduce


POKEPI_URL = "http://pokeapi.co/api/v2/type/"
DAMAGES = {"no_damage_to": 0, "half_damage_to": 0.5, "double_damage_to": 2}


def parse_input(attack_string):
    attackers, defenders = attack_string.split(" -> ")
    defenders = set(defenders.split())
    return attackers, defenders


def get_data(attacker):
    url = "".join((POKEPI_URL, attacker))
    response = requests.get(url)
    return response.json()


def parse_damage_relations(attacker, defenders, data):
    output = dict.fromkeys(defenders, 1)
    damage_relations = data["damage_relations"]

    for damage_rel, multiplier in DAMAGES.items():
        damage_types = damage_relations[damage_rel]

        for damage_type in damage_types:
            if damage_type["name"] in defenders:
                output[damage_type["name"]] = multiplier

    return output


def get_damage(inp):
    attacker, defenders = parse_input(inp)
    data = get_data(attacker)
    multipliers = parse_damage_relations(attacker, defenders, data)
    multiplier = reduce(mul, multipliers.values())
    return "{} : {}x".format(inp, multiplier)


test_inputs = """fire -> grass
fighting -> ice rock
psychic -> poison dark
water -> normal
fire -> rock"""


for line in test_inputs.splitlines():
    print(get_damage(line))
