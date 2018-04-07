def is_balanced(graph, v):
    outputs = 0
    if v in graph:
        outputs = len(graph[v])
    inputs = 0
    for vert in graph:
        if v in graph[vert]:
            inputs += 1
    return outputs == inputs

file = open("input.txt", "r")
graph = {}
vertex = []
for line in file.readlines():
    line = line.strip()
    arr = line.split(" -> ")
    from_v = arr[0]
    graph[from_v] = []
    if not from_v in vertex:
        vertex.append(from_v)
    for v in arr[1].split(","):
        graph[from_v].append(v)
        if not v in vertex:
            vertex.append(v)


nb = []
for ver in vertex:
    if not is_balanced(graph, ver):
        nb.append(ver)

if not nb[0] in graph:
    graph[nb[0]] = []
graph[nb[0]].append(nb[1])

v = graph.keys()[0]
stack = [nb[0]]
res = ""
while len(stack) != 0:
    w = stack[-1]
    for u in graph:
        if w in graph[u]:
            stack.append(u)
            graph[u].remove(w)
            break
    if w == stack[-1]:
        stack = stack[:-1]
        res = res + w + "->"
res = res[:-2]
for i in range(len(res) - 1, -1, -1):
    if res[i] == "-":
        res = res[:i]
        break
print(res)
