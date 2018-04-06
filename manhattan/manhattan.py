def distance_func(sw, ew, n, m):
    arr = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        arr[i][0] = arr[i - 1][0] + sw[i - 1][0]

    for j in range(1, m + 1):
        arr[0][j] = arr[0][j - 1] + ew[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] = max(arr[i - 1][j] + sw[i - 1][j],
                            arr[i][j - 1] + ew[i][j - 1])
    return arr[n][m]


file = open("input.txt", "r")

numbers = map(int, file.readline().split())
n = numbers[0]
m = numbers[1]

southern_weights = []
east_weights = []

for i in range(n):
    southern_weights.append(map(int, file.readline().strip().split()))

file.readline()

for i in range(n + 1):
    east_weights.append(map(int, file.readline().strip().split()))

distance = distance_func(southern_weights, east_weights, n, m)
print(distance)
