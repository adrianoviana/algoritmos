import random

def selection_sort(p):
    n = len(p)
    for i in range(n-1):
        imin = i
        for j in range(i+1, n):
            if p[j] < p[imin]:
                imin = j
        troca = p[i]
        p[i] = p[imin]
        p[imin] = troca
    return p

d = random.sample(range(1, 1000), 30)
print("Array aleatório/n")
print(d)
print("Array Ordenado/n")
print(selection_sort(d))