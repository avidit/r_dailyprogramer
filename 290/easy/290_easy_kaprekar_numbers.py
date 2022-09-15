def is_kaprekar(n):
    if n == 1:
        return True
    ns = str(n * n)
    for i in range(1, len(ns)):
        l, r = int(ns[:i]), int(ns[i:])
        if l == 0 or r == 0:
            continue
        if l + r == n:
            return True


def find_kaprekar(n1, n2):
    return list(filter(is_kaprekar, range(n1, n2)))


test_inputs = [(1, 50), (2, 100), (101, 9000)]
for a, b in test_inputs:
    print(find_kaprekar(a, b))
