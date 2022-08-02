from atcoder.atcoder_test import def_input, input

input_text = """
"""

def_input(input_text)

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [-1] * n
        self.rank = [1] * n

    def find(self, x: int) -> int:
        """根っこ＝親を見つける"""

        # 自分自身が親の場合
        if self.parent[x] == -1:
            return x
        
        tmp =  self.find(self.parent[x])
        self.parent[x] = tmp
        return tmp

    def union(self, x: int, y : int) -> None:
        x = self.find(x)
        y = self.find(y)

        # 親が一緒だったら,unionにする必要はない
        if x == y:
            return 

        if self.rank[x] > self.rank[y]:
            x, y = y, x

        if self.rank[x] == self.rank[y]:
            

        self.parent[x] = y


def main():
    n, q = map(int, input().split())

    uf = UnionFind(n)
    for _ in range(q):
        p, a, b = map(int, input().split())
        a -= 1
        b -= 1

        if p == 0:
            uf.union(a, b)

        if p == 1:
            if uf.find(a) == uf.find(b:
                print("Yes")
            else:
                print("No")
if __name__ == "__main__":
