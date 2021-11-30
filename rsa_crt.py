import timeit
# Extended Euclidean algorithm


def egcd(e, phi):
    if e == 0:
        return (phi, 0, 1)
    else:
        g, y, x = egcd(phi % e, e)
        return (g, x-(phi//e)*y, y)
# Function to compute the modular inverse


def modinv(e, phi):
    g, x, y = egcd(e, phi)
    return x % phi
# Encryption


def encrypt(pt, n, e):
    c = pow(pt, e, n)
    return c

# Decryption using RSA-Chinese Remainder Theorem


def decryptionCRT(p, q, e, c):
    phi = (p-1)*(q-1)
    d = int(modinv(e, phi))
    dq = pow(d, 1, q-1)
    dp = pow(d, 1, p-1)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    qinv = modinv(q, p)
    h = (qinv*(m1-m2)) % p
    m = m2+h*q
    return m
# Driver Code


def main(p, q, e, pt):
    # Encryption
    start = timeit.default_timer()
    n = p*q
    c = encrypt(pt, n, e)
    stop = timeit.default_timer()
    enc_time = stop-start
    # Decryption
    start = timeit.default_timer()
    m = decryptionCRT(p, q, e, c)
    stop = timeit.default_timer()
    dec_time = stop-start
    return enc_time*1000, dec_time*1000
