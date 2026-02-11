import sys
input = sys.stdin.readline

test_case = int(input())

for test in range(test_case):
    n = int(input())
    s = input()

    ans = 10**10   #some Big number

    for i in range(n):
        a = b = c = 0

        for j in range(i, min(n, i + 7)):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1

            length = j - i + 1

            if length >= 2 and a > b and a > c:
                ans = min(ans, length)

    print(ans if ans != 10**10 else -1)
