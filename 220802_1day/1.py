from atcoder.atcoder_test import def_input, input

input_text = """
HATAGAYA
"""

def_input(input_text)

if __name__ == "__main__":
    s = list(input())

    cnt = 0
    ans = 0

    for chr in s:
        if chr in ["A", "C", "G", "T"]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0

    print(ans)
