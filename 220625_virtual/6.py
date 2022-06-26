from atcoder.atcoder_test import def_input, input

input_text = """
1
1 1000000
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())

    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        num = b - a + 1
        ans += num * (2 * a + (num - 1) * 1) // 2
    print(ans)
