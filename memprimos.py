passos = 0

def teste_primo(x, primos):
	global passos
	n = len(primos)
	composto = False
	for p in primos:
		passos += 1
		if p >= x or p**2 > x:
			break
		composto = x % p == 0
		if composto:
			break
	if not composto:
		primos.append(x)
	return not composto

def teste_primos_ingenuo(x):
	global passos
	composto = False
	for i in range(2,x):
		passos += 1
		if i**2 > x:
			break
		composto = x % i == 0
		if composto:
			break
	return not composto

def teste_primos_muito_ingenuo(x):
	global passos
	composto = False
	for i in range(2,x):
		passos += 1
		composto = x % i == 0
		if composto:
			break
	return not composto

import time

MAX_PRIMO = 100000

primos = list()
start = time.clock()
for i in range(2,MAX_PRIMO):
	teste_primo(i,primos)

print((time.clock() - start))
print(passos)

passos = 0
primos = list()
start = time.clock()
for i in range(2,MAX_PRIMO):
	if teste_primos_ingenuo(i):
		primos.append(i)
print((time.clock() - start))
print(passos)

passos = 0
primos = list()
start = time.clock()
for i in range(2,MAX_PRIMO):
	if teste_primos_muito_ingenuo(i):
		primos.append(i)
print((time.clock() - start))
print(passos)
