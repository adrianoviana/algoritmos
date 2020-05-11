import random

def insertion_sort(p):
    n = len(p)
    for i in range(n):
        v = p[i]
        l = i
        while l > 0 and p[l-1] > v:
            p[l] = p[l-1]
            l = l-1
        p[l] = v
    return p

d = random.sample(range(1, 1000), 30)
print("Array desordenado")
print(d)
print("Array ordenado")
print(insertion_sort(d))