f = int(input())
s = input()
s_l = list(map(int, str(s)))
sent = 0

for i in range(f):
    sent = sent + int(s_l[i])
print(sent)