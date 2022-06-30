from atcoder.atcoder_test import def_input, input

input_text = """
10 2 3
abccabaabb
"""

def_input(input_text)

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    s = list(input())

    cnt_a = 0
    cnt_b = 0

    for value in s:
        if value == "a":
            if (cnt_a + cnt_b) < a + b:
                print("Yes")
                cnt_a += 1
                continue
        if value == "b":
            if (cnt_a + cnt_b) < a + b:
                if cnt_b < b:
                    print("Yes")
                    cnt_b += 1
                    continue
        print("No")
