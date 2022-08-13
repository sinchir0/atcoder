from atcoder.atcoder_test import def_input, input

input_text = """
10
1 2 3 4 5 6 7 8 9
"""

def_input(input_text)


if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))

    cnt = 0
    anc = p[n - 2]
    while True:
        cnt += 1
        if anc == 1:
            print(cnt)
            exit()
        anc = p[anc - 2]
