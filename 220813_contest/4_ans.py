from atcoder.atcoder_test import def_input, input

input_text = """
catredo
"""

def_input(input_text)

from collections import deque

if __name__ == "__main__":
    s = input()

    mp = {}

    queue = deque()
    mp[s] = 0
    queue.append(s)

    while queue:
        current = queue.popleft()
        if current == "atcoder":
            print(mp[current])
            exit()

        for i in range(1, 7):
            next = list(current)
            next[i - 1], next[i] = next[i], next[i - 1]
            next = "".join(next)
            if next not in mp:
                queue.append(next)
                mp[next] = mp[current] + 1
