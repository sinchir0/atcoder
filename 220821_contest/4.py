# 尺取法でも実装できるかも
from atcoder.atcoder_test import def_input, input

input_text = """
10 5 7 5
1 3 2 2 2 3 1 4 3 2
"""

def_input(input_text)

if __name__ == "__main__":
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    accumulate = [0]

    for element in A:
        accumulate.append(accumulate[-1] + element)

    x, y, z, w = -1, -1, -1, -1

    for left_idx in range(0, N):
        for right_idx in range(1, N):
            if accumulate[right_idx] - accumulate[left_idx] > P:
                break

            if accumulate[right_idx] - accumulate[left_idx] == P:
                x, y = left_idx, right_idx
                break
        if x != -1 and y != -1:
            break

    if x == -1 and y == -1:
        print("No")
        exit()

    for right_idx in range(y + 1, N):
        if accumulate[right_idx] - accumulate[y] > Q:
            break

        if accumulate[right_idx] - accumulate[y] == Q:
            z = right_idx
            break

    if z == -1:
        print("No")
        exit()

    for right_idx in range(z + 1, N):
        if accumulate[right_idx] - accumulate[z] > R:
            break

        if accumulate[right_idx] - accumulate[z] == R:
            w = right_idx
            break

    if w == -1:
        print("No")
        exit()
    else:
        print("Yes")
