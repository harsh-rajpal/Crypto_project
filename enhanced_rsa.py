import timeit  # importing timeit library for using timer in our program

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

# Decryption using modified RSA-CRT  which makes it different from normal RSA
def decryption(a, b, p, q, e, c):
    phi = (p-1)*(q-1)
    d = int(modinv(e, phi))
    dq = pow(d, 1, q-1)
    dp = pow(d, 1, p-1)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    qinv = modinv(q, p)
    h = (qinv*(m1-m2)) % p
    c1 = m2+h*q
    m = (c1-b)//a
    return m
# Driver Code


def main(a, b, p, q, e, pt):
    # Encryption
    start = timeit.default_timer()
    n = p*q
    # Added security
    c1 = a*pt+b
    c = encrypt(c1, n, e)
    # Noting Encryption  time which is difference of start and stop of timer
    stop = timeit.default_timer()
    enc_time = stop-start
    print('Encrypted message using modified RSA-CRT: ', c)
    # Decryption
    start = timeit.default_timer()
    m = decryption(a, b, p, q, e, c)
    # Noting Decryption  time which is difference of start and stop of timer
    stop = timeit.default_timer()
    dec_time = stop-start
    print('Decrypted message using modified RSA-CRT: ', m)
    return enc_time*1000, dec_time*1000
