from atcoder.atcoder_test import def_input, input

input_text = """
2
-3 6
4 2
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans = 0
    for a, b in zip(A,B):
        ans += a * b

    if ans == 0:
        print("Yes")
    else:
        print("No")

