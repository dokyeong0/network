def gcd(a,b):
    larger = 0
    smaller = 100000
    if (a>b):
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    while smaller > 0:
        rem = larger % smaller 
        larger = smaller
        smaller = rem
    return larger

if __name__ == "__main__":
    res = gcd(256,240)
    print(res)