import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
 
    balance = [0] * n #balance=[0,0,0..
    curr = 0
    for i in range(n):
        if a[i] == '1':
            curr += 1
        else:
            curr -= 1
        balance[i] = curr
 
    flipped = False
    poss = True
 
    for i in range(n - 1, -1, -1): #right to left
        current_bit = a[i]
        if flipped:
            current_bit = '1' if current_bit == '0' else '0' #logical inversion of bit
 
        if current_bit != b[i]:
            if balance[i] != 0:#flip prefix [0..i]
                poss = False
                break
            flipped = not flipped
 
    print("YES" if poss else "NO")
