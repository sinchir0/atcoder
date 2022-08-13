from atcoder.atcoder_test import def_input, input

input_text = """
6
382253568 723152896 37802240 379425024 404894720 471526144
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    while True:
        for idx, val in enumerate(A):
            if val % 2 == 0:
                A[idx] = val // 2
            else:
                print(cnt)
                exit()
        cnt += 1
