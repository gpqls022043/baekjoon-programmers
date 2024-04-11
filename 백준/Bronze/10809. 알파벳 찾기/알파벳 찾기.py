from string import ascii_lowercase

s = list(str(input()))
alphabet = list(ascii_lowercase)
minus = []
for i in range(len(alphabet)):
    minus.append(-1)
    
for j in range(len(alphabet)):
    for k in range(len(s)):
        if s[k] == alphabet[j]:
            minus.insert(alphabet.index(s[k]), s.index(s[k]))
            del minus[alphabet.index(s[k]) + 1]
print(*minus)