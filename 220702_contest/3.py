from atcoder.atcoder_test import def_input, input

input_text = """
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5
"""

def_input(input_text)

if __name__ == "__main__":
    n, q = map(int, input().split())
    s = input()

    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            last_ch = s[-x:]
            s = last_ch + s

            s = s[:-x]
        elif t == 2:
            print(s[x - 1])
