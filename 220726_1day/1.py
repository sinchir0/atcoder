from atcoder.atcoder_test import def_input, input

input_text = """
454 414 444
"""

def_input(input_text)

if __name__ == "__main__":
    a, b, c = map(int, input().split())

    cnt = 0
    while True:
        if ((a % 2) != 0) | ((b % 2) != 0) | (c % 2) != 0:
            break

        if cnt > 100:
            print(-1)
            exit()
        cnt += 1
        nxt_a = (b // 2) + (c // 2)
        nxt_b = (a // 2) + (c // 2)
        nxt_c = (a // 2) + (b // 2)

        a = nxt_a
        b = nxt_b
        c = nxt_c

    print(cnt)
