from atcoder.atcoder_test import def_input, input

input_text = """
Niwawo_Kakemeguru_Chokudai
11 17 18 26
"""

def_input(input_text)

if __name__ == "__main__":
    s = list(input())
    a, b, c, d = map(int, input().split())

    punct_num = set({a, b, c, d})

    ans = []
    for idx in range(len(s) + 1):
        if idx in punct_num:
            ans.append('"')
        if idx == len(s):
            break
        ans.append(s[idx])

    print("".join(ans))
