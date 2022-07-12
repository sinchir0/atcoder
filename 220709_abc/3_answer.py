from atcoder.atcoder_test import def_input, input

input_text = """
abbaac
abbbbaaac
"""

def_input(input_text)

from itertools import groupby


def rle(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


if __name__ == "__main__":
    s = list(input())
    t = list(input())

    ls = rle(s)
    lt = rle(t)

    if len(ls) != len(lt):
        print("No")
        exit()

    ls_k = [item[0] for item in ls]
    lt_k = [item[0] for item in lt]

    if ls_k != lt_k:
        print("No")
        exit()

    for i in range(len(ls)):
        if ls[i][1] != lt[i][1]:
            print("No")
            exit()
        if (ls[i][1] > lt[i][1]) or (lt[i][1] < 2):
            print("No")
            exit()

    print("Yes")
