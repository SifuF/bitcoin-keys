# secp256k1 curve parameters (P, A, B, G(x,y), N, H)
P = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
A = 7
B = 0
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G = (Gx, Gy)
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
H = 0x01


# Extended Euclidean algorithm
def modInv(a):
    t_n, t = 1, 0
    r_n, r = a % P, P
    while r_n != 0:
        quot = r//r_n
        t, t_n = t_n, t - t_n*quot
        r, r_n = r_n, r - r_n*quot
    if r > 1:
        raise Exception('Error: a is not invertible')
    if t < 0:
        t = t + P
    return t


def EC_Add(a, b):
    lam = ((b[1] - a[1]) * modInv(b[0] - a[0])) % P
    x_r = (lam**2 - a[0] - b[0]) % P
    y_r = (lam*(a[0] - x_r) - a[1]) % P
    return x_r, y_r


def EC_Double(a):
    lam = (3*(a[0]**2) * modInv(2*a[1])) % P
    x_r = (lam ** 2 - 2*a[0]) % P
    y_r = (lam * (a[0] - x_r) - a[1]) % P
    return x_r, y_r


# Double and add (always double, add only if bit is set).
def EC_Multiply(k, generator):
    if k == 0 or k >= N:
        raise Exception('Bad private key!')
    kBin = str(bin(k))[2:]
    pubK = generator
    for i in range(1, len(kBin)):
        pubK = EC_Double(pubK)
        if kBin[i] == "1":
            pubK = EC_Add(pubK, generator)
    return pubK


privKey = 0x1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD
pubKey = EC_Multiply(privKey, G)
print("PrivateKey =", hex(privKey)[2:])
print("PublicKey uncompressed = 04", hex(pubKey[0])[2:], hex(pubKey[1])[2:])

