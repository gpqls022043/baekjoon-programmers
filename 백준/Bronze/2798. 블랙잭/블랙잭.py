n, m = map(int, input().split())
card = list(map(int, input().split()))
blackjack_sum = 0

for i in range(n):
    for j in range(1, n):
        for k in range(2, n):
            if card[i] == card[j] or card[j] == card[k] or card[k] == card[i]:
                continue
            else:
                plus = card[i] + card[j] + card[k]
            if m - plus < 0:
                continue
            elif m - blackjack_sum > m - plus:
                blackjack_sum = plus
print(blackjack_sum)