from atcoder.atcoder_test import def_input, input

input_text = """
5 4 3
5 5 0 6 3
"""

def_input(input_text)

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    accumulate = [0]

    for element in A:
        accumulate.append(accumulate[-1] + element)

    left = [l * L - accumulate[l] for l in range(N + 1)]

    right = [(N - r) * R + accumulate[r] for r in range(N + 1)]

    rightmin = right
    for i in range(N - 1, -1, -1):
        rightmin[i] = min(rightmin[i], rightmin[i + 1])

    ans = float("inf")

    for l in range(N + 1):
        tmp = left[l] + rightmin[l]
        ans = min(ans, tmp)

    print(ans)
