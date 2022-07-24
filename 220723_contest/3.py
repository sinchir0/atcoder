from atcoder.atcoder_test import def_input, input

input_text = """
5
newfile
newfile
newfolder
newfile
newfolder
"""

def_input(input_text)

from collections import defaultdict

if __name__ == "__main__":
    n = int(input())

    d = defaultdict(int)

    for _ in range(n):
        s = input()
        num = d[s]

        if num:
            print(s + "(" + str(num) + ")")
        else:
            print(s)
        d[s] += 1
