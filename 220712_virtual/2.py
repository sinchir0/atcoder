from atcoder.atcoder_test import def_input, input

input_text = """
3300
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    m = (n // 1000) + 1
    ans = m * 1000 - n
    if ans == 1000:
        print(0)
    else:
        print(ans)
