# 演習：購買ログの解析
# log1：レジごとの購入者のIDのリストです。
# log2：レジごとの「購入商品のIDのタプル」のリストです。
# log1とlog2は対応しています。購入者log1[i]の購入した商品はlog2[i]です。
# 「商品IDが100の商品を購入している購入者」のIDをソートして出力してください。

log1 = [6, 1, 3, 5, 2, 4]

log2 = [(100, ), (115, 110, 180), (120, 100), (120, 131), (115, 100), (100, 115, 119)]


# ヒント
# ソートはsorted(対象)が使えます。
# log1とlog2の対応する要素で繰り返すには、zipが使えます。
# 「商品IDが100の商品を購入しているか」の判断は、inを使えます。
print(sorted([i1 for i1, i2 in zip(log1, log2) if 100 in i2]))


# sorted([i1 for i1, i2 in zip(log1, log2) if 100 in i2]) を分解すると
# 以下のプログラムと同じになる

# tmp = []
# for i1, i2 in zip(log1, log2):
#     if 100 in i2:
#         tmp.append(i1)
# result = sorted(tmp)
