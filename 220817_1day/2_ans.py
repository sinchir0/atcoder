from atcoder.atcoder_test import def_input, input

input_text = """
1 2
123-4567
"""

def_input(input_text)

if __name__ == "__main__":
    A, B = map(int, input().split())
    S = input()

    flag = True
    for i in range(A):
        if S[i] == "-":
            flag = False

    if S[A] != "-":
        flag = False

    for i in range(A + 1, A + B + 1):
        if S[i] == "-":
            flag = False

    if flag:
        print("Yes")
    else:
        print("No")
