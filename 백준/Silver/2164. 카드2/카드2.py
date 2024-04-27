from collections import deque

n = int(input())
card = deque(x for x in range(1, n + 1))
count = 0

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(*card)