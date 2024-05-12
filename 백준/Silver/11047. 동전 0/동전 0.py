n, k = map(int, input().split())
coin = 0
coin_type = []
count = 0

for i in range(n):
    coin_type.append(int(input()))
    
coin_type.reverse()
    
for i in coin_type:
    if i <= k - coin:
        count += k // i
        k = k % i
    if coin == k:
        break

print(count)