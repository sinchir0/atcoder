N, M = map(int, input().split())

fin_l = 0
fin_r = float("inf")
for _ in range(M):
    L, R = map(int, input().split())
    fin_l = max(L, fin_l)
    fin_r = min(R, fin_r)

if fin_r >= fin_l:
    print(fin_r - fin_l + 1)
else:
    print(0)