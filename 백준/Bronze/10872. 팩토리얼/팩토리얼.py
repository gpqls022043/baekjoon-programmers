def factorial(n):
    if n <= 1:
        answer = 1
    else:
        answer = factorial(n - 1) * n
    return answer    
print(factorial(int(input())))