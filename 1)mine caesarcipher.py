word = input('Enter a word: ')
key = int(input('Enter a key value: '))
encrypt = ''.join(chr((ord(c) + key - (65 if c.isupper() else 97)) % 26 + (65 if c.isupper() else 97)) for c in word)
decrypt = ''.join(chr((ord(c) - key - (65 if c.isupper() else 97)) % 26 + (65 if c.isupper() else 97)) for c in encrypt)
print(f'Encrypted text: {encrypt}\nDecrypted text: {decrypt}')
