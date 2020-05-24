def fatorial(n):
    print("calculando fatorial(%s)\n" % n)
    if n == 0:
        print("terminou fatorial(0) = 1\n")
        return 1
    else:
        f = n*fatorial(n-1)
        print("terminou fatorial("+str(n)+") = "+str(f)+"\n")
        return f

fatorial(4)