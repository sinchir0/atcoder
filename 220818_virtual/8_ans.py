from atcoder.atcoder_test import def_input, input

input_text = """
3
5 2 4
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    for a in A:
        while a % 2 == 0:
            a = a // 2
            cnt += 1

    print(cnt)
