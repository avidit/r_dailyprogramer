rules = {
    "white": [False, ["white", "black"]],
    "red": [True, ["green"]],
    "black": [False, ["white", "green", "orange"]],
    "orange": [True, ["red", "black"]],
    "green": [True, ["orange", "white"]],
    "purple": [False, ["purple", "green", "orange", "white"]],
}


def defuse_bomb(wires):
    state = "Bomb Defused"
    for i, wire in enumerate(wires[:-1]):
        print(wire)
        if rules[wire][0] != (wires[i + 1] in rules[wire][1]):
            state = "Boom"
    return state


if __name__ == "__main__":
    print(defuse_bomb(["white", "red", "green", "white"]))
    print(defuse_bomb(["white", "orange", "green", "white"]))
