import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ops = []

    
    for i in range(n): #a[i] < b[i]
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append((3, i + 1))

    for _ in range(n):  #bubblesortinG both
        for j in range(n - 1):
            # sort row a
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ops.append((1, j + 1))
                if a[j] > b[j]:
                    a[j], b[j] = b[j], a[j]
                    ops.append((3, j + 1))
                if a[j + 1] > b[j + 1]:
                    a[j + 1], b[j + 1] = b[j + 1], a[j + 1]
                    ops.append((3, j + 2))
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                ops.append((2, j + 1))
                if a[j] > b[j]:
                    a[j], b[j] = b[j], a[j]
                    ops.append((3, j + 1))
                if a[j + 1] > b[j + 1]:
                    a[j + 1], b[j + 1] = b[j + 1], a[j + 1]
                    ops.append((3, j + 2))

    print(len(ops))
    for t, i in ops:
        print(t, i)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
