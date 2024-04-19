after = []

while True:
    before = int(input())
    if before != 0:
        before = list(str(before))
        for i in range(1, len(before) + 1):
            after.append(before[len(before) - i])
        if after == before:
            print('yes')
            after.clear()
        else:
            print('no')
            after.clear()
    else:
        break