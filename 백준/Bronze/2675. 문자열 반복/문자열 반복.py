t = int(input())

for i in range(t):
    sent = []
    sent1 = ''
    r, s = input().split()
    s = list(str(s))
    for k in range(len(s)):
        sent.append(s[k] * int(r))
    for j in range(len(s)):
        sent1 = sent1 + sent[j]
    print(sent1)