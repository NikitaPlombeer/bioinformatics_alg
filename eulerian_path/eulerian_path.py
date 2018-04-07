file = open("input.txt", "r")
graph = {}
for line in file.readlines():
    line = line.strip()
    arr = line.split(" -> ")
    graph[arr[0]] = []
    for v in arr[1].split(","):
        graph[arr[0]].append(v)

v = graph.keys()[0]
stack = [v]
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
print(res[:-2])
