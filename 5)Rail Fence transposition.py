def rail_fence_cipher(text, key):
    rails, direction, row = [''] * key, 1, 0
    for c in text:
        rails[row] += c
        row += direction
        if row == 0 or row == key - 1: direction *= -1
    return ''.join(rails)

text = input("Enter plaintext: ")
key = int(input("Enter number of rails: "))
print("Encrypted text:", rail_fence_cipher(text, key))
