n = int(input())
arr = list(map(int, input().split()))

arr.sort()

day = 1

for problems in arr:
    if problems >= day:
        day += 1

print(day - 1)
