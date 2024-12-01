import numpy as np
import math
from sympy import isprime

p = np.random.randint(0, 999999)
while(not(isprime(p)) and p % 4 != 3):
    p = np.random.randint(0, 999999)

q = np.random.randint(0, 999999)
while(not(isprime(q)) and q % 4 != 3):
    q = np.random.randint(0, 999999)

print(f"p: {p}, q: {q}")

N = p*q

print(f"N: {N}")

x = np.random.randint(0, 999999)
while(math.gcd(x, N) == 1):
    x = np.random.randint(0, 999999)

print(f"x: {x}")

x_list = []

x_bits = ""

x_bits += str(pow(x, 2, N) % 2)
x_list.append(pow(x, 2, N))

for i in range(1, 20000):
    x_list.append(pow(x_list[i-1], 2, N))
    x_bits += str(pow(x_list[i-1], 2, N) % 2)

print(x_bits)

#------------------------
#---TEST DŁUGIEJ SERII---
#------------------------
print("TEST DŁUGIEJ SERII")

licznik = 0
test_dlugiej_serii = True
liczniki = []

for i in range(1, len(x_bits)):
    if x_bits[i] == x_bits[i-1]:
        licznik += 1
    else:
        licznik = 0
    
    liczniki.append(licznik)

    if licznik >= 26:
        test_dlugiej_serii = False
        print("Ciąg bitów nie przeszedł testu długiej serii.")
        break

print(f"Najdłuższa seria: {max(liczniki)}")

if test_dlugiej_serii:
    print("Ciąg bitów przeszedł test długiej serii.")
    
#-----------------------------
#---TEST POJEDYNCZYCH BITÓW---
#-----------------------------
print("TEST POJEDYNCZYCH BITÓW")

licznik_jedynek = 0

for i in x_bits:
    if i == '1':
        licznik_jedynek += 1

if licznik_jedynek > 9725 and licznik_jedynek < 10275:
    print(f"Liczba bitów '1': {licznik_jedynek}\nCiąg bitów przeszedł test pojedynczych bitów.")
else:
    print(f"Liczba bitów '1': {licznik_jedynek}\nCiąg bitów nie przeszedł testu pojedynczych bitów.")

#-----------------------------
#---TEST SERII----------------
#-----------------------------
print("TEST SERII")

licznik = 0
liczniki_serii = {}

for i in range(6):
    liczniki_serii[i+1] = 0

for i in range(1, len(x_bits)):
    if x_bits[i] == x_bits[i-1]:
        licznik += 1
    else:
        if licznik > 5:
            liczniki_serii[6] += 1
        elif licznik == 0:
            continue
        else:
            liczniki_serii[licznik] += 1
        licznik = 0

for key, value in liczniki_serii.items():
   test_serii = True
   if key == 1 and (value < 2315 or value > 2685):
        test_serii = False 
   elif key == 2 and (value < 1114 or value > 1386):
        test_serii = False
   elif key == 3 and (value < 527 or value > 723):
        test_serii = False 
   elif key == 4 and (value < 240 or value > 384):
        test_serii = False 
   elif key == 5 and (value < 103 or value > 209):
        test_serii = False 
   elif key == 6 and (value < 103 or value > 209):
        test_serii = False 
   if test_serii:
        if key == 6:
            print(f"Długość serii: {key} i więcej \t Liczność występowania serii: {value} \t PASSED")
        else:
            print(f"Długość serii: {key} \t\t Liczność występowania serii: {value} \t PASSED")
   else:
        if key == 6:
            print(f"Długość serii: {key} i więcej \t Liczność występowania serii: {value} \t NOT PASSED")
        else:
            print(f"Długość serii: {key} \t\t Liczność występowania serii: {value} \t NOT PASSED")
    
#--------------------------------
#---TEST POKEROWY----------------
#--------------------------------
print("TEST POKEROWY")

segmenty = []
segmenty_wystapienia = {}

for i in range(0, len(x_bits)-4, 4):
    segmenty.append(x_bits[i:i+4])

for i in segmenty:
    if i in segmenty_wystapienia.keys():
        segmenty_wystapienia[i] += 1
    else:
        segmenty_wystapienia[i] = 1

suma = 0
for value in segmenty_wystapienia.values():
    suma += value ** 2

x = 16./5000. * suma - 5000

if x > 2.16 and x < 46.17:
    print(f"Wartość x: {x} \t Ciąg bitów przeszedł test pokerowy.")
else:
    print(f"Wartość x: {x} \t Ciąg bitów nie przeszedł testu pokerowego.")