# リストの内包表記
# リストの内包表記は[要素の式 for 変数 in イテラブル]と書きます。
sq = [i**2 for i in range(10)]
# sq = list(map(lambda i: i**2, range(10)))

print(sq)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
