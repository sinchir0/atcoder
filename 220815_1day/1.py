from atcoder.atcoder_test import def_input, input

input_text = """
35753
"""

def_input(input_text)

if __name__ == "__main__":
    S = input()
    ans = float("inf")
    for i in range(len(S) - 2):
        ans = min(abs(753 - int(S[i : i + 3])), ans)
    print(ans)
