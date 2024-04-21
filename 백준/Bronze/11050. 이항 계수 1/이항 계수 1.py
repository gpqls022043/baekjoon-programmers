n, k = map(int, input().split())
minus = n - k

def kf(k):
    if k <= 1:
        return 1
    return k * kf(k - 1)

def nf(n):
    if n <= 1:
        return 1
    return n * nf(n - 1)

def minusf(minus):
    if minus <= 1:
        return 1
    return minus * minusf(minus - 1)

print(nf(n) // (minusf(minus) * kf(k)))