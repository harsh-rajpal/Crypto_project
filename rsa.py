import timeit #importing timeit library for using timer in our program
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


# Decryption using simple RSA
def decryptionRSA(p, q, e, c):
    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    return m


# Driver Code
def main(p, q, e, pt):
    # Encryption
    start = timeit.default_timer()
    n = p*q
    c = encrypt(pt, n, e)
    stop = timeit.default_timer()
    enc_time = stop-start #Noting Encryption  time which is difference of start and stop of timer
    # Decryption
    start = timeit.default_timer()
    m = decryptionRSA(p, q, e, c)
    stop = timeit.default_timer()
    # Noting Decryption  time which is difference of start and stop of timer
    dec_time = stop-start
    return enc_time*1000, dec_time*1000