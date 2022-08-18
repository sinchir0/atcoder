from atcoder.atcoder_test import def_input, input

input_text = """
2
2
2
100
"""

def_input(input_text)

if __name__ == "__main__":
    A, B, C, X = int(input()), int(input()), int(input()), int(input())

    ans = 0
    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(C + 1):
                tmp = 500 * i + 100 * j + 50 * k
                if tmp == X:
                    ans += 1
    print(ans)
