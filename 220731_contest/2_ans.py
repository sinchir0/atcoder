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

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    adj = [[False] * n for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = True
        adj[v][u] = True
    
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if adj[i][j] and adj[j][k] and adj[k][i]:
                    ans += 1
    
    print(ans)
