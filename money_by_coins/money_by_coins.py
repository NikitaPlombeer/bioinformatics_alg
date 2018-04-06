import sys


def count_min_number_of_coins(denoms, summa):
    arr = [sys.maxint] * (summa + 1)
    min_d = denoms[-1]
    for m in range(summa + 1):
        if m < min_d:
            arr[m] = 0
            continue
        for denomination in denoms:
            if m >= denomination:
                arr[m] = min(arr[m], arr[m - denomination] + 1)

    return arr[summa]


file = open("input.txt", "r")

value = int(file.readline())
denominations = map(int, file.readline().strip().split(","))

min_number = count_min_number_of_coins(denominations, value)
print(min_number)
