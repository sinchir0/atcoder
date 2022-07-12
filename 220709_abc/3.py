from atcoder.atcoder_test import def_input, input

input_text = """
abbaac
abbbbaaac
"""

def_input(input_text)

if __name__ == "__main__":
    s = list(input())
    t = list(input())

    s_i = 0
    t_i = 0

    if s[-1] == s[-2]:
        for _ in range((len(t) - len(s))):
            s.append(s[-1])
    else:
        for _ in range((len(t) - len(s))):
            s.append("1")

    while t_i < len(t):
        if s_i >= 2:
            if s[s_i - 1] == s[s_i - 2]:
                t_val = t[t_i]
                while t[t_i] == t_val:
                    t_i += 1
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()

    print("Yes")
