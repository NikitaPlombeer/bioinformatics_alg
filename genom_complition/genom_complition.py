def vert_in_outs(graph, v):
    outputs = 0
    if v in graph:
        outputs = len(graph[v])
    inputs = 0
    for vert in graph:
        if v in graph[vert]:
            inputs += 1
    return (outputs, inputs)


file = open("input.txt", "r")
k = int(file.readline().strip())

kmers = []
for line in file.readlines():
    kmers.append(line.strip())

graph = {}

for kmer in kmers:
    graph[kmer[1:]] = []
    graph[kmer[:-1]] = []

vertex = []
for vert in graph:
    if not vert in vertex:
        vertex.append(vert)
    for kmer in kmers:
        if kmer[:-1] == vert:
            if not kmer[1:] in vertex:
                vertex.append(kmer[1:])
            graph[vert].append(kmer[1:])

start = ""
end = ""
for ver in vertex:
    (outputs, inputs) = vert_in_outs(graph, ver)
    if outputs > inputs:
        start = ver
    if outputs < inputs:
        end = ver

if not end in graph:
    graph[end] = []
graph[end].append(start)

stack = [start]
res = ""
loop = []
while len(stack) != 0:
    w = stack[-1]
    for u in graph:
        if w in graph[u]:
            stack.append(u)
            graph[u].remove(w)
            if u != w:
                break
    if w == stack[-1]:
        stack = stack[:-1]
        loop.append(w)

loop = loop[:-1]
res = ""
for i in range(len(loop) - 1):
    res = res + loop[i][0]
res = res + loop[-1]
print(res)
