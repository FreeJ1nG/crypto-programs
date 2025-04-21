class ECC:
    def __init__(self, a, b, p):
        """
        Initialize the elliptic curve: y^2 = x^3 + ax + b (mod p)
        """
        self.a = a
        self.b = b
        self.p = p

        # Check if the curve is valid
        if (4 * a**3 + 27 * b**2) % p == 0:
            raise ValueError("Invalid curve parameters: discriminant is zero.")

    def is_on_curve(self, point):
        """
        Check if a point is on the curve.
        """
        if point is None:  # The point at infinity is on the curve
            return True
        x, y = point
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def point_add(self, p1, p2):
        print(f" >> point_add: p1={p1}, p2={p2}")
        """
        Add two points on the elliptic curve.
        """
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 and y1 != y2:
            return None  # Point at infinity

        if x1 == x2:
            # Point doubling
            m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p
        else:
            # Point addition
            m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        
        x3 = ((m**2 - x1 - x2) + 2 * self.p) % self.p
        y3 = ((m * (x1 - x3) - y1) + 2 * self.p) % self.p

        print(f" >> point_add: m={m}, x3={x3}, y3={y3}")

        return (x3, y3)

    def scalar_mult(self, k, point):
        """
        Perform scalar multiplication: k * point.
        """
        result = None  # Start with the point at infinity
        addend = point

        while k > 0:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1

        return result


# Example usage
if __name__ == "__main__":
    # Define the curve: y^2 = x^3 + ax + b (mod p)
    a = 9
    b = 17
    p = 23  # A prime number
    curve = ECC(a, b, p)

    # Define a base point (generator)
    g = (16, 5)
    assert curve.is_on_curve(g), "Base point is not on the curve."

    # Perform scalar multiplication
    k = 9
    point = curve.scalar_mult(k, g)
    print(f"{k} * {g} = {point}")