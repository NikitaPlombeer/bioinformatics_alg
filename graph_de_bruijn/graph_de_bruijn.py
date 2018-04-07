file = open("input.txt")
kmers = file.readlines()

for idx, value in enumerate(kmers):
    kmers[idx] = value.strip()


graph = {}

for kmer in kmers:
    graph[kmer[1:]] = []
    graph[kmer[:-1]] = []

for vert in graph:
    for kmer in kmers:
        if kmer[:-1] == vert:
            graph[vert].append(kmer[1:])

for vert in graph:
    res = vert + " -> "
    if len(graph[vert]) != 0:
        for v in graph[vert]:
            res = res + v + ","
        print(res[:-1])
