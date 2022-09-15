# [It's super effective!](https://redd.it/5961a5)

## Description

In the popular Pokemon games all moves and Pokemons have types that determine how effective certain moves are against certain Pokemons. These work by some very simple rules, a certain type can be super effective, normal, not very effective or have no effect at all against another type. These translate respectively to 2x, 1x, 0.5x and 0x damage multiplication. If a Pokemon has multiple types the effectiveness of a move against this Pokemon will be the product of the effectiveness of the move to it's types.

## Formal Inputs & Outputs

### Input

The program should take the type of a move being used and the types of the Pokemon it is being used on.

#### Example inputs

    fire -> grass
    fighting -> ice rock
    psychic -> poison dark
    water -> normal
    fire -> rock

#### Output

The program should output the damage multiplier these types lead to.

##### Example outputs

    2x
    4x
    0x
    1x
    0.5x

#### Notes/Hints

Since probably not every dailyprogrammer user is an avid Pokémon player that knows the type effectiveness multipliers by heart here is a Pokémon type chart.

#### Bonus 1

Use the [Pokemon api](https://pokeapi.co/) to calculate the output damage. Like, `http://pokeapi.co/api/v2/type/fire/`

#### Bonus 2

Deep further into the api and give the multiplier for folowing

 fire punch -> bulbasaur
 wrap -> onix
 surf -> dwegong

_side note:_ the api replaces a space with a hypen `-`

#### Finally

Special thanks to [/u/Daanvdk](/u/Daanvdk) for posting the idea on [/r/dailyprogrammer_ideas](https://www.reddit.com/r/dailyprogrammer_ideas). If you also have a good idea, don't be afraid to put it over their.
