from atcoder.atcoder_test import def_input, input

input_text = """
2 2
3 1
2 6
2 6
2 1
"""

def_input(input_text)

if __name__ == "__main__":
    n, x = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(n)]

    # num_listの一項目を辿り着くまでの総和の時間にする
    sum_num = 0
    ans = float("inf")
    for value in num_list:
        sum_num += value[0] + value[1]
        x -= 1
        tmp = sum_num + value[1] * x
        ans = min(ans, tmp)
        if x == 0:
            break

    print(ans)
