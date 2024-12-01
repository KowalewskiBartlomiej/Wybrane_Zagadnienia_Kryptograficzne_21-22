import numpy as np
from math import gcd
from sympy import isprime, is_primitive_root

n = np.random.randint(500, 10000)
while(not(isprime(n))):
    n = np.random.randint(500, 10000)

for i in range(3, n):
    if is_primitive_root(i, n):
        g = i
        break

print(f"n, g : {n}, {g}")

x = np.random.randint(500, 10000)
y = np.random.randint(500, 10000)

print(f"x: {x}")
print(f"y: {y}")

X = pow(g, x, n)
Y = pow(g, y, n)

print(f"X: {X}")
print(f"Y: {Y}")

Klucz_A = pow(Y, x, n)
Klucz_B = pow(X, y, n)

print(f"Klucz_A: {Klucz_A}")
print(f"Klucz_B: {Klucz_B}")