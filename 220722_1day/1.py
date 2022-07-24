from atcoder.atcoder_test import def_input, input

input_text = """
1
10
2
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    x_num = list(map(int, input().split()))

    ans = 0
    for num in x_num:
        ans += min(num * 2, abs(num - k) * 2)

    print(ans)

    