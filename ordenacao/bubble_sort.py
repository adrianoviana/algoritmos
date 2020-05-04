import random

def bubble_sort(p):
    n = len(p)
    for i in range(n):
        for j in range(n-1):
            if p[j] > p[j+1]:
                troca = p[j]
                p[j] = p[j+1]
                p[j+1] = troca
    return p

print("array desordenado")
d = random.sample(range(1, 1000), 30)
print(d)
print("array ordenado")
print(bubble_sort(d))