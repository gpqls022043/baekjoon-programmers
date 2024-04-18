a, b = map(int, input().split())

def min(a, b):
    a_list = []
    b_list = []
    for i in range(1, a + 1):
        if a % i == 0:
            a_list.append(i)
    for j in range(1, b + 1):
        if b % j == 0:
            b_list.append(j)
    a_list.reverse()
    b_list.reverse()
    for A in a_list:
        for B in b_list:
            if A == B:
                return A
           
def max(a, b):
    for i in range(1, b + 1):
        for j in range(1, a + 1):
            if a * i == b * j:
                return a * i
            else:
                continue
print(min(a, b))
print(max(a, b))