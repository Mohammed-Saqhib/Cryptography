def modinv(a, m):
    x0, x1 = 0, 1
    while a > 1: a, m, x0, x1 = m, a % m, x1 - (a // m) * x0, x0
    return x1 + m if x1 < 0 else x1

p, q, e = (int(input(f"Enter {x}: ")) for x in ["prime p", "prime q", "public exponent e"])
n, phi, d = p * q, (p - 1) * (q - 1), modinv(e, (p - 1) * (q - 1))

print(f"Public key: ({e}, {n})\nPrivate key: ({d}, {n})")
plaintext = input("Enter plaintext: ").upper()
encrypted = [pow(ord(c), e, n) for c in plaintext]
print("Encrypted:", encrypted, "\nDecrypted:", ''.join(chr(pow(c, d, n)) for c in encrypted))
