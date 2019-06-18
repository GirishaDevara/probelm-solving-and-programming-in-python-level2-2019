def prime(i):
    f = True
    if i == 2:
        return True
    for value in range(2,int(i**0.5)+1):
        if i % value == 0:
            return False
    return True


def SpecialNum(n,p):
    prime_count=0
    for v in range(2,n):
        if n % v == 0 and prime(v):
            prime_count += 1
    if prime_count == p:
        return "YES"
    return "NO"