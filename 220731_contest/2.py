from atcoder.atcoder_test import def_input, input

input_text = """
7 10
1 7
5 7
2 5
3 6
4 7
1 5
2 4
1 3
1 6
2 7
"""

def_input(input_text)

import itertools

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    ans = 0
    for a, b, c in itertools.combinations(list(range(n)), 3):
        if ((a in graph[b]) & (a in graph[c])) & ((b in graph[a]) & (b in graph[c])) & ((c in graph[a]) & (c in graph[b])):
            ans += 1
    print(ans)
