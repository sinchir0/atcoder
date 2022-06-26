from atcoder.atcoder_test import def_input, input

input_text = """
20 199999
oooooooooxoooooooooo
"""

def_input(input_text)

if __name__ == "__main__":
    N, X = map(int, input().split())
    ans_list = list(input())
    for n in range(N):
        if ans_list[n] == "o":
            X += 1
        else:
            X = max(0, X - 1)
    print(X)
