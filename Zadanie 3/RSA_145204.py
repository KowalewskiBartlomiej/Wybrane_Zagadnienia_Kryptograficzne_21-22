import random
import math
import numpy as np

def czy_pierwsza(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

p = np.random.randint(1, 100000)
while(not(czy_pierwsza(p))):
    p = np.random.randint(1, 100000)

q = np.random.randint(1, 100000)
while(not(czy_pierwsza(q))):
    q = np.random.randint(1, 100000)

print(f"p: {p}")
print(f"q: {q}")

#p = 31
#q = 19

n = p*q

print(f"n: {n}")

phi = (p-1)*(q-1)

print(f"phi: {phi}")

for i in range(3, phi):
  if czy_pierwsza(i) and math.gcd(i, phi) == 1:
    e = i
    break

print(f"e: {e}")

d = pow(e, -1, phi)

print(f"d: {d}")

klucz_publiczny = (e,n)
klucz_prywatny = (d,n)

print(f"klucz_prywatny: {klucz_prywatny}")
print(f"klucz_publiczny: {klucz_publiczny}")

wiadomość = "Test1234"

wiadomość_zaszyfrowana = []

for i in wiadomość:
    #print(int(ord(i)))
    c = pow(int(ord(i)), e, n)
    #print(c)
    wiadomość_zaszyfrowana.append(c)

wiadomość_odszyfrowana = ""

for i in range(len(wiadomość_zaszyfrowana)):
    m = pow(wiadomość_zaszyfrowana[i], d, n)
    #print(m)
    wiadomość_odszyfrowana+=chr(m)

print(wiadomość_odszyfrowana)