from atcoder.atcoder_test import def_input, input

input_text = """
2 10
"""

def_input(input_text)

import itertools

if __name__ == "__main__":
    n, m = map(int, input().split())
    cand = list(range(1, m + 1))

    for ans in itertools.permutations(cand, n):
        num = 0
        flg = True
        for val in ans:
            if num >= val:
                flg = False
                break
            num = val
        if flg:
            print(*ans)
