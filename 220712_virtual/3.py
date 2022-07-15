from atcoder.atcoder_test import def_input, input

input_text = """
RLRLRLRLRL
"""

def_input(input_text)

if __name__ == "__main__":
    s = input()

    odd = list(s[::2])
    even = list(s[1::2])

    if (set(odd) <= {"R", "U", "D"}) and (set(even) <= {"L", "U", "D"}):
        print("Yes")
    else:
        print("No")
