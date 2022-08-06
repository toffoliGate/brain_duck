import random

def mult():
    ch = random.randint(1, 3)
    if ch == 1:
        f = "*"
        n1, n2 = random.randint(11, 99), random.randint(11, 99)
        r = n1*n2
    if ch == 2:
        f = "/"
        n1, n2 = random.randint(1000, 99999), random.randint(99, 999)
        r = n1/n2
    print(n1,f,n2)
    inp = input()
    print(r)

    return 0

mult()
