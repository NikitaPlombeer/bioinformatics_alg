import sys

file = open("input.txt", "r")

numbers = map(int, file.readline().split())
l = numbers[0]
t = numbers[1]
dnk_list = []
for i in range(t):
    dnk_list.append(file.readline().strip())
n = len(dnk_list[0])
p = 4
word = [0] * l

decode = ['A', 'C', 'G','T']
min_total = sys.maxint
best = []
for u in range(pow(p, t)):
    mod = 1

    for i in range(len(word) - 1, -1, -1):
        tmp = word[i] + mod
        word[i] = tmp % p
        mod = tmp / p
        if mod == 0:
            break

    total = 0
    for line in dnk_list:
        min_h = sys.maxint
        for i in range(n - l + 1):
            h = 0
            for j in range(l):
                if line[i + j] != decode[word[j]]:
                    h = h + 1
            if min_h > h:
                min_h = h
        total = total + min_h
    if min_total > total:
        min_total = total
        best = word[:]
result = ""
for i in best:
    result += decode[i]
print(result)
