# coding=utf-8
# короч в моем питоне нет енамов: грусть_печаль

direction_map = {'UP': '↑', 'LEFT': '←', 'DIAG': '↖'}
letters = {}
scoring_matrix = []


def razruli(v, w, i, j, s):
    direction = direction_map['UP']
    b_max = s[i - 1][j] - 5

    if s[i][j - 1] - 5 > b_max:
        b_max = s[i][j - 1] - 5
        direction = direction_map['LEFT']

    vi = v[i - 1]
    wj = w[j - 1]
    score = scoring_matrix[letters[vi]][letters[wj]]
    if b_max < (s[i - 1][j - 1] + score):
        b_max = s[i - 1][j - 1] + score
        direction = direction_map['DIAG']

    if b_max < 0:
        b_max = 0
    s[i][j] = b_max
    return direction


def make_word(v, w, directions, n, m, first, s):
    result = ""
    i = n - 1
    j = m - 1

    score_max = s[i][j]
    for ii in range(n):
        for jj in range(m):
            if(s[ii][jj] > score_max):
                score_max = s[ii][jj]
                i = ii
                j = jj

    while i >= 0 and j >= 0:
        if s[i][j] == 0:
            break
        if directions[i][j] == direction_map['DIAG']:
            if first:
                result = w[j - 1] + result
            else:
                result = v[i - 1] + result

            i -= 1
            j -= 1
        elif directions[i][j] == direction_map['UP']:
            if first:
                result = "-" + result
            else:
                result = v[i - 1] + result

            i -= 1
        elif directions[i][j] == direction_map['LEFT']:
            if not first:
                result = "-" + result
            else:
                result = w[j - 1] + result
            j -= 1
    return result


def common_substring(v, w):
    n = len(v) + 1
    m = len(w) + 1
    directions = [[-1 for x in range(m)] for y in range(n)]
    s = [[0 for x in range(m)] for y in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            directions[i][j] = razruli(v, w, i, j, s)

    directions[0][0] = direction_map['DIAG']
    for i in range(1, m):
        directions[0][i] = direction_map['LEFT']
    for i in range(1, n):
        directions[i][0] = direction_map['UP']

    score_max = s[0][0]
    for ii in range(n):
        for jj in range(m):
            if (s[ii][jj] > score_max):
                score_max = s[ii][jj]
    print(score_max)
    
    print(make_word(v, w, directions, n, m, True, s))
    print(make_word(v, w, directions, n, m, False, s))



file = open("PAM250.txt", "r")
lines = file.readlines()

for idx, letter in enumerate(lines[0].split()):
    letters[letter] = idx

for line in lines[1:]:
    scoring_matrix.append(map(int, line.split()[1:]))

file = open("input.txt", "r")

v = file.readline().strip()
w = file.readline().strip()

common_substring(v, w)
