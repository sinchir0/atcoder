from atcoder.atcoder_test import def_input, input

input_text = """
3
1
4
3
"""

def_input(input_text)

from collections import Counter

if __name__ == "__main__":

    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    A_sorted = sorted(A)

    A_cnt = Counter(A)

    max_num = A_sorted[-1]

    # idxでlistにランダムアクセスした値と、maxの値を比較
    for idx in range(N):

        num = A[idx]
        # もし、ランダムアクセスした値の方が大きい場合
        if num == max_num:
            # collectionで2個以上あるかを確認
            # あったらランダムアクセスした値、なかったらmaxから一つ小さい値
            if A_cnt[num] >= 2:
                print(num)
            else:
                print(A_sorted[-2])
        # もしmaxの値の方が大きい場合
        else:
            print(max_num)