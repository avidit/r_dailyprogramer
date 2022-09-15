from itertools import permutations


test_grams = [
    "xxx + x81 = 9x4",
    "xxx + 5x1 = 86x",
    "xxx + 39x = x75",
    "xxx + xxx + 23x + 571 = xxx + x82",
    "xxx + xxx + xx7 + 212 = xxx + 889",
    "xxx + xxx + 1x6 + 142 = xxx + 553",
    "xxx + xxx + xxx + 4x1 + 689 = xxx + xxx + x5x + 957",
    "xxx + xxx + xxx + 64x + 581 = xxx + xxx + xx2 + 623",
    "xxx + xxx + xxx + x81 + 759 = xxx + xxx + 8xx + 462",
    "xxx + xxx + xxx + 6x3 + 299 = xxx + xxx + x8x + 423",
    "xxx + xxx + xxx + 58x + 561 = xxx + xxx + xx7 + 993",
]


def checksum(gram):
    lhs, rhs = gram.split(" = ")
    lhs = sum(int(n) for n in lhs.split(" + "))
    rhs = sum(int(n) for n in rhs.split(" + "))
    return lhs == rhs


def find_missing(gram):
    digits = list(range(1, 10)) * int((gram.count("+") + 2) / 3)
    [digits.remove(int(i)) for i in gram if i.isdigit()]
    return digits


def fill_a_gram(gram):
    perms = permutations(find_missing(gram))
    format = gram.replace("x", "{}")
    grams = (format.format(*perm) for perm in perms)
    return grams


def gram_it(test_gram):
    return next(gram for gram in fill_a_gram(test_gram) if checksum(gram))


for test_gram in test_grams:
    print(gram_it(test_gram))
