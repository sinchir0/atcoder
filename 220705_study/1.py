from atcoder.atcoder_test import def_input, input

input_text = """
3
000
1 2 3
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())

    s = input()

    w_list = list(map(int, input().split()))

    # sortを行う
    weight_s_list = list(zip(s, w_list))

    weight_s_list = sorted(weight_s_list, key=lambda x: x[1])

    # 最初は大人の人数が答えとなる
    now = s.count("1")
    ans = now

    # Wの小さい方から区切っていった時に、子供であったらnowを増やし、大人だったらnowを減らす
    for i in range(n):
        if weight_s_list[i][0] == "0":
            now += 1
        else:
            now -= 1
        # 同じ体重が二人続いた場合はansを更新しない
        if (i < n - 1) and (weight_s_list[i][1] == weight_s_list[i + 1][1]):
            continue
        ans = max(ans, now)

    print(ans)
