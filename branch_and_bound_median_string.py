import sys

decode = ["A", "C", "G", "T"]

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


def distance_func(s1, s2, l):
    dist = 0
    for ind in range(l):
        if s1[ind] != s2[ind]:
            dist += 1
    return dist


def total_distance_func(dna, word, t, n, l):
    result = 0
    for ind in range(t):
        min_h = sys.maxint
        for j in range(n):
            sub = dna[ind][j:j + l]
            dist = distance_func(sub, word, l)
            if min_h > dist:
                min_h = dist
        result += min_h
    return result


def make_word(s, l):
    res = "A" * l
    for i in range(l):
        res = res[:i] + decode[s[i] - 1] + res[i + 1:]
    return res


def branch_and_bound_motif_search(dnk_list, t, n, l):
    s = [1] * l
    best_distance = sys.maxint
    i = 1
    best_word = ""
    while i > 0:
        if i < l:
            word = make_word(s, i)
            optimistic_distance = total_distance_func(dnk_list, word, t, n, i)
            if optimistic_distance > best_distance:
                i = bypass(s, i, 4)
            else:
                i = next_vertex(s, i, l, 4)
        else:
            word = make_word(s, l)
            distance = total_distance_func(dnk_list, word, t, n, i)
            if distance < best_distance:
                best_distance = distance
                best_word = word
            i = next_vertex(s, i, l, 4)
    return best_word


numbers = map(int, raw_input().split())
l = numbers[0]
t = numbers[1]

dnk_list = []
for i in range(t):
    dnk_list.append(raw_input())
n = len(dnk_list[0])

best = branch_and_bound_motif_search(dnk_list, t, n - l + 1, l)
print(best)
