def vigenere(text, key, enc=True):
    key = (key * -(-len(text) // len(key)))[:len(text)]
    return ''.join(
        chr((ord(c) - 65 + (ord(k) - 65) * (1 if enc else -1)) % 26 + 65) if c.isalpha() else c
        for c, k in zip(text.upper(), key.upper())
    )

text = input("Enter plaintext: ")
key = input("Enter keyword: ")
print("Encrypted:", (encrypted := vigenere(text, key)))
print("Decrypted:", vigenere(encrypted, key, False))
