from atcoder.atcoder_test import def_input, input

input_text = """
3
5 2 4
"""

def_input(input_text)

from collections import deque

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    q = deque()
    q.append(A)

    while len(q) > 0:
        nxt_a = q.popleft()

        cnt = 0
        for val in nxt_a:
            if val % 2 != 0:
                cnt += 1

        if cnt == N:
            continue

        ans = 0
        fin_ans = 0
        for idx in range(N):
            try:
                if nxt_a[idx] % 2 == 0:
                    nxt_a[idx] = nxt_a[idx] // 2
                    nxt_a = [val * 3 if i != idx else val for i, val in enumerate(nxt_a) ]
                    q.append(nxt_a)
                    ans += 1
                else:
                    continue
            except:
                breakpoint()
        fin_ans = max(ans, fin_ans)
    print(fin_ans)
