def next_vertex(s, i, L, k):
    if i < L:
        s[i + 1 - 1] = 1
        return i + 1
    for j in range(L, 0, -1):
        if s[j - 1] < k:
            s[j - 1] += 1
            return j
    return 0


def bypass(s, i, k):
    for j in range(i, 0, -1):
        if s[j - 1] < k:
            s[j - 1] += 1
            return j
    return 0


def det_score(s, i, l, dnk_list):
    score = 0
    for j in range(l):
        map = {}
        max = 0
        for u in range(i):
            substring = dnk_list[u][s[u] - 1:s[u] + l - 1]
            c = substring[j]
            if not c in map:
                count = 1
            else:
                count = map[c] + 1
            map[c] = count
            if max < count:
                max = count
        score += max
    return score


#l = 3
#t = 5
def branch_and_bound_motif_search(dnk_list, t, n, l):
    s = [1] * t
    best_score = 0
    i = 1
    best = []
    while i > 0:
        if i < t:
            optimistic_score = det_score(s, i, l, dnk_list) + (t - i) * l
            if optimistic_score < best_score:
                i = bypass(s, i, n - l + 1)
            else:
                i = next_vertex(s, i, t, n - l + 1)
        else:
            score = det_score(s, i, l, dnk_list)
            if score >= best_score:
                best_score = score
                best = s[:]
            i = next_vertex(s, i, t, n - l + 1)
    return best


numbers = map(int, raw_input().split())
l = numbers[0]
t = numbers[1]

dnk_list = []
for i in range(t):
    dnk_list.append(raw_input())
n = len(dnk_list[0])

best = branch_and_bound_motif_search(dnk_list, t, n, l)

for i in range(len(dnk_list)):
    print(dnk_list[i][best[i] - 1:best[i] + l - 1])
