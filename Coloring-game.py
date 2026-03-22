import sys
from bisect import bisect_right

def count_pairs_greater(a, left, right, need):
    cnt = 0

    for j in range(left + 1, right + 1):
        
        target = need - a[j] #want a[i] > need - a[j]
        idx = bisect_right(a, target, left, j)
        cnt += (j - idx)
    return cnt

def solve_one(a):
    n = len(a)
    if n < 3:
        return 0

    best, ans =0,0
    maxv = a[-1]

    for k in range(0, n - 2):
        if k == n - 1:
            continue
        if k <= n - 3:
            M = maxv
        else:
            M = maxv

        need = max(a[k], M - a[k])
        right = k - 1
        if right >= 1:
            ans += count_pairs_greater(a, 0, right, need)
    k = n - 1
    z = a[k]

    if n - 3 >= 0:
        j = n - 2
        if j - 1 >= 0:
            M = a[n - 3]
            need = max(z, M - z)  
            target = need - a[j]
            idx = bisect_right(a, target, 0, j)  # i in [0..j)
            ans += (j - idx)  # i choices


    if n - 3 >= 1:
        M = a[n - 2]
        need = max(z, M - z)
        ans += count_pairs_greater(a, 0, n - 3, need)
    return ans

def main():
    input = sys.stdin.readline
    test_case = int(input())
    for test in range(test_case):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve_one(a))

if __name__ == "__main__":
    main()
