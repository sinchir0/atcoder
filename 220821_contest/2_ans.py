from atcoder.atcoder_test import def_input, input

input_text = """
4 1 10
9 1 1
1 3
"""

def_input(input_text)

if __name__ == "__main__":
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))

    bonus = [0] * N
    for _ in range(M):
        x, y = map(int, input().split())
        bonus[x - 1] = y

    T += bonus[0]

    for idx in range(N - 1):
        T -= A[idx]

        if bonus[idx]:
            T += bonus[idx]

        if T <= 0:
            print("No")
            exit()

    print("Yes")
