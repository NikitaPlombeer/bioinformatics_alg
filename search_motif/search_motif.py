file = open("input.txt", "r")
numbers = map(int, file.readline().split())

l = numbers[0]
t = numbers[1]

dnk_list = []
for i in range(t):
    dnk_list.append(file.readline())
n = len(dnk_list[0])
p = n - l

best = [0] * t
bestScore = 0

s = [0] * t

for u in range(pow(p, t)):
    mod = 1
    for i in range(len(s) - 1, -1, -1):
        tmp = s[i] + mod
        s[i] = tmp % p
        mod = tmp / p
        if mod == 0:
            break
    score = 0
    for j in range(l):
        map = {}
        max = 0
        for i in range(len(dnk_list)):
            substring = dnk_list[i][s[i]:s[i] + l]
            c = substring[j]
            count = 0
            if not c in map:
                count = 1
            else:
                count = map[c] + 1
            map[c] = count
            if max < count:
                max = count
        score += max
    if bestScore <= score:
        bestScore = score
        best = s[:]

for i in range(len(dnk_list)):
    print(dnk_list[i][best[i]:best[i] + l])
