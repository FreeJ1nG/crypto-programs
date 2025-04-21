def miller_rabin_witness(n, a):
    """
    Perform a single Miller-Rabin witness test for base a and odd integer n > 2.
    Returns True if a is a witness to n's compositeness, False otherwise.
    """
    if n <= 2 or n % 2 == 0:
        raise ValueError("n must be an odd integer greater than 2")
    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False  # Not a witness

    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return False  # Not a witness
    return True  # a is a witness to n's compositeness

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter n (odd integer > 2): "))
    a = int(input("Enter base a (2 <= a <= n-2): "))
    if miller_rabin_witness(n, a):
        print(f"{a} is a witness to the compositeness of {n}.")
    else:
        print(f"{a} is not a witness; {n} may be prime.")