from polynomial import Polynomial as P


def in_gf(p: P):
    return GFPolynomial([abs(int(t)) % 2 for t in p])


class GFPolynomial(P):
    def __mul__(self, other):
        return in_gf(super().__mul__(other))

    def __sub__(self, other):
        return in_gf(super().__sub__(other))

    def __mod__(self, other):
        return in_gf(super().__mod__(other))

    def __add__(self, other):
        return in_gf(super().__add__(other))

    def __divmod__(self, other):
        q, r = super().__divmod__(other)
        return in_gf(q), in_gf(r)

    def __floordiv__(self, other):
        return in_gf(super().__floordiv__(other))


a = GFPolynomial([1, 0, 0, 0, 0, 0])
b = GFPolynomial([1, 0, 1])
m = GFPolynomial([1, 0, 0, 0, 0, 1, 1])
print((a * b) % m)
