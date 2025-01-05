import numpy as np
letter_num = {chr(i): i - 97 for i in range(97, 123)}
num_to_letter = {v: k for k, v in letter_num.items()}

def mod_inverse(a, m):
    return next(i for i in range(1, m) if (a * i) % m == 1)

def matrix_mod_inverse(matrix, m):
    det = int(round(np.linalg.det(matrix))) % m
    adj = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % m
    return (mod_inverse(det, m) * adj) % m

def text_to_numbers(text): return [letter_num[c] for c in text]
def numbers_to_text(nums): return ''.join(num_to_letter[n % 26] for n in nums)

plain_text = input("Plain text: ").lower()
matrix = np.array([[int(input()) for _ in range(int(input("Cols: ")))] for _ in range(int(input("Rows: ")))])
modulus = 26

# Encryption
chunks = [plain_text[i:i+len(matrix)] + 'x' * (len(matrix)-len(plain_text[i:i+len(matrix)])) for i in range(0, len(plain_text), len(matrix))]
encrypted = ''.join(numbers_to_text((np.dot(matrix, text_to_numbers(chunk)) % modulus).flatten()) for chunk in chunks)
print("Encrypted:", encrypted)

# Decryption
matrix_inv = matrix_mod_inverse(matrix, modulus)
decrypted = ''.join(numbers_to_text((np.dot(matrix_inv, text_to_numbers(chunk)) % modulus).flatten()) for chunk in chunks)
print("Decrypted:", decrypted)

"""
Plain text: hello
Rows: 2
Cols: 2
2
3
Cols: 2
1
4 """