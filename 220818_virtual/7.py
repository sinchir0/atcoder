from atcoder.atcoder_test import def_input, input

input_text = """
AtCoCo
"""

def_input(input_text)

import collections
import re

if __name__ == "__main__":
    S = input()
    flag = True
    if S[0] != "A":
        flag = False

    cnt = collections.Counter(list(S[2:-1]))
    if cnt["C"] != 1:
        flag = False

    if not re.sub("A|C", "", S).islower():
        flag = False

    if flag:
        print("AC")
    else:
        print("WA")
