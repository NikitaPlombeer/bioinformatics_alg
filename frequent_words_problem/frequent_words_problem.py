file = open("input.txt", "r")

string = file.readline().strip()
k = int(file.readline().strip())

max = 0
d = {}
for i in range(len(string) - k + 1):
    str = string[i:i+k]
    if not str in d:
        d[str] = 1
    else:
        d[str] += 1
    if max < d[str]:
        max = d[str]

list = []
for key, value in d.iteritems():
    if value == max:
        list.insert(0, key)
list.sort()

for item in list:
    print item
