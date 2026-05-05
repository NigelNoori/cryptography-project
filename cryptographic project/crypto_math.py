import random # Used just for generating initial random bits, not for crypto algorithms

def gcd(a, b):
    """Euclidean algorithm to find the greatest common divisor."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find modular inverse coefficients."""
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(e, phi):
    """Calculates the modular inverse of e modulo phi."""
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception("Modular inverse does not exist. e and phi are not coprime.")
    return x % phi

def mod_pow(base, exp, mod):
    """Manual Square-and-Multiply algorithm (base^exp) % mod."""
    result = 1
    base = base % mod
    while exp > 0:
        # If the current bit is 1, multiply the result by the current base
        if exp % 2 == 1:
            result = (result * base) % mod
        # Square the base and shift the exponent right by 1 bit
        exp = exp >> 1
        base = (base * base) % mod
    return result

def is_prime(n, k=5):
    """Manual Miller-Rabin primality test. k determines the accuracy of the test."""
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0: 
        return False

    # Find r and d such that n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Run the test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = mod_pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits, verbose=False):
    """Generates a prime number of the specified bit length."""
    if verbose:
        print(f"[SYS] Searching for a {bits}-bit prime number...")
    while True:
        # Generate random odd number
        p = random.getrandbits(bits)
        # Ensure the number has the exact bit length and is odd
        p |= (1 << bits - 1) | 1 
        if is_prime(p):
            if verbose:
                print(f"[SYS] Found prime!")
            return p