import sys
input = sys.stdin.readline
t = int(input())

for test in range(t):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    casinos.sort() 
    current = k
    i = 0
    
    while True:
        best = current
        start = i
        while i < n and casinos[i][0] <= current:
            l, r, real = casinos[i]
            if l <= current <= r:
                if real > best:
                    best = real
            i += 1
        if best == current:
            break
        
        current = best
        i = start
    print(current)
