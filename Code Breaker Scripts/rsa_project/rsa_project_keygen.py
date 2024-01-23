def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def generate_keys(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    g = gcd(e, phi)
    while g != 1:
        e += 1
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def main():
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (not one you entered above): "))
    public, private = generate_keys(p, q)
    print("Your public key is ", public, " and your private key is ", private)

if __name__ == '__main__':
    main()


#pub key = (5,323), priv key = (173,323)