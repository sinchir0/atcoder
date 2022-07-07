from atcoder.atcoder_test import def_input, input

input_text = """
12 10
"""

def_input(input_text)

if __name__ == "__main__":
    a, b = map(str, input().split())
    tmp = int(a + b)
    for num in range(2, 350 * 350):
        if num * num == tmp:
            print("Yes")
            exit()
    print("No")
