n = int(input())
card = [x for x in range(1, n + 1)]
answer = []
running = True

while running:
    if len(card) == 1:
        break
    answer.append(card[0])
    card.pop(0)
    card.append(card[0])
    card.pop(0)
print(*answer + card)