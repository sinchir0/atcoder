from atcoder.atcoder_test import def_input, input

input_text = """
2
3 4
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split()))

    v = sorted(v, reverse=True)

    if len(v) == 2:
        print(sum(v) / len(v))
        exit()

    ans = v.pop()
    while len(v) > 1:
        a = v.pop()
        ans = (ans + a) / 2

    print((ans + v[0]) / 2)
