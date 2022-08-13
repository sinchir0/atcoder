from atcoder.atcoder_test import def_input, input

input_text = """
1
"""

def_input(input_text)

if __name__ == "__main__":
    s = int(input())

    a = [False] * (10 ** 6)
    a[s] = True

    cnt = 1
    while True:
        if s % 2 == 0:
            s = s // 2
        else:
            s = 3 * s + 1
        cnt += 1
        if a[s]:
            print(cnt)
            exit()
        a[s] = True
