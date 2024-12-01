import random
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

#Podaj sekret:
sekret = 87562
#Podaj liczbę udziałów:
n = 8
#Podaj minimalną liczbę udziałów potrzebnych do odtworzenia sekretu: 
t = 4
#Podaj liczbę pierwszą:
p = None

poprawne = True
if t >= n:
   print("Liczba t powinna być mniejsza od całkowitej liczby udziałów.")
   poprawne = False

if poprawne:
  if (p=="" or p==None or not(czy_pierwsza(int(p)))):
      print("Podana liczba p nie jest liczbą pierwszą.")
      p = None

  if (p == None):
      p = np.random.randint(sekret + 1, 2 * sekret)
      while(not(czy_pierwsza(p))):
          p = np.random.randint(sekret + 1, 2 * sekret)

  print("p: ", p)
  
  wspolczynniki = []
  print("Współczynniki:")
  for i in range(t-1):
    wspolczynniki.append(random.randint(0, p))
    print("a_" + str(i+1) + " = " + str(wspolczynniki[i]))

  udzialy = []
  for i in range(n):
      udzial = 0
      for j in reversed(range(t-1)):
          udzial += ((i+1)**(j+1)*wspolczynniki[j])
      udzial += sekret
      print("Udział " + str(i+1) + ": " + str(udzial%p))
      udzialy.append((i+1, udzial%p))

  potrzebne_udzialy = random.sample(udzialy, k=t)

  print("Wybrane udzialy: ", potrzebne_udzialy)

  for i in range(t):
      print("Udział " + str(udzialy.index(potrzebne_udzialy[i])+1) + ": " + str(potrzebne_udzialy[i]))

  odtwarzany_sekret = 0
  for i in range(len(potrzebne_udzialy)):
      x = potrzebne_udzialy[i][0]
      y = 1
      for j in range(len(potrzebne_udzialy)):
          if j != i:
              xj = potrzebne_udzialy[j][0]
              y *= (xj * pow((xj - x), -1, p))
      y *= potrzebne_udzialy[i][1]
      odtwarzany_sekret += y%p

  print("Odtworzony sekret: ", odtwarzany_sekret%p)