from atcoder.atcoder_test import def_input, input

input_text = """
0 1 4 5
"""

def_input(input_text)

if __name__ == "__main__":
    l1, r1, l2, r2 = map(int, input().split())
    blue_l = list(range(l1, r1 + 1))
    red_l = list(range(l2, r2 + 1))

    ans = len(set(blue_l) & set(red_l))
    if ans <= 1:
        print(0)
    else:
        print(ans - 1)
