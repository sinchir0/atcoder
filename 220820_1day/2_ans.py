from atcoder.atcoder_test import def_input, input

input_text = """
29
20
7
35
120
"""

def_input(input_text)

import itertools

if __name__ == "__main__":
    num = [int(input()) for _ in range(5)]

    ans = float("inf")

    for cand in list(itertools.permutations(num)):
        tmp = 0
        for idx, val in enumerate(cand):
            if idx == 4:
                tmp += val
            else:
                if val % 10 > 0:
                    val = val - (val % 10) + 10
                tmp += val
        ans = min(ans, tmp)

    print(ans)
