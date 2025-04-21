from polynomial import Polynomial


def corrected_divmod(a: Polynomial, b: Polynomial):
    if a == Polynomial([1, 0]) and b == Polynomial([1]):
        return Polynomial([1, 0]), Polynomial([0])
    return divmod(a, b)


def in_gf(p: Polynomial):
    return Polynomial([abs(int(t)) % 2 for t in p])


def fp(p: Polynomial | None, ljust_width=24):
    if p is None:
        return '--'.ljust(ljust_width)
    return str(p).ljust(ljust_width)


def print_table_row(
        q: Polynomial | None,
        r: Polynomial | None,
        y: Polynomial | None,
        a: Polynomial | None,
        b: Polynomial | None,
        y2: Polynomial | None,
        y1: Polynomial | None,
):
    print(f"{fp(q)} | {fp(r)} | {fp(y)} | {
          fp(a)} | {fp(b)} | {fp(y2)} | {fp(y1)}")


# Program to find a^-1(x) given a(x) and m(x)
# Such that a(x) * a^-1(x) = 1 (mod m(x))
a = Polynomial([1, 0, 1, 0, 1, 1])
m = Polynomial([1, 0, 0, 0, 0, 1, 1])
# a = Polynomial([1, 0, 0, 0, 0, 0, 1, 1])  # x^7+x+1
# m = Polynomial([1, 0, 0, 0, 1, 1, 0, 1, 1])  # x^8+x^4+x^3+x+1

original_a = a

print("a(x):", a)
print("m(x):", m)

y2, y1 = Polynomial(0), Polynomial(1)
a, b = m, a

print(f"{"q(x)".ljust(24)} | {"r(x)".ljust(24)} | {
      "y(x)".ljust(24)} | {"a(x)".ljust(24)} | {"b(x)".ljust(24)} | {
      "y2(x)".ljust(24)} | {"y1(x)".ljust(24)}")
print("-" * 24 * 7)

print_table_row(None, None, None, a, b, y2, y1)

while b != Polynomial(0):
    q, r = corrected_divmod(a, b)
    q, r = in_gf(q), in_gf(r)
    y = in_gf(y2 - q * y1)
    a, b, y2, y1 = b, r, y1, y
    print_table_row(q, r, y, a, b, y2, y1)

print(f"The modulo inverse of a is: {y2}")
print(f"a(x) * a^-1(x) mod m(x) = ({original_a}) * ({y2}) mod ({m}) =",
      in_gf((original_a * y2) % m))
