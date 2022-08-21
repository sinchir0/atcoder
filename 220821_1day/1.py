from atcoder.atcoder_test import def_input, input

input_text = """
3
3
1
2
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    a = {}
    for i in range(N):
        a[i] = int(input())

    button = 1
    cnt = 0
    while cnt <= N:
        nxt_button = a[button - 1]
        cnt += 1
        if nxt_button == 2:
            print(cnt)
            exit()
        else:
            button = nxt_button
    print(-1)