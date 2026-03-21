import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)

    dp = [0] * n            # dp[i]=length of longest regular bracket substring ending at i
    st = []                 #stack ofIndices of '('

    best, cnt = 0, 0       #cnt = nuM of substr with length=best
    for i, ch in enumerate(s):
        if ch == '(':
            st.append(i)
        else:  # ch == ')'
            if st:
                j = st.pop()            # index oF matching '('
                base = i - j + 1
                if j - 1 >= 0:
                    base += dp[j - 1]
                dp[i] = base

                if dp[i] > best:
                    best = dp[i]
                    cnt = 1
                elif dp[i] == best and best > 0:
                    cnt += 1
    if best == 0:
        print("0 1")
    else:
        print(best, cnt)

if __name__ == "__main__":
    main()
