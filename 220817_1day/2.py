from atcoder.atcoder_test import def_input, input

input_text = """
1 2
1
"""

def_input(input_text)

if __name__ == "__main__":
    A, B = map(int, input().split())
    S = input()

    if len(S) != (A + B + 1):
        print("No")
        exit()

    cand_word = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    first = S[:A]
    haifun = S[A : A + 1]
    last = S[A + 1 :]

    if haifun != "-":
        print("No")
        exit()

    for val in first:
        if val not in cand_word:
            print("No")
            exit()

    for val in last:
        if val not in cand_word:
            print("No")
            exit()

    print("Yes")
