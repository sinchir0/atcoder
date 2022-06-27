from atcoder.atcoder_test import def_input, input

input_text = """
7
14 14 2 13 56 2 37
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = 1001001001  # ちょうど10桁と分かりやすく、32bitでもC言語だったらオーバーフローしない数字

    for mean in range(min(num_list), max(num_list)+1):
        n_ans = sum([(num - mean) ** 2 for num in num_list])
        if ans > n_ans:
            ans = n_ans

    print(ans)
