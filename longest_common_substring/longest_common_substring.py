# coding=utf-8
# короч в моем питоне нет енамов: грусть_печаль

map = {'UP': 0, 'LEFT': 1, 'DIAG': 2}


def razruli(v, w, i, j, s):
    if j == 1 and i != 1:
        direction = map['UP']
        s[i][j] = s[i - 1][j]
    elif i == 1 and j != 1:
        direction = map['LEFT']
        s[i][j] = s[i][j - 1]
    else:
        direction = map['UP']
        b_max = s[i - 1][j]

        if s[i][j - 1] >= b_max:
            b_max = s[i][j - 1]
            direction = map['LEFT']

        if v[i - 1] == w[j - 1] and b_max <= (s[i - 1][j - 1] + 1):
            b_max = s[i - 1][j - 1] + 1
            direction = map['DIAG']

        s[i][j] = b_max
    return direction


def make_word(v, directions, n, m):
    result = ""
    i = n - 2
    j = m - 2
    while i >= 0 and j >= 0:
        if directions[i][j] == map['DIAG']:
            result = v[i] + result
            i -= 1
            j -= 1
        elif directions[i][j] == map['UP']:
            i -= 1
        elif directions[i][j] == map['LEFT']:
            j -= 1
    return result


def common_substring(v, w):
    n = len(v) + 1
    m = len(w) + 1
    directions = [[-1 for x in range(m - 1)] for y in range(n - 1)]
    s = [[0 for x in range(m)] for y in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            directions[i - 1][j - 1] = razruli(v, w, i, j, s)

    return make_word(v, directions, n, m)

file = open("input.txt", "r")

v = file.readline().strip()
w = file.readline().strip()

cs = common_substring(v, w)
print(cs)
