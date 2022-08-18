from atcoder.atcoder_test import def_input, input

input_text = """
5
IIDID
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    S = list(input())

    tmp = 0
    ans = 0
    for word in S:
        if word == "I":
            tmp += 1
        else:
            tmp -= 1
        ans = max(ans, tmp)
    print(ans)
