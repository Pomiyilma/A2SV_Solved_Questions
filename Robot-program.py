import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
    
    prefix = []
    current = 0
    
    for ch in s:
        if ch == 'L':
            current -= 1
        else:
            current += 1
        prefix.append(current)
    
    answer = 0
    first_hit_time = -1
    
    for i in range(n):
        if x + prefix[i] == 0:
            first_hit_time = i + 1
            break
    
    if first_hit_time == -1 or first_hit_time > k:
        print(0)
        continue
    
    answer = 1
    remaining = k - first_hit_time

    cycle_length = -1
    for i in range(n):
        if prefix[i] == 0:
            cycle_length = i + 1
            break
    
    if cycle_length == -1:
        print(answer)
    else:
        answer += remaining // cycle_length
        print(answer)
