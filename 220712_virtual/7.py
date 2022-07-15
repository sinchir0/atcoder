from atcoder.atcoder_test import def_input, input

input_text = """
KIHBR
"""

def_input(input_text)

from itertools import groupby


def rle(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


import re

if __name__ == "__main__":
    s = input()

    pat = r"A{0,1}K{1}I{1}H{1}A{0,1}B{1}A{0,1}R{1}A{0,1}$"

    if re.match(pat, s):
        print("YES")
    else:
        print("NO")
    
