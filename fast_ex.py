import sys

sys.setrecursionlimit(10**6)


def mul(a, b, m):
    return ((a % m) * (b % m)) % m


def fast_ex(b, ex, m):
    if ex == 0:
        return 1
    tmp = fast_ex(b, ex // 2, m)
    res = mul(tmp, tmp, m)
    if ex % 2 == 1:
        res = mul(res, b, m)
    return res


b = int(input("Input base: "))
ex = int(input("Input exponent: "))
m = int(input("Input modulo: "))

print(fast_ex(b, ex, m))
