p = int(input("Enter the prime modulus (p): "))  
g = int(input("Enter the primitive root modulo p (g): "))  

x = int(input("Enter the private key for the first person (x): "))  
A = pow(g, x, p)  
print(f"First person's public key (A): {A}\n")

y = int(input("Enter the private key for the second person (y): "))  
B = pow(g, y, p)  
print(f"Second person's public key (B): {B}\n")

shared_secret_first_person = pow(B, x, p)  
shared_secret_second_person = pow(A, y, p) 

print(f"Shared secret computed by the first person: {shared_secret_first_person}")
print(f"Shared secret computed by the second person: {shared_secret_second_person}\n")

assert shared_secret_first_person == shared_secret_second_person, "Shared secrets do not match!"