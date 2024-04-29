n = int(input())
count = 0

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
fact = list(map(int, str(factorial(n))))
fact.reverse()

for i in fact:
    if i == 0:
        count += 1
        continue
    else:
        print(count)
        break