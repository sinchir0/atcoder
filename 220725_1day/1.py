from atcoder.atcoder_test import def_input, input

input_text = """
20 3
0 5 15
"""

def_input(input_text)

if __name__ == "__main__":
    k, n = map(int, input().split())

    a_list = list(map(int, input().split()))

    a_list.append(a_list[0] + k)

    # diff = [abs(i - j) for i, j in zip(a_list[:-1], a_list[1:])]
    max_len = 0
    for i in range(n):
        max_len = max(max_len, a_list[i + 1] - a_list[i])

    print(k - max_len)
