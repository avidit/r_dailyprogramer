def reformat(it):
    return it.replace(":", "-").replace("..", "-").split("-")


def get_number(prev, seq):
    i = len(seq)
    num = int(str(prev)[:-i] + seq)
    return num if prev < num else num + 10**i


def get_sequence(prev, seq, inc=1):
    return range(prev, get_number(prev, seq) + 1, int(inc))


def solve(it):
    res = [0]
    seq = map(reformat, it.split(","))
    for item in seq:
        item[0] = get_number(res[-1], item[0])
        if len(item) == 1:
            res.append(item[0])
        else:
            res += get_sequence(*item)

    return " ".join(str(i) for i in res[1:])


input_data = ["1,3,7,2,4,1", "1-3,1-2", "1:5:2", "104-2", "104..02", "545,64:11"]


if __name__ == "__main__":
    for inp in input_data:
        print(solve(inp))
