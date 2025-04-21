def print_table_row(
        q: int | None,
        r: int | None,
        y: int | None,
        a: int,
        b: int,
        y2: int,
        y1: int,
):
    print(f"{str(q).ljust(18)} | {str(r).ljust(18)} | {str(y).ljust(18)} | {
          str(a).ljust(18)} | {str(b).ljust(18)} | {str(y2).ljust(18)} | {
          str(y1).ljust(18)}")


a = int(input("Input a (The output will be a^-1 mod m): "))
m = int(input("Input m: "))

print(f"{"q".ljust(18)} | {"r".ljust(18)} | {
      "y".ljust(18)} | {"a".ljust(18)} | {"b".ljust(18)} | {
      "y2".ljust(18)} | {"y1".ljust(18)}")
print("-" * 20 * 7)

original_a = a

y2, y1 = 0, 1
a, b = m, a

print_table_row(None, None, None, a, b, y2, y1)

while b > 0:
    q, r = a // b, a % b
    y = y2 - q * y1
    a, b, y2, y1 = b, r, y1, y
    print_table_row(q, r, y, a, b, y2, y1)

y2 = (y2 + 2 * m) % m

print(f"The modulo inverse of ({original_a})^-1 mod {m} = {y2}")
print(
    f"a * a^-1 mod {m} = {original_a} * {y2} mod {m} = {original_a * y2 % m}")
