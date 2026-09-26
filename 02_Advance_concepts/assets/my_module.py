def HCF(a, b):
    if b == 0:
        return a
    else:
        return HCF(b, a % b)

def LCM(a, b):
    return (a * b) // HCF(a, b)

PI = 3.14159