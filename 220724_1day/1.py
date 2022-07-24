from atcoder.atcoder_test import def_input, input

input_text = """
3
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())

    ans = 1
    ans_cnt = 0

    for i in range(1, n + 1):
        cnt = 0
        org_num = i
        while True:
            if i % 2 == 0:
                i = i // 2
                cnt += 1
            else:
                break
        if ans_cnt < cnt:
            ans_cnt = cnt
            ans = org_num

    print(ans)
