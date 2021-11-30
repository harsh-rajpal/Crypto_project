import random


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def mod_inverse(x, y):
    x = x % y
    for i in range(1, y):
        if (x*i) % y == 1:
            return i


def encrypt(p, q, msg):
    n = p*q
    phi_n = (p-1)*(q-1)

    while True:
        e = random.randrange(1, phi_n)
        g = gcd(e, phi_n)
        d = mod_inverse(e, phi_n)

        if g == 1 and e != d:
            break

    ct = [pow(ord(i), e, n) for i in msg]
    ct_arr = [chr(i) for i in ct]
    ct_str = "".join(ct_arr)
    return n, phi_n, e, d, ct, ct_str


def decrypt(d, n, ct_str):
    ct = [ord(i) for i in ct_str]
    pt = [pow(i, d, n) for i in ct]
    pt_arr = [chr(i) for i in pt]
    pt_str = "".join(pt_arr)
    return pt_str
